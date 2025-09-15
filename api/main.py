import os
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import torch
import numpy as np
import trimesh
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
from shap_e.util.notebooks import decode_latent_mesh

# -----------------------------
# Environment + FastAPI setup
# -----------------------------
os.makedirs("outputs", exist_ok=True)
app = FastAPI()

# -----------------------------
# Device + Models
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

xm = load_model("transmitter", device=device)
model = load_model("text300M", device=device)
diffusion = diffusion_from_config(load_config("diffusion"))
print("✅ Models loaded successfully!")

# -----------------------------
# 3D Generation & Save Helpers
# -----------------------------
def gen_3d(prompt, scale=12.0, steps=32):
    """
    Generate 3D asset from text prompt
    """
    latents = sample_latents(
        batch_size=1,
        model=model,
        diffusion=diffusion,
        guidance_scale=scale,
        model_kwargs=dict(texts=[prompt]),
        progress=True,
        clip_denoised=True,
        use_fp16=True,
        use_karras=True,
        karras_steps=steps,
        sigma_min=1e-3,
        sigma_max=160,
        s_churn=0,
    )
    with torch.no_grad():
        mesh = decode_latent_mesh(xm, latents[0]).tri_mesh()
    return mesh

def save_mesh(mesh, fname):
    """
    Save mesh as .obj + .glb and return GLB path
    """
    obj_file = f"outputs/{fname}.obj"
    mesh.export(obj_file)
    glb_file = f"outputs/{fname}.glb"
    mesh.export(glb_file)
    return glb_file

# -----------------------------
# FastAPI Endpoints
# -----------------------------
@app.get("/")
def root():
    return {"message": "Shap-E 3D Generator API running 🚀"}

@app.get("/generate")
def generate(prompt: str = Query(..., description="Text prompt for 3D model")):
    """
    Generate 3D model from prompt and return .glb file
    """
    mesh = gen_3d(prompt)
    glb_file = save_mesh(mesh, "asset")
    return FileResponse(glb_file, media_type="model/gltf-binary", filename="asset.glb")
