import tempfile
from pathlib import Path

import streamlit as st
from file_processor import procesar  # adapta a tu función

st.title("Procesador de archivos .sgi")

archivo = st.file_uploader("Sube tu archivo .sgi", type=["sgi"])

if archivo and st.button("Procesar"):
    with tempfile.TemporaryDirectory() as tmp:
        ruta_in = Path(tmp) / archivo.name

        ruta_in.write_bytes(archivo.getvalue())

        with st.spinner("Procesando..."):
            ruta_out = procesar(ruta_in)  # tu script

        st.session_state["resultado"] = ruta_out.read_bytes()
        st.session_state["nombre"] = f"resultado_{archivo.name}"

if "resultado" in st.session_state:
    st.success("Listo")
    st.download_button(
        "Descargar resultado",
        st.session_state["resultado"],
        file_name=st.session_state["nombre"],
    )