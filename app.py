import os
import streamlit as st
import tempfile
import pyvista as pv
import panel as pn

# Configurar PyVista para evitar problemas con Jupyter
pv.global_theme.jupyter_backend = None
pn.extension("vtk")

# Título de la app
st.title("Visor de Modelos STL")

# Subir archivo STL
uploaded_file = st.file_uploader("Sube un archivo STL", type=["stl"])

if uploaded_file is not None:
    # Guardar archivo temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".stl") as tmpfile:
        tmpfile.write(uploaded_file.read())
        file_path = tmpfile.name

    # Leer el STL con PyVista
    malha = pv.read(file_path)

    # Crear visualización interactiva
    plotter = pv.Plotter()
    plotter.add_mesh(malha, color="lightblue", show_edges=True)

    # Integrar con Panel para mostrarlo en Streamlit
    pane = pn.pane.VTK(plotter.ren_win, sizing_mode="stretch_both")
    st.write(pane)

    # Eliminar el archivo temporal
    os.remove(file_path)
