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
        puntos_ganados = juego.jugar()
        
        if puntos_ganados > 0 and st.button("✅ Guardar puntos", key="save_math"):
            exito, nuevos_logros = db.actualizar_puntos(
                st.session_state.usuario_actual, 
                puntos_ganados, 
                "Matemáticas"
            )
            if exito:
                st.success(f"🎉 +{puntos_ganados} puntos guardados!")
                if nuevos_logros:
                    for logro in nuevos_logros:
                        st.balloons()
                        st.info(f"🏆 ¡Nuevo logro: {logro}!")
    
    with tabs[1]:
        juego = JuegoVocabulario()
        puntos_ganados = juego.jugar()
        
        if puntos_ganados > 0 and st.button("✅ Guardar puntos", key="save_voc"):
            exito, nuevos_logros = db.actualizar_puntos(
                st.session_state.usuario_actual, 
                puntos_ganados, 
                "Vocabulario"
            )
            if exito:
                st.success(f"🎉 +{puntos_ganados} puntos guardados!")
                if nuevos_logros:
                    for logro in nuevos_logros:
                        st.balloons()
                        st.info(f"🏆 ¡Nuevo logro: {logro}!")
    
    with tabs[2]:
        juego = JuegoGeografia()
        puntos_ganados = juego.jugar()
        
        if puntos_ganados > 0 and st.button("✅ Guardar puntos", key="save_geo"):
            exito, nuevos_logros = db.actualizar_puntos(
                st.session_state.usuario_actual, 
                puntos_ganados, 
                "Geografía"
            )
            if exito:
                st.success(f"🎉 +{puntos_ganados} puntos guardados!")
                if nuevos_logros:
                    for logro in nuevos_logros:
                        st.balloons()
                        st.info(f"🏆 ¡Nuevo logro: {logro}!")
