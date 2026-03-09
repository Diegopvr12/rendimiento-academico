"""Juegos educativos para EduPlay"""
import streamlit as st
import random

# ============================================
# JUEGO DE MATEMÁTICAS (CORREGIDO)
# ============================================
class JuegoMatematicas:
    def __init__(self):
        if 'math_puntos' not in st.session_state:
            st.session_state.math_puntos = 0
        if 'math_num1' not in st.session_state:
            st.session_state.math_num1 = None
        if 'math_num2' not in st.session_state:
            st.session_state.math_num2 = None
        if 'math_operador' not in st.session_state:
            st.session_state.math_operador = None
        if 'math_resultado' not in st.session_state:
            st.session_state.math_resultado = None
        if 'math_opciones' not in st.session_state:
            st.session_state.math_opciones = []
        if 'math_respondido' not in st.session_state:
            st.session_state.math_respondido = False
        if 'math_mensaje' not in st.session_state:
            st.session_state.math_mensaje = None
        
        # Generar primera pregunta si no existe
        if st.session_state.math_num1 is None:
            self.generar_pregunta()
    
    def generar_pregunta(self):
        """Genera una nueva pregunta"""
        # Elegir operador
        operador = random.choice(['+', '-', '×'])
        
        if operador == '+':
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            resultado = num1 + num2
        elif operador == '-':
            num1 = random.randint(5, 20)
            num2 = random.randint(1, num1)
            resultado = num1 - num2
        else:  # ×
            num1 = random.randint(2, 10)
            num2 = random.randint(2, 10)
            resultado = num1 * num2
        
        # Generar opciones
        opciones = [resultado]
        while len(opciones) < 4:
            op = resultado + random.randint(-5, 5)
            if op not in opciones and op > 0:
                opciones.append(op)
        
        random.shuffle(opciones)
        
        # Guardar en sesión
        st.session_state.math_num1 = num1
        st.session_state.math_num2 = num2
        st.session_state.math_operador = operador
        st.session_state.math_resultado = resultado
        st.session_state.math_opciones = opciones
        st.session_state.math_respondido = False
        st.session_state.math_mensaje = None
    
    def jugar(self):
        st.markdown("## 🧮 Matemáticas Rápidas")
        st.caption("Pon a prueba tu agilidad mental")
        
        # Mostrar puntos
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Puntos en esta partida", st.session_state.math_puntos)
        
        # Mostrar mensaje si existe
        if st.session_state.math_mensaje:
            if "✅" in st.session_state.math_mensaje:
                st.success(st.session_state.math_mensaje)
            else:
                st.error(st.session_state.math_mensaje)
        
        # Mostrar la pregunta
        num1 = st.session_state.math_num1
        num2 = st.session_state.math_num2
        operador = st.session_state.math_operador
        
        st.markdown(f"## **{num1} {operador} {num2} = ?**")
        
        # Mostrar opciones en 2 columnas
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(f"**{st.session_state.math_opciones[0]}**", key="math_1", use_container_width=True, disabled=st.session_state.math_respondido):
                if st.session_state.math_opciones[0] == st.session_state.math_resultado:
                    st.session_state.math_puntos += 10
                    st.session_state.math_mensaje = "✅ ¡Correcto! +10 puntos"
                    st.balloons()
                else:
                    st.session_state.math_mensaje = f"❌ Incorrecto. La respuesta era {st.session_state.math_resultado}"
                st.session_state.math_respondido = True
                st.rerun()
            
            if st.button(f"**{st.session_state.math_opciones[1]}**", key="math_2", use_container_width=True, disabled=st.session_state.math_respondido):
                if st.session_state.math_opciones[1] == st.session_state.math_resultado:
                    st.session_state.math_puntos += 10
                    st.session_state.math_mensaje = "✅ ¡Correcto! +10 puntos"
                    st.balloons()
                else:
                    st.session_state.math_mensaje = f"❌ Incorrecto. La respuesta era {st.session_state.math_resultado}"
                st.session_state.math_respondido = True
                st.rerun()
        
        with col2:
            if st.button(f"**{st.session_state.math_opciones[2]}**", key="math_3", use_container_width=True, disabled=st.session_state.math_respondido):
                if st.session_state.math_opciones[2] == st.session_state.math_resultado:
                    st.session_state.math_puntos += 10
                    st.session_state.math_mensaje = "✅ ¡Correcto! +10 puntos"
                    st.balloons()
                else:
                    st.session_state.math_mensaje = f"❌ Incorrecto. La respuesta era {st.session_state.math_resultado}"
                st.session_state.math_respondido = True
                st.rerun()
            
            if st.button(f"**{st.session_state.math_opciones[3]}**", key="math_4", use_container_width=True, disabled=st.session_state.math_respondido):
                if st.session_state.math_opciones[3] == st.session_state.math_resultado:
                    st.session_state.math_puntos += 10
                    st.session_state.math_mensaje = "✅ ¡Correcto! +10 puntos"
                    st.balloons()
                else:
                    st.session_state.math_mensaje = f"❌ Incorrecto. La respuesta era {st.session_state.math_resultado}"
                st.session_state.math_respondido = True
                st.rerun()
        
        # Botón siguiente pregunta (solo si ya respondió)
        if st.session_state.math_respondido:
            if st.button("➡️ Siguiente Pregunta", key="math_next", use_container_width=True):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.math_puntos


# ============================================
# JUEGO DE ESPAÑOL
# ============================================
class JuegoEspanol:
    def __init__(self):
        if 'esp_puntos' not in st.session_state:
            st.session_state.esp_puntos = 0
        if 'esp_pregunta' not in st.session_state:
            st.session_state.esp_pregunta = None
        if 'esp_correcta' not in st.session_state:
            st.session_state.esp_correcta = None
        if 'esp_opciones' not in st.session_state:
            st.session_state.esp_opciones = []
        if 'esp_respondido' not in st.session_state:
            st.session_state.esp_respondido = False
        if 'esp_mensaje' not in st.session_state:
            st.session_state.esp_mensaje = None
        
        self.preguntas = [
            {
                'pregunta': '¿Cuál es el sinónimo de "alegría"?',
                'opciones': ['Felicidad', 'Tristeza', 'Enojo', 'Miedo'],
                'correcta': 'Felicidad'
            },
            {
                'pregunta': '¿Cuál es el antónimo de "grande"?',
                'opciones': ['Pequeño', 'Enorme', 'Gigante', 'Inmenso'],
                'correcta': 'Pequeño'
            },
            {
                'pregunta': '¿Qué palabra es un sustantivo?',
                'opciones': ['Casa', 'Correr', 'Hermoso', 'Rápidamente'],
                'correcta': 'Casa'
            },
            {
                'pregunta': '¿Cuál es el plural de "lápiz"?',
                'opciones': ['Lápices', 'Lapizs', 'Lápizes', 'Lapices'],
                'correcta': 'Lápices'
            }
        ]
        
        if st.session_state.esp_pregunta is None:
            self.generar_pregunta()
    
    def generar_pregunta(self):
        pregunta = random.choice(self.preguntas)
        st.session_state.esp_pregunta = pregunta['pregunta']
        st.session_state.esp_correcta = pregunta['correcta']
        st.session_state.esp_opciones = pregunta['opciones']
        st.session_state.esp_respondido = False
        st.session_state.esp_mensaje = None
    
    def jugar(self):
        st.markdown("## 📚 Español")
        st.caption("Pon a prueba tu conocimiento del idioma")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Puntos en esta partida", st.session_state.esp_puntos)
        
        if st.session_state.esp_mensaje:
            if "✅" in st.session_state.esp_mensaje:
                st.success(st.session_state.esp_mensaje)
            else:
                st.error(st.session_state.esp_mensaje)
        
        st.markdown(f"### {st.session_state.esp_pregunta}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(st.session_state.esp_opciones[0], key="esp_1", use_container_width=True, disabled=st.session_state.esp_respondido):
                if st.session_state.esp_opciones[0] == st.session_state.esp_correcta:
                    st.session_state.esp_puntos += 15
                    st.session_state.esp_mensaje = "✅ ¡Correcto! +15 puntos"
                    st.balloons()
                else:
                    st.session_state.esp_mensaje = f"❌ Incorrecto. La respuesta es: {st.session_state.esp_correcta}"
                st.session_state.esp_respondido = True
                st.rerun()
            
            if st.button(st.session_state.esp_opciones[1], key="esp_2", use_container_width=True, disabled=st.session_state.esp_respondido):
                if st.session_state.esp_opciones[1] == st.session_state.esp_correcta:
                    st.session_state.esp_puntos += 15
                    st.session_state.esp_mensaje = "✅ ¡Correcto! +15 puntos"
                    st.balloons()
                else:
                    st.session_state.esp_mensaje = f"❌ Incorrecto. La respuesta es: {st.session_state.esp_correcta}"
                st.session_state.esp_respondido = True
                st.rerun()
        
        with col2:
            if st.button(st.session_state.esp_opciones[2], key="esp_3", use_container_width=True, disabled=st.session_state.esp_respondido):
                if st.session_state.esp_opciones[2] == st.session_state.esp_correcta:
                    st.session_state.esp_puntos += 15
                    st.session_state.esp_mensaje = "✅ ¡Correcto! +15 puntos"
                    st.balloons()
                else:
                    st.session_state.esp_mensaje = f"❌ Incorrecto. La respuesta es: {st.session_state.esp_correcta}"
                st.session_state.esp_respondido = True
                st.rerun()
            
            if st.button(st.session_state.esp_opciones[3], key="esp_4", use_container_width=True, disabled=st.session_state.esp_respondido):
                if st.session_state.esp_opciones[3] == st.session_state.esp_correcta:
                    st.session_state.esp_puntos += 15
                    st.session_state.esp_mensaje = "✅ ¡Correcto! +15 puntos"
                    st.balloons()
                else:
                    st.session_state.esp_mensaje = f"❌ Incorrecto. La respuesta es: {st.session_state.esp_correcta}"
                st.session_state.esp_respondido = True
                st.rerun()
        
        if st.session_state.esp_respondido:
            if st.button("➡️ Siguiente Pregunta", key="esp_next", use_container_width=True):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.esp_puntos


# ============================================
# JUEGO DE GEOGRAFÍA
# ============================================
class JuegoGeografia:
    def __init__(self):
        if 'geo_puntos' not in st.session_state:
            st.session_state.geo_puntos = 0
        if 'geo_pais' not in st.session_state:
            st.session_state.geo_pais = None
        if 'geo_capital' not in st.session_state:
            st.session_state.geo_capital = None
        if 'geo_opciones' not in st.session_state:
            st.session_state.geo_opciones = []
        if 'geo_respondido' not in st.session_state:
            st.session_state.geo_respondido = False
        if 'geo_mensaje' not in st.session_state:
            st.session_state.geo_mensaje = None
        
        self.capitales = {
            'Francia': 'París',
            'Japón': 'Tokio',
            'Brasil': 'Brasilia',
            'Australia': 'Canberra',
            'Egipto': 'El Cairo',
            'México': 'Ciudad de México',
            'España': 'Madrid',
            'Italia': 'Roma',
            'Reino Unido': 'Londres',
            'Alemania': 'Berlín'
        }
        
        if st.session_state.geo_pais is None:
            self.generar_pregunta()
    
    def generar_pregunta(self):
        pais = random.choice(list(self.capitales.keys()))
        capital = self.capitales[pais]
        
        otras = random.sample([c for p, c in self.capitales.items() if p != pais], 3)
        opciones = [capital] + otras
        random.shuffle(opciones)
        
        st.session_state.geo_pais = pais
        st.session_state.geo_capital = capital
        st.session_state.geo_opciones = opciones
        st.session_state.geo_respondido = False
        st.session_state.geo_mensaje = None
    
    def jugar(self):
        st.markdown("## 🌍 Geografía")
        st.caption("Adivina las capitales del mundo")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Puntos en esta partida", st.session_state.geo_puntos)
        
        if st.session_state.geo_mensaje:
            if "✅" in st.session_state.geo_mensaje:
                st.success(st.session_state.geo_mensaje)
            else:
                st.error(st.session_state.geo_mensaje)
        
        st.markdown(f"### ¿Cuál es la capital de **{st.session_state.geo_pais}**?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(st.session_state.geo_opciones[0], key="geo_1", use_container_width=True, disabled=st.session_state.geo_respondido):
                if st.session_state.geo_opciones[0] == st.session_state.geo_capital:
                    st.session_state.geo_puntos += 20
                    st.session_state.geo_mensaje = "✅ ¡Correcto! +20 puntos"
                    st.balloons()
                else:
                    st.session_state.geo_mensaje = f"❌ Incorrecto. La capital es {st.session_state.geo_capital}"
                st.session_state.geo_respondido = True
                st.rerun()
            
            if st.button(st.session_state.geo_opciones[1], key="geo_2", use_container_width=True, disabled=st.session_state.geo_respondido):
                if st.session_state.geo_opciones[1] == st.session_state.geo_capital:
                    st.session_state.geo_puntos += 20
                    st.session_state.geo_mensaje = "✅ ¡Correcto! +20 puntos"
                    st.balloons()
                else:
                    st.session_state.geo_mensaje = f"❌ Incorrecto. La capital es {st.session_state.geo_capital}"
                st.session_state.geo_respondido = True
                st.rerun()
        
        with col2:
            if st.button(st.session_state.geo_opciones[2], key="geo_3", use_container_width=True, disabled=st.session_state.geo_respondido):
                if st.session_state.geo_opciones[2] == st.session_state.geo_capital:
                    st.session_state.geo_puntos += 20
                    st.session_state.geo_mensaje = "✅ ¡Correcto! +20 puntos"
                    st.balloons()
                else:
                    st.session_state.geo_mensaje = f"❌ Incorrecto. La capital es {st.session_state.geo_capital}"
                st.session_state.geo_respondido = True
                st.rerun()
            
            if st.button(st.session_state.geo_opciones[3], key="geo_4", use_container_width=True, disabled=st.session_state.geo_respondido):
                if st.session_state.geo_opciones[3] == st.session_state.geo_capital:
                    st.session_state.geo_puntos += 20
                    st.session_state.geo_mensaje = "✅ ¡Correcto! +20 puntos"
                    st.balloons()
                else:
                    st.session_state.geo_mensaje = f"❌ Incorrecto. La capital es {st.session_state.geo_capital}"
                st.session_state.geo_respondido = True
                st.rerun()
        
        if st.session_state.geo_respondido:
            if st.button("➡️ Siguiente País", key="geo_next", use_container_width=True):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.geo_puntos


# ============================================
# JUEGO DE FILOSOFÍA
# ============================================
class JuegoFilosofia:
    def __init__(self):
        if 'fil_puntos' not in st.session_state:
            st.session_state.fil_puntos = 0
        if 'fil_pregunta' not in st.session_state:
            st.session_state.fil_pregunta = None
        if 'fil_correcta' not in st.session_state:
            st.session_state.fil_correcta = None
        if 'fil_opciones' not in st.session_state:
            st.session_state.fil_opciones = []
        if 'fil_respondido' not in st.session_state:
            st.session_state.fil_respondido = False
        if 'fil_mensaje' not in st.session_state:
            st.session_state.fil_mensaje = None
        
        self.preguntas = [
            {
                'pregunta': '¿Quién fue el maestro de Platón?',
                'opciones': ['Sócrates', 'Aristóteles', 'Pitágoras', 'Heráclito'],
                'correcta': 'Sócrates'
            },
            {
                'pregunta': '¿Qué significa "filosofía"?',
                'opciones': ['Amor a la sabiduría', 'Estudio de la naturaleza', 'Ciencia del ser', 'Pensamiento lógico'],
                'correcta': 'Amor a la sabiduría'
            },
            {
                'pregunta': '¿Quién escribió "La República"?',
                'opciones': ['Platón', 'Aristóteles', 'Sócrates', 'Descartes'],
                'correcta': 'Platón'
            },
            {
                'pregunta': '¿Qué frase dijo Descartes?',
                'opciones': ['Pienso, luego existo', 'Solo sé que nada sé', 'El hombre es la medida', 'Dios ha muerto'],
                'correcta': 'Pienso, luego existo'
            }
        ]
        
        if st.session_state.fil_pregunta is None:
            self.generar_pregunta()
    
    def generar_pregunta(self):
        pregunta = random.choice(self.preguntas)
        st.session_state.fil_pregunta = pregunta['pregunta']
        st.session_state.fil_correcta = pregunta['correcta']
        st.session_state.fil_opciones = pregunta['opciones']
        st.session_state.fil_respondido = False
        st.session_state.fil_mensaje = None
    
    def jugar(self):
        st.markdown("## 🤔 Filosofía")
        st.caption("Explora el mundo de las ideas")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Puntos en esta partida", st.session_state.fil_puntos)
        
        if st.session_state.fil_mensaje:
            if "✅" in st.session_state.fil_mensaje:
                st.success(st.session_state.fil_mensaje)
            else:
                st.error(st.session_state.fil_mensaje)
        
        st.markdown(f"### {st.session_state.fil_pregunta}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(st.session_state.fil_opciones[0], key="fil_1", use_container_width=True, disabled=st.session_state.fil_respondido):
                if st.session_state.fil_opciones[0] == st.session_state.fil_correcta:
                    st.session_state.fil_puntos += 25
                    st.session_state.fil_mensaje = "✅ ¡Correcto! +25 puntos"
                    st.balloons()
                else:
                    st.session_state.fil_mensaje = f"❌ Incorrecto. La respuesta es: {st.session_state.fil_correcta}"
                st.session_state.fil_respondido = True
                st.rerun()
            
            if st.button(st.session_state.fil_opciones[1], key="fil_2", use_container_width=True, disabled=st.session_state.fil_respondido):
                if st.session_state.fil_opciones[1] == st.session_state.fil_correcta:
                    st.session_state.fil_puntos += 25
                    st.session_state.fil_mensaje = "✅ ¡Correcto! +25 puntos"
                    st.balloons()
                else:
                    st.session_state.fil_mensaje = f"❌ Incorrecto. La respuesta es: {st.session_state.fil_correcta}"
                st.session_state.fil_respondido = True
                st.rerun()
        
        with col2:
            if st.button(st.session_state.fil_opciones[2], key="fil_3", use_container_width=True, disabled=st.session_state.fil_respondido):
                if st.session_state.fil_opciones[2] == st.session_state.fil_correcta:
                    st.session_state.fil_puntos += 25
                    st.session_state.fil_mensaje = "✅ ¡Correcto! +25 puntos"
                    st.balloons()
                else:
                    st.session_state.fil_mensaje = f"❌ Incorrecto. La respuesta es: {st.session_state.fil_correcta}"
                st.session_state.fil_respondido = True
                st.rerun()
            
            if st.button(st.session_state.fil_opciones[3], key="fil_4", use_container_width=True, disabled=st.session_state.fil_respondido):
                if st.session_state.fil_opciones[3] == st.session_state.fil_correcta:
                    st.session_state.fil_puntos += 25
                    st.session_state.fil_mensaje = "✅ ¡Correcto! +25 puntos"
                    st.balloons()
                else:
                    st.session_state.fil_mensaje = f"❌ Incorrecto. La respuesta es: {st.session_state.fil_correcta}"
                st.session_state.fil_respondido = True
                st.rerun()
        
        if st.session_state.fil_respondido:
            if st.button("➡️ Siguiente Pregunta", key="fil_next", use_container_width=True):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.fil_puntos
