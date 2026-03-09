import streamlit as st
from games import JuegoMatematicas, JuegoVocabulario, JuegoGeografia
from database import Database

db = Database()

def show():
    st.markdown("## 🎯 **Minijuegos Educativos**")
    
    if not st.session_state.get('usuario_actual'):
        st.warning("⚠️ Por favor, inicia sesión para jugar")
        return
    
    tabs = st.tabs(["🧮 Matemáticas", "📚 Vocabulario", "🌍 Geografía"])
    
    with tabs[0]:
        juego = JuegoMatematicas()
        puntos_actuales = juego.jugar()
        
        # Botón para guardar puntos acumulados
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
                        # Reiniciar puntos del juego
                        st.session_state.math_puntos = 0
                        st.rerun()
    
    with tabs[1]:
        juego = JuegoVocabulario()
        puntos_actuales = juego.jugar()
        
        if puntos_actuales > 0:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💰 Guardar puntos", key="save_voc"):
                    exito, nuevos_logros = db.actualizar_puntos(
                        st.session_state.usuario_actual, 
                        puntos_actuales, 
                        "Vocabulario"
                    )
                    if exito:
                        st.success(f"🎉 ¡{puntos_actuales} puntos guardados en tu cuenta!")
                        if nuevos_logros:
                            for logro in nuevos_logros:
                                st.balloons()
                                st.info(f"🏆 ¡Nuevo logro: {logro}!")
                        st.session_state.voc_puntos = 0
                        st.rerun()
    
    with tabs[2]:
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
