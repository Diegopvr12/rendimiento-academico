import streamlit as st
from games import JuegoMatematicas, JuegoGeografia
from database import Database

db = Database()

def show():
    st.markdown("# 🎯 Minijuegos")
    
    if not st.session_state.get('usuario_actual'):
        st.warning("⚠️ Inicia sesión para jugar")
        return
    
    tabs = st.tabs(["🧮 Matemáticas", "🌍 Geografía"])
    
    with tabs[0]:
        juego = JuegoMatematicas()
        puntos = juego.jugar()
        
        if puntos > 0:
            if st.button("💰 Guardar puntos en mi cuenta", key="save_math"):
                exito, nuevos = db.actualizar_puntos(st.session_state.usuario_actual, puntos, "Matemáticas")
                if exito:
                    st.success(f"🎉 ¡{puntos} puntos guardados!")
                    st.session_state.math_puntos = 0
                    st.rerun()
    
    with tabs[1]:
        juego = JuegoGeografia()
        puntos = juego.jugar()
        
        if puntos > 0:
            if st.button("💰 Guardar puntos en mi cuenta", key="save_geo"):
                exito, nuevos = db.actualizar_puntos(st.session_state.usuario_actual, puntos, "Geografía")
                if exito:
                    st.success(f"🎉 ¡{puntos} puntos guardados!")
                    st.session_state.geo_puntos = 0
                    st.rerun()
