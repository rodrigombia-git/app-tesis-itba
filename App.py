# App.py (Versión de Prueba sin Login)
import streamlit as st

st.set_page_config(
    page_title="Prueba de Despliegue",
    page_icon="✅",
    layout="centered"
)

st.title("✅ Prueba de Despliegue del Núcleo de la App")
st.success("Si puedes ver esta página, el problema está 100% aislado en el sistema de login.")

st.write("---")
st.header("Navegación:")
st.page_link("pages/1_Dashboard.py", label="Ir al Dashboard", icon="📊")
st.page_link("pages/2_ABM_Tutores.py", label="Ir a ABM Tutores", icon="👨‍🏫")
# ... y así sucesivamente para las otras páginas.