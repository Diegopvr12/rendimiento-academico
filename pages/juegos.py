import streamlit as st
from games import JuegoMatematicas, JuegoEspanol, JuegoGeografia, JuegoFilosofia
from database import Database

db = Database()

def show():
    st.markdown("# 🎯 Minijuegos Educativos")
    
    if not st.session_state.get('usuario_actual'):
        st.warning("⚠️ Por favor, inicia sesión para jugar")
        return
    
    tabs = st.tabs(["🧮 Matemáticas", "📚 Español", "🌍 Geografía", "🤔 Filosofía"])
    
    with tabs[0]:
        juego = JuegoMatematicas()
        puntos = juego.jugar()
        
        if puntos > 0 and st.button("💰 Guardar puntos en mi cuenta", key="save_math"):
            exito, nuevos_logros = db.actualizar_puntos(
                st.session_state.usuario_actual, 
                puntos, 
                "Matemáticas"
            )
            if exito:
                st.success(f"🎉 ¡{puntos} puntos guardados!")
                if nuevos_logros:
                    for logro in nuevos_logros:
                        st.balloons()
                        st.info(f"🏆 ¡Nuevo logro: {logro}!")
                st.session_state.math_puntos = 0
                st.rerun()
    
    with tabs[1]:
        juego = JuegoEspanol()
        puntos = juego.jugar()
        
        if puntos > 0 and st.button("💰 Guardar puntos en mi cuenta", key="save_esp"):
            exito, nuevos_logros = db.actualizar_puntos(
                st.session_state.usuario_actual, 
                puntos, 
                "Español"
            )
            if exito:
                st.success(f"🎉 ¡{puntos} puntos guardados!")
                if nuevos_logros:
                    for logro in nuevos_logros:
                        st.balloons()
                        st.info(f"🏆 ¡Nuevo logro: {logro}!")
                st.session_state.esp_puntos = 0
                st.rerun()
    
    with tabs[2]:
        juego = JuegoGeografia()
        puntos = juego.jugar()
        
        if puntos > 0 and st.button("💰 Guardar puntos en mi cuenta", key="save_geo"):
            exito, nuevos_logros = db.actualizar_puntos(
                st.session_state.usuario_actual, 
                puntos, 
                "Geografía"
            )
            if exito:
                st.success(f"🎉 ¡{puntos} puntos guardados!")
                if nuevos_logros:
                    for logro in nuevos_logros:
                        st.balloons()
                        st.info(f"🏆 ¡Nuevo logro: {logro}!")
                st.session_state.geo_puntos = 0
                st.rerun()
    
    with tabs[3]:
        juego = JuegoFilosofia()
        puntos = juego.jugar()
        
        if puntos > 0 and st.button("💰 Guardar puntos en mi cuenta", key="save_fil"):
            exito, nuevos_logros = db.actualizar_puntos(
                st.session_state.usuario_actual, 
                puntos, 
                "Filosofía"
            )
            if exito:
                st.success(f"🎉 ¡{puntos} puntos guardados!")
                if nuevos_logros:
                    for logro in nuevos_logros:
                        st.balloons()
                        st.info(f"🏆 ¡Nuevo logro: {logro}!")
                st.session_state.fil_puntos = 0
                st.rerun()
