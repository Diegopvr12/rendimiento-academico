import streamlit as st
from games import JuegoMatematicas, JuegoEspanol, JuegoGeografia, JuegoFilosofia
from database import Database

db = Database()

def show():
    st.markdown("# 🎯 Minijuegos Educativos")
    
    if not st.session_state.get('usuario_actual'):
        st.warning("⚠️ Inicia sesión para jugar")
        return
    
    # Crear pestañas para cada juego
    tabs = st.tabs(["🧮 Matemáticas", "📚 Español", "🌍 Geografía", "🤔 Filosofía"])
    
    # Pestaña de Matemáticas
    with tabs[0]:
        juego = JuegoMatematicas()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_math"):
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
    
    # Pestaña de Español
    with tabs[1]:
        juego = JuegoEspanol()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_esp"):
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
    
    # Pestaña de Geografía
    with tabs[2]:
        juego = JuegoGeografia()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_geo"):
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
    
    # Pestaña de Filosofía
    with tabs[3]:
        juego = JuegoFilosofia()
        puntos = juego.jugar()
        
        if puntos > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_fil"):
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
