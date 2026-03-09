import streamlit as st
from games import (
    JuegoMatematicas, 
    JuegoEspanol, 
    JuegoGeografia, 
    JuegoHistoria, 
    JuegoFilosofia
)
from database import Database

db = Database()

def show():
    st.markdown("# 🎯 Minijuegos Educativos")
    
    if not st.session_state.get('usuario_actual'):
        st.warning("⚠️ Inicia sesión para jugar")
        return
    
    # Crear pestañas para cada juego
    tabs = st.tabs([
        "🧮 Matemáticas", 
        "📚 Español", 
        "🌍 Geografía", 
        "📜 Historia", 
        "🤔 Filosofía"
    ])
    
    # ===== MATEMÁTICAS =====
    with tabs[0]:
        st.markdown("### 🧮 Matemáticas Rápidas")
        st.caption("Pon a prueba tu agilidad mental con operaciones básicas")
        
        juego = JuegoMatematicas()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("💰 Guardar puntos", key="save_math", use_container_width=True):
                    exito, nuevos = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos, 
                        "Matemáticas"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos} puntos guardados!")
                        if nuevos:
                            for logro in nuevos:
                                st.balloons()
                                st.info(f"🏆 {logro}")
                        st.session_state.math_puntos = 0
                        st.rerun()
    
    # ===== ESPAÑOL =====
    with tabs[1]:
        st.markdown("### 📚 Español")
        st.caption("Pon a prueba tu conocimiento del idioma")
        
        juego = JuegoEspanol()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("💰 Guardar puntos", key="save_esp", use_container_width=True):
                    exito, nuevos = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos, 
                        "Español"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos} puntos guardados!")
                        if nuevos:
                            for logro in nuevos:
                                st.balloons()
                                st.info(f"🏆 {logro}")
                        st.session_state.esp_puntos = 0
                        st.rerun()
    
    # ===== GEOGRAFÍA =====
    with tabs[2]:
        st.markdown("### 🌍 Geografía")
        st.caption("Adivina las capitales del mundo")
        
        juego = JuegoGeografia()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("💰 Guardar puntos", key="save_geo", use_container_width=True):
                    exito, nuevos = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos, 
                        "Geografía"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos} puntos guardados!")
                        if nuevos:
                            for logro in nuevos:
                                st.balloons()
                                st.info(f"🏆 {logro}")
                        st.session_state.geo_puntos = 0
                        st.rerun()
    
    # ===== HISTORIA =====
    with tabs[3]:
        st.markdown("### 📜 Historia")
        st.caption("Viaja a través del tiempo y aprende historia")
        
        juego = JuegoHistoria()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("💰 Guardar puntos", key="save_hist", use_container_width=True):
                    exito, nuevos = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos, 
                        "Historia"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos} puntos guardados!")
                        if nuevos:
                            for logro in nuevos:
                                st.balloons()
                                st.info(f"🏆 {logro}")
                        st.session_state.hist_puntos = 0
                        st.rerun()
    
    # ===== FILOSOFÍA =====
    with tabs[4]:
        st.markdown("### 🤔 Filosofía")
        st.caption("Explora el mundo de las ideas")
        
        juego = JuegoFilosofia()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("💰 Guardar puntos", key="save_fil", use_container_width=True):
                    exito, nuevos = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos, 
                        "Filosofía"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos} puntos guardados!")
                        if nuevos:
                            for logro in nuevos:
                                st.balloons()
                                st.info(f"🏆 {logro}")
                        st.session_state.fil_puntos = 0
                        st.rerun()
