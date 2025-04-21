import streamlit as st

st.markdown(
    """
    <div style='text-align: center;'>
        <h1>🌿 Bienvenido/a a EcoMentor 🌿</h1>
        <p>Tu asistente personal para vivir de forma más sostenible.</p>
    </div>
    """,
    unsafe_allow_html=True
)

pg = st.navigation([st.Page("pages/a_page.py"), st.Page("streamlit_app.py")])
pg.run()
