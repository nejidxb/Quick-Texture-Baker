# 🧩 Quick Texture Baker

**Quick Texture Baker** is a lightweight ![Blender 4.0+](https://img.shields.io/badge/Blender-4.0%2B-orange?logo=blender) add-on designed for artists, modders, and developers who want to **create and bake textures quickly** without navigating deep into Blender’s shader or render settings.  

It automates **image texture node creation** and **diffuse baking** for the selected mesh, making it perfect for both manual workflows and automated 3D pipelines.

---

## ✨ Features

- 🖼️ **Create Image Texture Nodes** — Instantly create a new texture node and assign a 1024×1024 image.
- 🔥 **One-Click Baking** — Bake the selected mesh’s material directly to the chosen image (Diffuse only).
- ⚙️ **Automatic Setup** — Automatically configures render engine (Cycles) and bake settings.
- 🧠 **Smart Handling** — Detects missing materials, existing images, and prevents bake errors.
- 🎨 **Ideal For:** Model preparation, character baking, or texture export pipelines.

---

## 🧩 Installation (In Blender)
1. Click this button to download the add-on ZIP:  
   [![Download Add-on](https://img.shields.io/badge/⬇️%20Download%20Addon-ZIP-blue?style=for-the-badge&logo=github)](https://github.com/<your-username>/Quick-Texture-Baker/releases/latest/download/Quick-Texture-Baker.zip)

2. Go to **Edit → Preferences → Add-ons → Install**  
3. Select the downloaded **`.zip` file** or the **add-on folder**  
4. Enable ✅ **Quick Texture Baker** in the add-ons list

---

## 🚀 Usage

1. **Select an object** that has a material applied  
2. Open **Sidebar → Quick Texture Baker** (in the **3D Viewport**)  
3. Enter a **Texture Name** (e.g., `Body`, `Hand`, etc.)  
4. Click **Create Texture Node** — a new image texture node is created and linked automatically  
5. Click **Bake to Texture (Diffuse)** — the add-on will automatically:  
   - Switch the render engine to **Cycles**  
   - Set the bake type to **Diffuse**  
   - Disable **Direct** and **Indirect** lighting  
   - Bake to the **selected image texture node**

✅ The baked texture will appear in the **Image Editor** and be stored in **Blender’s image data** list.

---

## 📂 File Structure
```
Quick-Texture-Baker/
│
├── __init__.py              # Add-on entry point (registers all modules)
├── ui.py                    # UI panel for Create & Bake buttons
├── ops_create_texture.py    # Operator to create texture image nodes
└── ops_bake_texture.py      # Operator to bake materials to image textures
```

---

## 🧩 Add-on Modules

### `ops_create_texture.py`
- Creates a new **Image Texture Node** with a custom name  
- Links it to the active material  
- Reuses existing images if they already exist  

### `ops_bake_texture.py`
- Automates **Diffuse baking** for the active mesh  
- Configures materials, nodes, and render settings automatically  
- Executes `bpy.ops.object.bake()` safely with error handling  

### `ui.py`
- Provides the **Quick Texture Baker** panel in  
  **3D View → Sidebar → Quick Texture Baker**
- Contains:  
  - 🧱 Texture Name input field  
  - 🎨 “Create Texture Node” button  
  - 🔥 “Bake to Texture (Diffuse)” button  

---

## 📜 License

This add-on is released under the **GNU General Public License v3.0 (GPLv3)**.  
You are free to use, modify, and redistribute it under the same license.  
This program comes with **ABSOLUTELY NO WARRANTY**; see the [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE) for details.

**© 2025 Sudhanshu Ambastha**

---

> “**Quick Texture Baker** is built to simplify one of the most repetitive steps in Blender — baking textures — while staying lightweight, transparent, and artist-friendly.”
