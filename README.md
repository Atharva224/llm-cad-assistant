# llm-cad-assistant


# LLM-Aided CAD Design Assistant

This project converts natural language descriptions like  
`"Create a hollow cylinder with outer diameter 20mm and wall thickness 2mm"`  
into **parametric OpenSCAD code** and renders a real-time **3D preview** using OpenSCAD and Streamlit.

---

## Features

- Prompt-based 3D geometry generation
- Supports shapes: hollow cylinder, solid/hollow cubes, spheres, stepped cylinders, torus, and hole patterns
- Automatic dimension parsing (diameter, height, thickness)
- Real-time OpenSCAD rendering
- Minimal, responsive Streamlit interface

---

## 🚀 Getting Started

### 🔨 Install requirements

```bash
pip install -r requirements.txt
