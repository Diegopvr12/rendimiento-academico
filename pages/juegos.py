import streamlit as st
from games import JuegoMatematicas, JuegoEspanol, JuegoGeografia, JuegoFilosofia
from database import Database

db = Database()

def show():
    st.markdown("## 🎯 **Minijuegos Educativos**")
    
    if not st.session_state.get('usuario_actual'):
        st.warning("⚠️ Por favor, inicia sesión para jugar")
        return
    
    # Ahora tenemos 5 juegos
    tabs = st.tabs(["🧮 Matemáticas", "📚 Español", "🌍 Geografía", "🤔 Filosofía", "🎲 Todos"])
    
    # ===== MATEMÁTICAS =====
    with tabs[0]:
        st.markdown("### 🧮 Matemáticas Rápidas")
        st.caption("Pon a prueba tu agilidad mental con operaciones básicas")
        juego = JuegoMatematicas()
        puntos_actuales = juego.jugar()
        
        if puntos_actuales > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_math"):
                    exito, nuevos_logros = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos_actuales, 
                        "Matemáticas"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos_actuales} puntos guardados en tu cuenta!")
                        if nuevos_logros:
                            for logro in nuevos_logros:
                                st.balloons()
                                st.info(f"🏆 ¡Nuevo logro: {logro}!")
                        st.session_state.math_puntos = 0
                        st.rerun()
    
    # ===== ESPAÑOL =====
    with tabs[1]:
        st.markdown("### 📚 Español - Lengua y Literatura")
        st.caption("Gramática, ortografía, sinónimos y más")
        juego = JuegoEspanol()
        puntos_actuales = juego.jugar()
        
        if puntos_actuales > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_esp"):
                    exito, nuevos_logros = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos_actuales, 
                        "Español"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos_actuales} puntos guardados en tu cuenta!")
                        if nuevos_logros:
                            for logro in nuevos_logros:
                                st.balloons()
                                st.info(f"🏆 ¡Nuevo logro: {logro}!")
                        st.session_state.esp_puntos = 0
                        st.rerun()
    
    # ===== GEOGRAFÍA =====
    with tabs[2]:
        st.markdown("### 🌍 Geografía Mundial")
        st.caption("Capitales, países y datos curiosos")
        juego = JuegoGeografia()
        puntos_actuales = juego.jugar()
        
        if puntos_actuales > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_geo"):
                    exito, nuevos_logros = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos_actuales, 
                        "Geografía"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos_actuales} puntos guardados en tu cuenta!")
                        if nuevos_logros:
                            for logro in nuevos_logros:
                                st.balloons()
                                st.info(f"🏆 ¡Nuevo logro: {logro}!")
                        st.session_state.geo_puntos = 0
                        st.rerun()
    
    # ===== FILOSOFÍA =====
    with tabs[3]:
        st.markdown("### 🤔 Filosofía")
        st.caption("Pensadores, corrientes y conceptos filosóficos")
        juego = JuegoFilosofia()
        puntos_actuales = juego.jugar()
        
        if puntos_actuales > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_fil"):
                    exito, nuevos_logros = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos_actuales, 
                        "Filosofía"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos_actuales} puntos guardados en tu cuenta!")
                        if nuevos_logros:
                            for logro in nuevos_logros:
                                st.balloons()
                                st.info(f"🏆 ¡Nuevo logro: {logro}!")
                        st.session_state.fil_puntos = 0
                        st.rerun()
    
    # ===== TODOS LOS JUEGOS =====
    with tabs[4]:
        st.markdown("### 🎲 Todos los Juegos")
        st.caption("Selecciona el juego que prefieras")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background:linear-gradient(135deg,#FF6B6B,#FF8E8E);padding:1.5rem;border-radius:15px;text-align:center;color:white;">
                <h1>🧮</h1>
                <h3>Matemáticas</h3>
                <p>10 pts por acierto</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Jugar Matemáticas", key="all_math"):
                st.session_state.pagina = "Juegos"
                st.rerun()
        
        with col2:
            st.markdown("""
            <div style="background:linear-gradient(135deg,#4ECDC4,#6EE7E0);padding:1.5rem;border-radius:15px;text-align:center;color:white;">
                <h1>📚</h1>
                <h3>Español</h3>
                <p>15 pts por acierto</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Jugar Español", key="all_esp"):
                st.session_state.pagina = "Juegos"
                st.rerun()
        
        with col3:
            st.markdown("""
            <div style="background:linear-gradient(135deg,#FFD93D,#FFE15D);padding:1.5rem;border-radius:15px;text-align:center;color:white;">
                <h1>🌍</h1>
                <h3>Geografía</h3>
                <p>20 pts por acierto</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Jugar Geografía", key="all_geo"):
                st.session_state.pagina = "Juegos"
                st.rerun()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div style="background:linear-gradient(135deg,#9B59B6,#8E44AD);padding:1.5rem;border-radius:15px;text-align:center;color:white;">
                <h1>🤔</h1>
                <h3>Filosofía</h3>
                <p>25 pts por acierto</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Jugar Filosofía", key="all_fil"):
                st.session_state.pagina = "Juegos"
                st.rerun()
