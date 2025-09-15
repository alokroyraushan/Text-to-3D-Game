# 🌳 Text-to-3D Game Asset Generator

This project was developed by **Alok Kumar (GitHub: alokroyraushan)** as part of the submission for **Red Panda Games Careers**.  
We are building next-gen AI hyper mobile games, and this demonstrates how 3D game assets can be generated and optimized automatically using AI.

---

## 🎮 Why This Project?
Red Panda Games aims to push boundaries in mobile gaming, and this project shows:
- 3D asset generation directly from text prompts using **Shap‑E**  
- Mesh optimization to ensure assets are mobile‑friendly  
- A portfolio of useful foundations (tree, sword, potion, shield, helmet, rock)  
- A backend API (FastAPI) for easy integration into game pipelines  

---

## 🚀 Features
- Generate 3D assets (`.glb` ) from text  
- Mesh simplification & optimization for performance  
- REST API to programmatically request assets  
- Sample portfolio of multiple assets  
- Colab notebook for experimentation  

---

## 📂 Project Structure
```
text-to-3d/
├── api/
│   ├── main.py              # FastAPI backend
│   └── requirements.txt     # Dependencies
├── notebooks/
│   └── Text_to_3D_Game.ipynb   # Colab notebook
├── outputs/                 # Generated 3D models
│   └── (game assets in .glb format)
└── README.md
```

---

## 🔧 Install & Run

### 1️⃣ Colab Experimentation
Open the Colab notebook here:  
[Text-to‑3D Game Asset Generator (Colab)](https://colab.research.google.com/drive/1Jil1QA8wtY4s4abOwS7X3lOM7YRQMRQb?usp=sharing)  
Run all cells to generate assets and sample experiments in browser directly.

### 2️⃣ Local / API Setup
```bash
git clone https://github.com/alokroyraushan/text-to-3d-api.git
cd text-to-3d-api/api
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

- **Health Check**  
```http
GET /
```
Response:
```json
{"message": "API running 🚀"}
```

- **Generate Asset**  
```http
GET /generate?prompt=A+wooden+shield
```
Response:
```json
FileResponse → asset.glb download
```

---

## 🎮 Portfolio Assets
Generated assets include:
- 🌳 Low‑poly Tree  
- 🗡️ Fantasy Sword  
- 🛡️ Wooden Shield  
- 🧪 Potion Bottle  
- ⛑️ Helmet  
- 🪨 Rock  

All assets are optimized (mesh reduction) for better performance on mobile.

---

## 📢 Submission Summary

This repository contains the **Text-to-3D Game Asset Generator** project developed by **Alok Kumar** for **Red Panda Games Careers**.

### 1️⃣ GitHub Repo Contents
- **Code:** Colab notebook (`Text-to-3D Game.ipynb`) and optional API scripts.  
- **README:** Detailed instructions to run the project and understand outputs.  
- **Sample Outputs:** Optimized `.glb` files in the `outputs/` folder. Screenshots can be added for visualization.

### 2️⃣ Model / Tool Used
- **Tool:** Shap‑E  
- **Reason:** Automatically generates 3D assets from text prompts. Supports mesh optimization for mobile-friendly performance.

### 3️⃣ Input Parameters Tested
- **Guidance Scales:** `[7.0, 12.0, 15.0, 18.0, 25.0]`  
- **Steps:** `[32, 64, 128]`  
- **Optimal Trade-Off:** Scale = `12.0`, Steps = `32`

### 4️⃣ Observations
- Increasing **steps** slightly improved mesh quality but increased runtime.  
- Adjusting **guidance scale** affected mesh style and complexity.  
- Mesh simplification reduced triangles by ~1.4–3.4% without noticeable visual degradation.  

### 5️⃣ Post-Processing & Optimization
| Asset | Original Triangles | Reduced Triangles | Reduction % |
|-------|------------------|-----------------|-------------|
| Low-poly Tree | 99,128 | 97,628 | 1.5% |
| Simple Tree (Mobile) | 78,416 | 76,916 | 1.9% |
| Minimalist Tree | 86,472 | 84,972 | 1.7% |
| Game-ready Tree | 74,804 | 73,304 | 2.0% |
| Optimized Tree | 46,416 | 44,916 | 3.2% |
| Fantasy Sword | 59,652 | 57,652 | 3.4% |
| Potion | 141,980 | 139,980 | 1.4% |
| Shield | 60,752 | 58,752 | 3.3% |
| Helmet | 126,932 | 124,932 | 1.6% |
| Rock | 120,984 | 118,984 | 1.7% |



### 8️⃣ Repository Link
[https://github.com/alokroyraushan/Text-to-3D-Game](https://github.com/alokroyraushan/Text-to-3D-Game)  

This submission provides **code, Colab notebook, optimized `.glb` assets, and a detailed summary** of experiments and observations.

---

## 🖼️ Visualizations & Screenshots

The generated 3D game assets (`.glb` files) can be visualized and explored interactively.  
You can view/download all assets from the shared Drive link:

[View 3D Assets on Google Drive](https://drive.google.com/file/d/1N59QL3d8bIlgqCy-rBfUnN40SKQdFyvX/view?usp=sharing)

---

## 📦 Requirements
- Python 3.10+  
- CUDA GPU (optional for speed)  
- Dependencies as listed in `requirements.txt`

---

## 👨‍💻 Author
**Alok Kumar** (GitHub: alokroyraushan)  
Email: alokroyraushan@gmail.com  

---

## 📝 License
MIT License © 2025 Alok Kumar
