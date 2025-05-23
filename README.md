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


### ▶️ Run the App

```bash
streamlit run app.py
```

---

### 🛠️ Ensure OpenSCAD is Installed

Download it from: https://openscad.org/downloads/

(Optional) Add OpenSCAD to system PATH if not already:

```bash
# For Windows (adjust if your path is different)
setx PATH "%PATH%;C:\Program Files\OpenSCAD\"
```

---

### Example Prompts

```
Design a hollow cylinder with outer diameter 40mm and thickness 3mm
Create a cube with side 30mm
Generate a torus with major radius 40mm and minor radius 5mm
Make a stepped cylinder with base diameter 30mm, top diameter 20mm, and height 60mm
Generate a hollow cube of 50mm with wall thickness 5mm
Create a plate with 4 holes, spacing 20mm, and hole radius 3mm
```

---

### 📸 Screenshots

Add your rendered screenshots like this:

```markdown
![preview](screenshot1.png)
```

---

### Project Structure

```bash
llm-cad-assistant/
├── app.py              # Streamlit interface
├── cad_generator.py    # Geometry logic and regex parsing
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```
