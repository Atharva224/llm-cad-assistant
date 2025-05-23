import streamlit as st
import subprocess
import tempfile
from pathlib import Path
from cad_generator import prompt_to_openscad_code

st.title("LLM-Aided CAD Design Assistant")

prompt = st.text_input("Enter CAD description (e.g., 'hollow cylinder...')")

if prompt:
    code = prompt_to_openscad_code(prompt)
    st.code(code, language='scad')

    # Save to temp file
    with tempfile.NamedTemporaryFile(suffix=".scad", delete=False) as tmp:
        tmp.write(code.encode())
        scad_path = tmp.name

    # Generate PNG using OpenSCAD
    png_path = Path(scad_path).with_suffix(".png")
    subprocess.run(["C:/Program Files/OpenSCAD/openscad.exe", "-o", str(png_path), str(scad_path)])


    st.image(str(png_path), caption="CAD Preview")
