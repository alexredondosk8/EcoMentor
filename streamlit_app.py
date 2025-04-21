import streamlit as st

def registrar_usuario():
    st.sidebar.header("👤 Registro de Usuario")
    
    nombre = st.sidebar.text_input("Nombre")
    edad = st.sidebar.number_input("Edad", min_value=5, max_value=100, step=1)
    intereses = st.sidebar.multiselect(
        "Intereses sostenibles", 
        ["Hogar", "Transporte", "Consumo responsable", "Energía", "Agua"]
    )

    if st.sidebar.button("Registrarme"):
        if nombre and intereses:
            st.session_state["usuario"] = {
                "nombre": nombre,
                "edad": edad,
                "intereses": intereses
            }
            st.sidebar.success(f"¡Bienvenido/a, {nombre}!")
        else:
            st.sidebar.error("Por favor, completa todos los campos obligatorios.")

def mostrar_bienvenida():
    usuario = st.session_state.get("usuario")
    if usuario:
        st.write(f"Hola **{usuario['nombre']}** 👋, estas son tus recomendaciones personalizadas según tus intereses:")
