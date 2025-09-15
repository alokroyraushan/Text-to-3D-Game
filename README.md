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

## ⚙️ Parameters & Experimentation
- Tested **guidance scales**: `[7.0, 12.0, 15.0, 18.0, 25.0]`  
- Tested **steps**: `[32, 64, 128]`  
- Found optimal trade‑off at **scale = 12.0**, **steps = 32**  

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
