"""EduPlay - Sistema de Rendimiento Académico"""
import streamlit as st
from database import Database
from helpers import calcular_nivel

# Configuración de la página - DEBE SER LO PRIMERO
st.set_page_config(
    page_title="EduPlay - Aprende Jugando",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar variables de sesión
if 'usuario_actual' not in st.session_state:
    st.session_state.usuario_actual = None
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

# Inicializar base de datos
db = Database()

# Sidebar
with st.sidebar:
    st.markdown("# 🎮 **EduPlay**")
    st.markdown("---")
    
    # Menú de navegación
    if st.button("🏠 Inicio", use_container_width=True):
        st.session_state.pagina = "Inicio"
        st.rerun()
    
    if st.button("🎯 Juegos", use_container_width=True):
        st.session_state.pagina = "Juegos"
        st.rerun()
    
    if st.button("📊 Mi Progreso", use_container_width=True):
        st.session_state.pagina = "Progreso"
        st.rerun()
    
    if st.button("🏆 Ranking", use_container_width=True):
        st.session_state.pagina = "Ranking"
        st.rerun()
    
    st.markdown("---")
    
    # Sección de usuario
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
        with st.form("login_form"):
            nombre = st.text_input("👤 Nombre de usuario", placeholder="Ej: Ana123")
            if st.form_submit_button("🎮 Jugar", use_container_width=True):
                if nombre:
                    st.session_state.usuario_actual = nombre
                    db.obtener_usuario(nombre)
                    st.rerun()
                else:
                    st.error("Por favor ingresa un nombre")

# Contenido principal
if st.session_state.pagina == "Inicio":
    try:
        from pages import inicio
        inicio.show()
    except:
        st.markdown("# 🎮 Bienvenido a EduPlay")
        st.markdown("### La plataforma que hace del aprendizaje una experiencia divertida")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("### 🧮 Matemáticas")
        with col2:
            st.markdown("### 📚 Español")
        with col3:
            st.markdown("### 🌍 Geografía")
        with col4:
            st.markdown("### 🤔 Filosofía")

elif st.session_state.pagina == "Juegos":
    try:
        from pages import juegos
        juegos.show()
    except:
        st.markdown("# 🎯 Juegos")
        st.info("Selecciona un juego de la barra lateral")

elif st.session_state.pagina == "Progreso":
    if not st.session_state.usuario_actual:
        st.warning("⚠️ Inicia sesión para ver tu progreso")
    else:
        st.markdown("# 📊 Mi Progreso")
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
            st.markdown("### 🏆 Mis Logros")
            cols = st.columns(3)
            for i, logro in enumerate(datos['logros']):
                with cols[i % 3]:
                    st.markdown(f"✅ {logro}")
        
        if datos['historial']:
            st.markdown("### 📜 Historial Reciente")
            for partida in datos['historial'][-5:]:
                st.markdown(f"- {partida['fecha']}: {partida['juego']} (+{partida['puntos']} pts)")

elif st.session_state.pagina == "Ranking":
    st.markdown("# 🏆 Ranking de Jugadores")
    ranking = db.obtener_ranking()
    
    for i, jugador in enumerate(ranking[:10]):
        if i == 0:
            st.markdown(f"🥇 **{jugador['usuario']}** - ⭐ {jugador['puntos']} pts")
        elif i == 1:
            st.markdown(f"🥈 **{jugador['usuario']}** - ⭐ {jugador['puntos']} pts")
        elif i == 2:
            st.markdown(f"🥉 **{jugador['usuario']}** - ⭐ {jugador['puntos']} pts")
        else:
            st.markdown(f"{i+1}. **{jugador['usuario']}** - ⭐ {jugador['puntos']} pts")
