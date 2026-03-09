"""Juegos educativos para EduPlay"""
import streamlit as st
import random

# ============================================
# JUEGO DE MATEMÁTICAS (VERSIÓN SIMPLE Y FUNCIONAL)
# ============================================
class JuegoMatematicas:
    def __init__(self):
        # Inicializar variables de sesión
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
            num2 = random.randint(1, num1)  # num2 siempre menor o igual a num1
            resultado = num1 - num2
        
        else:  # multiplicación
            num1 = random.randint(2, 10)
            num2 = random.randint(2, 10)
            resultado = num1 * num2
        
        # Guardar en sesión
        st.session_state.math_num1 = num1
        st.session_state.math_num2 = num2
        st.session_state.math_operador = operador
        st.session_state.math_resultado = resultado
        
        # Generar opciones (1 correcta + 3 incorrectas)
        opciones = [resultado]
        while len(opciones) < 4:
            # Generar opción incorrecta cercana al resultado
            if operador == '+' or operador == '-':
                incorrecta = resultado + random.randint(-3, 3)
            else:  # multiplicación
                incorrecta = resultado + random.randint(-5, 5)
            
            if incorrecta not in opciones and incorrecta > 0:
                opciones.append(incorrecta)
        
        random.shuffle(opciones)
        st.session_state.math_opciones = opciones
        st.session_state.math_respondido = False
    
    def jugar(self):
        st.markdown("### 🧮 Matemáticas Rápidas")
        st.caption("Pon a prueba tu agilidad mental con operaciones básicas")
        
        # Mostrar puntos
        st.metric("Puntos en esta partida", st.session_state.math_puntos)
        
        # Generar primera pregunta si no existe
        if st.session_state.math_num1 is None:
            self.generar_pregunta()
        
        # Mostrar la pregunta
        num1 = st.session_state.math_num1
        num2 = st.session_state.math_num2
        operador = st.session_state.math_operador
        
        # Usar st.write para asegurar formato correcto
        st.markdown(f"## **{num1} {operador} {num2} = ?**")
        
        # Mostrar opciones en 2 columnas
        col1, col2 = st.columns(2)
        
        # Opción 1
        with col1:
            if st.button(
                f"**{st.session_state.math_opciones[0]}**", 
                key="math_opt1",
                use_container_width=True,
                disabled=st.session_state.math_respondido
            ):
                if st.session_state.math_opciones[0] == st.session_state.math_resultado:
                    st.session_state.math_puntos += 10
                    st.success("✅ ¡Correcto! +10 puntos")
                else:
                    st.error(f"❌ Incorrecto. La respuesta era {st.session_state.math_resultado}")
                st.session_state.math_respondido = True
                st.rerun()
        
        # Opción 2
        with col2:
            if st.button(
                f"**{st.session_state.math_opciones[1]}**", 
                key="math_opt2",
                use_container_width=True,
                disabled=st.session_state.math_respondido
            ):
                if st.session_state.math_opciones[1] == st.session_state.math_resultado:
                    st.session_state.math_puntos += 10
                    st.success("✅ ¡Correcto! +10 puntos")
                else:
                    st.error(f"❌ Incorrecto. La respuesta era {st.session_state.math_resultado}")
                st.session_state.math_respondido = True
                st.rerun()
        
        col3, col4 = st.columns(2)
        
        # Opción 3
        with col3:
            if st.button(
                f"**{st.session_state.math_opciones[2]}**", 
                key="math_opt3",
                use_container_width=True,
                disabled=st.session_state.math_respondido
            ):
                if st.session_state.math_opciones[2] == st.session_state.math_resultado:
                    st.session_state.math_puntos += 10
                    st.success("✅ ¡Correcto! +10 puntos")
                else:
                    st.error(f"❌ Incorrecto. La respuesta era {st.session_state.math_resultado}")
                st.session_state.math_respondido = True
                st.rerun()
        
        # Opción 4
        with col4:
            if st.button(
                f"**{st.session_state.math_opciones[3]}**", 
                key="math_opt4",
                use_container_width=True,
                disabled=st.session_state.math_respondido
            ):
                if st.session_state.math_opciones[3] == st.session_state.math_resultado:
                    st.session_state.math_puntos += 10
                    st.success("✅ ¡Correcto! +10 puntos")
                else:
                    st.error(f"❌ Incorrecto. La respuesta era {st.session_state.math_resultado}")
                st.session_state.math_respondido = True
                st.rerun()
        
        # Botón para siguiente pregunta (solo aparece después de responder)
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
                'pregunta': '¿Qué es un sustantivo?',
                'opciones': [
                    'Palabra que nombra personas, animales o cosas',
                    'Palabra que expresa acciones',
                    'Palabra que describe cualidades',
                    'Palabra que une oraciones'
                ],
                'correcta': 'Palabra que nombra personas, animales o cosas'
            }
        ]
        
        if 'esp_puntos' not in st.session_state:
            st.session_state.esp_puntos = 0
        if 'esp_pregunta_actual' not in st.session_state:
            st.session_state.esp_pregunta_actual = None
        if 'esp_correcta' not in st.session_state:
            st.session_state.esp_correcta = None
        if 'esp_opciones' not in st.session_state:
            st.session_state.esp_opciones = []
        if 'esp_respondido' not in st.session_state:
            st.session_state.esp_respondido = False
    
    def generar_pregunta(self):
        pregunta = random.choice(self.preguntas)
        st.session_state.esp_pregunta_actual = pregunta['pregunta']
        st.session_state.esp_correcta = pregunta['correcta']
        st.session_state.esp_opciones = pregunta['opciones']
        st.session_state.esp_respondido = False
    
    def jugar(self):
        st.markdown("### 📚 Español")
        
        st.metric("Puntos", st.session_state.esp_puntos)
        
        if st.session_state.esp_pregunta_actual is None:
            self.generar_pregunta()
        
        st.markdown(f"### {st.session_state.esp_pregunta_actual}")
        
        col1, col2 = st.columns(2)
        
        for i, opcion in enumerate(st.session_state.esp_opciones):
            with col1 if i < 2 else col2:
                if st.button(
                    opcion, 
                    key=f"esp_{i}",
                    use_container_width=True,
                    disabled=st.session_state.esp_respondido
                ):
                    if opcion == st.session_state.esp_correcta:
                        st.session_state.esp_puntos += 15
                        st.success("✅ ¡Correcto! +15 puntos")
                    else:
                        st.error(f"❌ Incorrecto. La respuesta es: {st.session_state.esp_correcta}")
                    st.session_state.esp_respondido = True
                    st.rerun()
        
        if st.session_state.esp_respondido:
            if st.button("➡️ Siguiente Pregunta", key="esp_next"):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.esp_puntos


# ============================================
# JUEGO DE GEOGRAFÍA
# ============================================
class JuegoGeografia:
    def __init__(self):
        self.capitales = {
            'Francia': 'París',
            'Japón': 'Tokio',
            'Brasil': 'Brasilia',
            'Australia': 'Canberra',
            'Egipto': 'El Cairo',
            'México': 'Ciudad de México',
            'España': 'Madrid',
            'Italia': 'Roma'
        }
        
        if 'geo_puntos' not in st.session_state:
            st.session_state.geo_puntos = 0
        if 'geo_pais_actual' not in st.session_state:
            st.session_state.geo_pais_actual = None
        if 'geo_capital_correcta' not in st.session_state:
            st.session_state.geo_capital_correcta = None
        if 'geo_opciones' not in st.session_state:
            st.session_state.geo_opciones = []
        if 'geo_respondido' not in st.session_state:
            st.session_state.geo_respondido = False
    
    def generar_pregunta(self):
        pais = random.choice(list(self.capitales.keys()))
        capital_correcta = self.capitales[pais]
        
        otras = random.sample([c for p, c in self.capitales.items() if p != pais], 3)
        opciones = [capital_correcta] + otras
        random.shuffle(opciones)
        
        st.session_state.geo_pais_actual = pais
        st.session_state.geo_capital_correcta = capital_correcta
        st.session_state.geo_opciones = opciones
        st.session_state.geo_respondido = False
    
    def jugar(self):
        st.markdown("### 🌍 Geografía")
        
        st.metric("Puntos", st.session_state.geo_puntos)
        
        if st.session_state.geo_pais_actual is None:
            self.generar_pregunta()
        
        st.markdown(f"### ¿Cuál es la capital de **{st.session_state.geo_pais_actual}**?")
        
        col1, col2 = st.columns(2)
        
        for i, opcion in enumerate(st.session_state.geo_opciones):
            with col1 if i < 2 else col2:
                if st.button(
                    opcion, 
                    key=f"geo_{i}",
                    use_container_width=True,
                    disabled=st.session_state.geo_respondido
                ):
                    if opcion == st.session_state.geo_capital_correcta:
                        st.session_state.geo_puntos += 20
                        st.success("✅ ¡Correcto! +20 puntos")
                    else:
                        st.error(f"❌ Incorrecto. La capital es {st.session_state.geo_capital_correcta}")
                    st.session_state.geo_respondido = True
                    st.rerun()
        
        if st.session_state.geo_respondido:
            if st.button("➡️ Siguiente País", key="geo_next"):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.geo_puntos


# ============================================
# JUEGO DE FILOSOFÍA
# ============================================
class JuegoFilosofia:
    def __init__(self):
        self.preguntas = [
            {
                'pregunta': '¿Quién fue el maestro de Platón?',
                'opciones': ['Sócrates', 'Aristóteles', 'Pitágoras', 'Heráclito'],
                'correcta': 'Sócrates'
            },
            {
                'pregunta': '¿Qué significa la palabra "filosofía"?',
                'opciones': ['Amor a la sabiduría', 'Estudio de la naturaleza', 'Ciencia del ser', 'Pensamiento lógico'],
                'correcta': 'Amor a la sabiduría'
            },
            {
                'pregunta': '¿Quién escribió "La República"?',
                'opciones': ['Platón', 'Aristóteles', 'Sócrates', 'Descartes'],
                'correcta': 'Platón'
            }
        ]
        
        if 'fil_puntos' not in st.session_state:
            st.session_state.fil_puntos = 0
        if 'fil_pregunta_actual' not in st.session_state:
            st.session_state.fil_pregunta_actual = None
        if 'fil_correcta' not in st.session_state:
            st.session_state.fil_correcta = None
        if 'fil_opciones' not in st.session_state:
            st.session_state.fil_opciones = []
        if 'fil_respondido' not in st.session_state:
            st.session_state.fil_respondido = False
    
    def generar_pregunta(self):
        pregunta = random.choice(self.preguntas)
        st.session_state.fil_pregunta_actual = pregunta['pregunta']
        st.session_state.fil_correcta = pregunta['correcta']
        st.session_state.fil_opciones = pregunta['opciones']
        st.session_state.fil_respondido = False
    
    def jugar(self):
        st.markdown("### 🤔 Filosofía")
        
        st.metric("Puntos", st.session_state.fil_puntos)
        
        if st.session_state.fil_pregunta_actual is None:
            self.generar_pregunta()
        
        st.markdown(f"### {st.session_state.fil_pregunta_actual}")
        
        col1, col2 = st.columns(2)
        
        for i, opcion in enumerate(st.session_state.fil_opciones):
            with col1 if i < 2 else col2:
                if st.button(
                    opcion, 
                    key=f"fil_{i}",
                    use_container_width=True,
                    disabled=st.session_state.fil_respondido
                ):
                    if opcion == st.session_state.fil_correcta:
                        st.session_state.fil_puntos += 25
                        st.success("✅ ¡Correcto! +25 puntos")
                    else:
                        st.error(f"❌ Incorrecto. La respuesta es: {st.session_state.fil_correcta}")
                    st.session_state.fil_respondido = True
                    st.rerun()
        
        if st.session_state.fil_respondido:
            if st.button("➡️ Siguiente Pregunta", key="fil_next"):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.fil_puntos
