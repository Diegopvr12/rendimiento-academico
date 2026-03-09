"""Juegos educativos para EduPlay"""
import streamlit as st
import random
import time

# ============================================
# JUEGO DE MATEMÁTICAS
# ============================================
class JuegoMatematicas:
    def __init__(self):
        if 'math_puntos' not in st.session_state:
            st.session_state.math_puntos = 0
        if 'math_preguntas' not in st.session_state:
            st.session_state.math_preguntas = 0
        if 'math_aciertos' not in st.session_state:
            st.session_state.math_aciertos = 0
        if 'math_pregunta_actual' not in st.session_state:
            st.session_state.math_pregunta_actual = None
        if 'math_respuesta_correcta' not in st.session_state:
            st.session_state.math_respuesta_correcta = None
        if 'math_opciones' not in st.session_state:
            st.session_state.math_opciones = []
        if 'math_respondido' not in st.session_state:
            st.session_state.math_respondido = False
    
    def generar_pregunta(self):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        op = random.choice(['+', '-', '×'])
        
        if op == '+':
            resultado = num1 + num2
        elif op == '-':
            num1, num2 = max(num1, num2), min(num1, num2)
            resultado = num1 - num2
        else:
            resultado = num1 * num2
        
        opciones = [resultado]
        while len(opciones) < 4:
            op = resultado + random.randint(-5, 5)
            if op not in opciones and op > 0:
                opciones.append(op)
        
        random.shuffle(opciones)
        
        st.session_state.math_pregunta_actual = f"{num1} {op} {num2}"
        st.session_state.math_respuesta_correcta = resultado
        st.session_state.math_opciones = opciones
        st.session_state.math_respondido = False
    
    def jugar(self):
        st.markdown("### 🧮 Matemáticas Rápidas")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Puntos", st.session_state.math_puntos)
        with col2:
            if st.session_state.math_preguntas > 0:
                precision = (st.session_state.math_aciertos / st.session_state.math_preguntas) * 100
                st.metric("Precisión", f"{precision:.0f}%")
        
        if st.session_state.math_pregunta_actual is None:
            self.generar_pregunta()
        
        st.markdown(f"## **{st.session_state.math_pregunta_actual} = ?**")
        
        cols = st.columns(2)
        for i, opcion in enumerate(st.session_state.math_opciones):
            with cols[i % 2]:
                disabled = st.session_state.math_respondido
                if st.button(
                    f"**{opcion}**", 
                    key=f"math_{i}_{random.randint(1,1000)}", 
                    use_container_width=True,
                    disabled=disabled
                ):
                    st.session_state.math_preguntas += 1
                    if opcion == st.session_state.math_respuesta_correcta:
                        st.session_state.math_puntos += 10
                        st.session_state.math_aciertos += 1
                        st.session_state.math_respondido = True
                        st.balloons()
                        st.success("✅ ¡Correcto! +10 puntos")
                    else:
                        st.session_state.math_respondido = True
                        st.error(f"❌ Incorrecto. La respuesta era {st.session_state.math_respuesta_correcta}")
        
        if st.session_state.math_respondido:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("➡️ Siguiente", use_container_width=True):
                    self.generar_pregunta()
                    st.rerun()
        
        return st.session_state.math_puntos

# ============================================
# JUEGO DE VOCABULARIO (ESPAÑOL)
# ============================================
class JuegoEspanol:
    def __init__(self):
        self.preguntas = [
            {
                'pregunta': '¿Cuál es el sinónimo de "alegría"?',
                'opciones': ['Felicidad', 'Tristeza', 'Enojo', 'Miedo'],
                'correcta': 'Felicidad',
                'explicacion': 'Alegría y felicidad son sinónimos'
            },
            {
                'pregunta': '¿Cuál es el antónimo de "grande"?',
                'opciones': ['Pequeño', 'Enorme', 'Gigante', 'Inmenso'],
                'correcta': 'Pequeño',
                'explicacion': 'Grande y pequeño son antónimos'
            },
            {
                'pregunta': '¿Qué es un sustantivo?',
                'opciones': [
                    'Palabra que nombra personas, animales o cosas',
                    'Palabra que expresa acciones',
                    'Palabra que describe cualidades',
                    'Palabra que une oraciones'
                ],
                'correcta': 'Palabra que nombra personas, animales o cosas',
                'explicacion': 'Los sustantivos sirven para nombrar'
            },
            {
                'pregunta': '¿Cuál es el plural de "lápiz"?',
                'opciones': ['Lápices', 'Lapizs', 'Lápizes', 'Lapices'],
                'correcta': 'Lápices',
                'explicacion': 'Las palabras terminadas en Z cambian a CES'
            },
            {
                'pregunta': '¿Qué palabra está bien escrita?',
                'opciones': ['Baca', 'Vaca', 'Baka', 'Vaka'],
                'correcta': 'Vaca',
                'explicacion': 'Vaca es el animal, baca es el portaequipajes'
            },
            {
                'pregunta': '¿Qué es un verbo?',
                'opciones': [
                    'Acción o estado',
                    'Nombre de persona',
                    'Cualidad',
                    'Lugar'
                ],
                'correcta': 'Acción o estado',
                'explicacion': 'Los verbos expresan acciones (correr, saltar) o estados (ser, estar)'
            },
            {
                'pregunta': '¿Cuál es el sujeto de la oración: "Juan come manzanas"?',
                'opciones': ['Juan', 'come', 'manzanas', 'Juan come'],
                'correcta': 'Juan',
                'explicacion': 'El sujeto es quien realiza la acción'
            },
            {
                'pregunta': '¿Qué palabra es un adjetivo?',
                'opciones': ['Hermoso', 'Correr', 'Casa', 'Rápidamente'],
                'correcta': 'Hermoso',
                'explicacion': 'Los adjetivos describen cualidades'
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
        if 'esp_explicacion' not in st.session_state:
            st.session_state.esp_explicacion = None
        if 'esp_respondido' not in st.session_state:
            st.session_state.esp_respondido = False
        if 'esp_mensaje' not in st.session_state:
            st.session_state.esp_mensaje = None
    
    def generar_pregunta(self):
        pregunta = random.choice(self.preguntas)
        
        st.session_state.esp_pregunta_actual = pregunta['pregunta']
        st.session_state.esp_correcta = pregunta['correcta']
        st.session_state.esp_opciones = pregunta['opciones']
        st.session_state.esp_explicacion = pregunta['explicacion']
        st.session_state.esp_respondido = False
        st.session_state.esp_mensaje = None
    
    def jugar(self):
        st.markdown("### 📚 Español - Lengua y Literatura")
        
        st.metric("Puntos", st.session_state.esp_puntos)
        
        if st.session_state.esp_pregunta_actual is None:
            self.generar_pregunta()
        
        st.markdown(f"### **{st.session_state.esp_pregunta_actual}**")
        
        if st.session_state.esp_mensaje:
            if "✅" in st.session_state.esp_mensaje:
                st.success(st.session_state.esp_mensaje)
                st.info(f"📖 {st.session_state.esp_explicacion}")
            else:
                st.error(st.session_state.esp_mensaje)
                st.info(f"📖 {st.session_state.esp_explicacion}")
        
        cols = st.columns(2)
        for i, opcion in enumerate(st.session_state.esp_opciones):
            with cols[i % 2]:
                disabled = st.session_state.esp_respondido
                if st.button(
                    opcion, 
                    key=f"esp_{i}_{random.randint(1,1000)}", 
                    use_container_width=True,
                    disabled=disabled
                ):
                    if opcion == st.session_state.esp_correcta:
                        st.session_state.esp_puntos += 15
                        st.session_state.esp_respondido = True
                        st.session_state.esp_mensaje = "✅ ¡Correcto! +15 puntos"
                        st.balloons()
                    else:
                        st.session_state.esp_respondido = True
                        st.session_state.esp_mensaje = f"❌ Incorrecto. La respuesta correcta es: {st.session_state.esp_correcta}"
                    st.rerun()
        
        if st.session_state.esp_respondido:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("➡️ Siguiente Pregunta", use_container_width=True):
                    self.generar_pregunta()
                    st.rerun()
        
        return st.session_state.esp_puntos

# ============================================
# JUEGO DE FILOSOFÍA
# ============================================
class JuegoFilosofia:
    def __init__(self):
        self.preguntas = [
            {
                'pregunta': '¿Quién fue el maestro de Platón?',
                'opciones': ['Sócrates', 'Aristóteles', 'Pitágoras', 'Heráclito'],
                'correcta': 'Sócrates',
                'explicacion': 'Sócrates fue el maestro de Platón, quien a su vez fue maestro de Aristóteles'
            },
            {
                'pregunta': '¿Qué significa la palabra "filosofía"?',
                'opciones': ['Amor a la sabiduría', 'Estudio de la naturaleza', 'Ciencia del ser', 'Pensamiento lógico'],
                'correcta': 'Amor a la sabiduría',
                'explicacion': 'Filosofía viene del griego: philos (amor) y sophia (sabiduría)'
            },
            {
                'pregunta': '¿Quién escribió "La República"?',
                'opciones': ['Platón', 'Aristóteles', 'Sócrates', 'Descartes'],
                'correcta': 'Platón',
                'explicacion': '"La República" es uno de los diálogos más famosos de Platón'
            },
            {
                'pregunta': '¿Qué famosa frase dijo Descartes?',
                'opciones': [
                    'Pienso, luego existo',
                    'Solo sé que nada sé',
                    'El hombre es la medida de todas las cosas',
                    'Dios ha muerto'
                ],
                'correcta': 'Pienso, luego existo',
                'explicacion': '"Cogito, ergo sum" es la frase fundamental de Descartes'
            },
            {
                'pregunta': '¿Quién es considerado el padre de la filosofía occidental?',
                'opciones': ['Tales de Mileto', 'Sócrates', 'Platón', 'Aristóteles'],
                'correcta': 'Tales de Mileto',
                'explicacion': 'Tales fue el primer filósofo reconocido de la historia'
            },
            {
                'pregunta': '¿Qué corriente filosófica fundó Epicuro?',
                'opciones': ['Epicureísmo', 'Estoicismo', 'Cinicismo', 'Escepticismo'],
                'correcta': 'Epicureísmo',
                'explicacion': 'El epicureísmo busca la felicidad a través del placer moderado'
            },
            {
                'pregunta': '¿Qué filósofo dijo "Solo sé que nada sé"?',
                'opciones': ['Sócrates', 'Platón', 'Aristóteles', 'Pitágoras'],
                'correcta': 'Sócrates',
                'explicacion': 'Esta frase refleja la humildad intelectual de Sócrates'
            },
            {
                'pregunta': '¿Quién escribió "Así habló Zaratustra"?',
                'opciones': ['Nietzsche', 'Kant', 'Hegel', 'Schopenhauer'],
                'correcta': 'Nietzsche',
                'explicacion': 'Nietzsche escribió esta obra sobre el superhombre'
            },
            {
                'pregunta': '¿Qué es el "imperativo categórico" en Kant?',
                'opciones': [
                    'Una regla moral universal',
                    'Una ley física',
                    'Un tipo de gobierno',
                    'Una teoría del conocimiento'
                ],
                'correcta': 'Una regla moral universal',
                'explicacion': 'El imperativo categórico es la base de la ética kantiana'
            },
            {
                'pregunta': '¿Qué filósofo escribió "El contrato social"?',
                'opciones': ['Rousseau', 'Voltaire', 'Montesquieu', 'Hobbes'],
                'correcta': 'Rousseau',
                'explicacion': 'Rousseau propuso que la sociedad debe basarse en un contrato entre ciudadanos'
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
        if 'fil_explicacion' not in st.session_state:
            st.session_state.fil_explicacion = None
        if 'fil_respondido' not in st.session_state:
            st.session_state.fil_respondido = False
        if 'fil_mensaje' not in st.session_state:
            st.session_state.fil_mensaje = None
    
    def generar_pregunta(self):
        pregunta = random.choice(self.preguntas)
        
        st.session_state.fil_pregunta_actual = pregunta['pregunta']
        st.session_state.fil_correcta = pregunta['correcta']
        st.session_state.fil_opciones = pregunta['opciones']
        st.session_state.fil_explicacion = pregunta['explicacion']
        st.session_state.fil_respondido = False
        st.session_state.fil_mensaje = None
    
    def jugar(self):
        st.markdown("### 🤔 Filosofía")
        
        st.metric("Puntos", st.session_state.fil_puntos)
        
        if st.session_state.fil_pregunta_actual is None:
            self.generar_pregunta()
        
        st.markdown(f"### **{st.session_state.fil_pregunta_actual}**")
        
        if st.session_state.fil_mensaje:
            if "✅" in st.session_state.fil_mensaje:
                st.success(st.session_state.fil_mensaje)
                st.info(f"📖 {st.session_state.fil_explicacion}")
            else:
                st.error(st.session_state.fil_mensaje)
                st.info(f"📖 {st.session_state.fil_explicacion}")
        
        cols = st.columns(2)
        for i, opcion in enumerate(st.session_state.fil_opciones):
            with cols[i % 2]:
                disabled = st.session_state.fil_respondido
                if st.button(
                    opcion, 
                    key=f"fil_{i}_{random.randint(1,1000)}", 
                    use_container_width=True,
                    disabled=disabled
                ):
                    if opcion == st.session_state.fil_correcta:
                        st.session_state.fil_puntos += 25
                        st.session_state.fil_respondido = True
                        st.session_state.fil_mensaje = "✅ ¡Correcto! +25 puntos"
                        st.balloons()
                    else:
                        st.session_state.fil_respondido = True
                        st.session_state.fil_mensaje = f"❌ Incorrecto. La respuesta correcta es: {st.session_state.fil_correcta}"
                    st.rerun()
        
        if st.session_state.fil_respondido:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("➡️ Siguiente Pregunta", use_container_width=True):
                    self.generar_pregunta()
                    st.rerun()
        
        return st.session_state.fil_puntos

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
            'Italia': 'Roma',
            'Reino Unido': 'Londres',
            'Alemania': 'Berlín',
            'Rusia': 'Moscú',
            'China': 'Pekín',
            'India': 'Nueva Delhi',
            'Canadá': 'Ottawa',
            'Argentina': 'Buenos Aires',
            'Colombia': 'Bogotá',
            'Perú': 'Lima',
            'Chile': 'Santiago',
            'Venezuela': 'Caracas',
            'Uruguay': 'Montevideo'
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
        if 'geo_mensaje' not in st.session_state:
            st.session_state.geo_mensaje = None
    
    def generar_pregunta(self):
        pais = random.choice(list(self.capitales.keys()))
        capital_correcta = self.capitales[pais]
        
        otras_capitales = random.sample(
            [c for p, c in self.capitales.items() if p != pais], 
            3
        )
        
        opciones = [capital_correcta] + otras_capitales
        random.shuffle(opciones)
        
        st.session_state.geo_pais_actual = pais
        st.session_state.geo_capital_correcta = capital_correcta
        st.session_state.geo_opciones = opciones
        st.session_state.geo_respondido = False
        st.session_state.geo_mensaje = None
    
    def jugar(self):
        st.markdown("### 🌍 Geografía Mundial")
        
        st.metric("Puntos", st.session_state.geo_puntos)
        
        if st.session_state.geo_pais_actual is None:
            self.generar_pregunta()
        
        st.markdown(f"### **¿Cuál es la capital de...**")
        st.markdown(f"## **{st.session_state.geo_pais_actual}**")
        
        if st.session_state.geo_mensaje:
            if "✅" in st.session_state.geo_mensaje:
                st.success(st.session_state.geo_mensaje)
            else:
                st.error(st.session_state.geo_mensaje)
        
        cols = st.columns(2)
        for i, opcion in enumerate(st.session_state.geo_opciones):
            with cols[i % 2]:
                disabled = st.session_state.geo_respondido
                if st.button(
                    opcion, 
                    key=f"geo_{i}_{st.session_state.geo_pais_actual}", 
                    use_container_width=True,
                    disabled=disabled
                ):
                    if opcion == st.session_state.geo_capital_correcta:
                        st.session_state.geo_puntos += 20
                        st.session_state.geo_respondido = True
                        st.session_state.geo_mensaje = "✅ ¡Correcto! +20 puntos"
                        st.balloons()
                    else:
                        st.session_state.geo_respondido = True
                        st.session_state.geo_mensaje = f"❌ Incorrecto. La capital de {st.session_state.geo_pais_actual} es {st.session_state.geo_capital_correcta}"
                    st.rerun()
        
        if st.session_state.geo_respondido:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("➡️ Siguiente País", use_container_width=True):
                    self.generar_pregunta()
                    st.rerun()
        
        return st.session_state.geo_puntos

# ============================================
# JUEGO DE VOCABULARIO ORIGINAL (lo dejamos por compatibilidad)
# ============================================
class JuegoVocabulario(JuegoEspanol):
    """Alias de JuegoEspanol para mantener compatibilidad"""
    pass
