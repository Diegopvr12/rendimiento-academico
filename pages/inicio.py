import streamlit as st
from database import Database

db = Database()

def show():
    st.markdown("""
    <style>
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin-bottom: 2rem;
        }
        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            height: 100%;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero">
        <h1>🎮 Bienvenido a EduPlay</h1>
        <p style="font-size:1.2rem;">La plataforma que hace del aprendizaje una experiencia divertida</p>
    </div>
    """, unsafe_allow_html=True)
    
    stats = db.obtener_estadisticas_globales()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👥 Usuarios", stats['total_usuarios'])
    with col2:
        st.metric("⭐ Puntos Totales", f"{stats['total_puntos']:,}")
    with col3:
        st.metric("🎮 Partidas", stats['total_juegos'])
    with col4:
        st.metric("📊 Juegos", "4")
    
    st.markdown("## 🚀 **Características**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h1>🧮</h1>
            <h3>Matemáticas</h3>
            <p>Operaciones básicas y álgebra</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h1>📚</h1>
            <h3>Vocabulario</h3>
            <p>Amplía tu léxico</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h1>🌍</h1>
            <h3>Geografía</h3>
            <p>Capitales del mundo</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <h1>🏆</h1>
            <h3>Logros</h3>
            <p>Desbloquea recompensas</p>
        </div>
        """, unsafe_allow_html=True)
    
    if not st.session_state.get('usuario_actual'):
        st.info("👆 Inicia sesión en la barra lateral para comenzar a jugar")
