"""EduPlay - Sistema de Rendimiento Académico"""
import streamlit as st
from database import Database
from helpers import calcular_nivel

st.set_page_config(
    page_title="EduPlay",
    page_icon="🎮",
    layout="wide"
)

if 'usuario_actual' not in st.session_state:
    st.session_state.usuario_actual = None

db = Database()

with st.sidebar:
    st.markdown("# 🎮 **EduPlay**")
    st.markdown("---")
    
    pagina = st.radio(
        "Navegación",
        ["🏠 Inicio", "🎯 Juegos", "📊 Mi Progreso", "🏆 Ranking"],
        key="nav"
    )
    
    st.markdown("---")
    
    if st.session_state.usuario_actual:
        usuario = st.session_state.usuario_actual
        datos = db.obtener_usuario(usuario)
        
        st.markdown(f"""
        ### 👤 **{usuario}**
        - ⭐ Puntos: {datos['puntos']}
        - 🎮 Juegos: {datos['juegos_completados']}
        - 📊 Nivel: {calcular_nivel(datos['puntos'])}
        """)
        
        if st.button("🚪 Cerrar Sesión", use_container_width=True):
            st.session_state.usuario_actual = None
            st.rerun()
    else:
        with st.form("login"):
            nombre = st.text_input("👤 Usuario")
            if st.form_submit_button("🎮 Jugar", use_container_width=True):
                if nombre:
                    st.session_state.usuario_actual = nombre
                    db.obtener_usuario(nombre)
                    st.rerun()

if pagina == "🏠 Inicio":
    from pages import inicio
    inicio.show()
elif pagina == "🎯 Juegos":
    from pages import juegos
    juegos.show()
elif pagina == "📊 Mi Progreso":
    if not st.session_state.usuario_actual:
        st.warning("⚠️ Inicia sesión para ver tu progreso")
    else:
        st.markdown("## 📊 **Mi Progreso**")
        usuario = st.session_state.usuario_actual
        datos = db.obtener_usuario(usuario)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("⭐ Puntos Totales", datos['puntos'])
        with col2:
            st.metric("🎮 Juegos Completados", datos['juegos_completados'])
        with col3:
            st.metric("📊 Nivel", calcular_nivel(datos['puntos']))
        
        if datos['logros']:
            st.markdown("### 🏆 **Mis Logros**")
            cols = st.columns(3)
            for i, logro in enumerate(datos['logros']):
                with cols[i % 3]:
                    st.markdown(f"✅ {logro}")
        
        if datos['historial']:
            st.markdown("### 📜 **Historial Reciente**")
            for partida in datos['historial'][-5:]:
                st.markdown(f"- {partida['fecha']}: {partida['juego']} (+{partida['puntos']} pts)")
elif pagina == "🏆 Ranking":
    st.markdown("## 🏆 **Ranking de Jugadores**")
    ranking = db.obtener_ranking()
    
    for i, jugador in enumerate(ranking[:10]):
        medalla = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}."
        st.markdown(f"""
        {medalla} **{jugador['usuario']}**  
        ⭐ {jugador['puntos']} pts | 🎮 {jugador['juegos']} juegos | 📊 Nivel {jugador['nivel']}
        """)
