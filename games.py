"""Juegos educativos para EduPlay"""
import streamlit as st
import random
import time

class JuegoMatematicas:
    def __init__(self):
        # Inicializar variables de sesión para este juego
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
        """Genera una nueva pregunta matemática"""
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        op = random.choice(['+', '-', '×'])
        
        if op == '+':
            resultado = num1 + num2
        elif op == '-':
            num1, num2 = max(num1, num2), min(num1, num2)
            resultado = num1 - num2
        else:  # ×
            resultado = num1 * num2
        
        # Generar opciones
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
        
        # Mostrar puntos actuales
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Puntos", st.session_state.math_puntos)
        with col2:
            if st.session_state.math_preguntas > 0:
                precision = (st.session_state.math_aciertos / st.session_state.math_preguntas) * 100
                st.metric("Precisión", f"{precision:.0f}%")
        
        # Generar primera pregunta si no existe
        if st.session_state.math_pregunta_actual is None:
            self.generar_pregunta()
        
        # Mostrar pregunta
        st.markdown(f"## **{st.session_state.math_pregunta_actual} = ?**")
        
        # Mostrar opciones
        cols = st.columns(2)
        for i, opcion in enumerate(st.session_state.math_opciones):
            with cols[i % 2]:
                # Deshabilitar botones si ya respondió
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
        
        # Botón para siguiente pregunta
        if st.session_state.math_respondido:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("➡️ Siguiente", use_container_width=True):
                    self.generar_pregunta()
                    st.rerun()
        
        return st.session_state.math_puntos

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
        
        # Inicializar variables de sesión
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
        """Genera una nueva pregunta de geografía"""
        pais = random.choice(list(self.capitales.keys()))
        capital_correcta = self.capitales[pais]
        
        # Obtener otras capitales aleatorias
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
        
        # Mostrar puntos
        st.metric("Puntos", st.session_state.geo_puntos)
        
        # Generar primera pregunta si no existe
        if st.session_state.geo_pais_actual is None:
            self.generar_pregunta()
        
        # Mostrar pregunta
        st.markdown(f"### **¿Cuál es la capital de...**")
        st.markdown(f"## **{st.session_state.geo_pais_actual}**")
        
        # Mostrar mensaje si existe
        if st.session_state.geo_mensaje:
            if "✅" in st.session_state.geo_mensaje:
                st.success(st.session_state.geo_mensaje)
            else:
                st.error(st.session_state.geo_mensaje)
        
        # Mostrar opciones
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
        
        # Botón para siguiente pregunta
        if st.session_state.geo_respondido:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("➡️ Siguiente País", use_container_width=True):
                    self.generar_pregunta()
                    st.rerun()
        
        return st.session_state.geo_puntos

class JuegoVocabulario:
    def __init__(self):
        self.palabras = {
            'efímero': 'Que dura poco tiempo',
            'magnánimo': 'Que tiene grandeza de espíritu',
            'paradójico': 'Que contiene una paradoja',
            'sutil': 'Delicado, agudo',
            'inefable': 'Que no se puede explicar',
            'egregio': 'Insigne, excelente',
            'frugal': 'Moderado en comer y beber',
            'loable': 'Digno de alabanza'
        }
        
        # Inicializar variables de sesión
        if 'voc_puntos' not in st.session_state:
            st.session_state.voc_puntos = 0
        if 'voc_palabra_actual' not in st.session_state:
            st.session_state.voc_palabra_actual = None
        if 'voc_definicion_correcta' not in st.session_state:
            st.session_state.voc_definicion_correcta = None
        if 'voc_opciones' not in st.session_state:
            st.session_state.voc_opciones = []
        if 'voc_respondido' not in st.session_state:
            st.session_state.voc_respondido = False
        if 'voc_mensaje' not in st.session_state:
            st.session_state.voc_mensaje = None
    
    def generar_pregunta(self):
        """Genera una nueva pregunta de vocabulario"""
        palabra = random.choice(list(self.palabras.keys()))
        definicion = self.palabras[palabra]
        
        # Obtener otras definiciones
        otras_def = random.sample(
            [d for p, d in self.palabras.items() if p != palabra], 
            3
        )
        
        opciones = [definicion] + otras_def
        random.shuffle(opciones)
        
        st.session_state.voc_palabra_actual = palabra
        st.session_state.voc_definicion_correcta = definicion
        st.session_state.voc_opciones = opciones
        st.session_state.voc_respondido = False
        st.session_state.voc_mensaje = None
    
    def jugar(self):
        st.markdown("### 📚 Vocabulario")
        
        # Mostrar puntos
        st.metric("Puntos", st.session_state.voc_puntos)
        
        # Generar primera pregunta si no existe
        if st.session_state.voc_palabra_actual is None:
            self.generar_pregunta()
        
        # Mostrar pregunta
        st.markdown(f"### **¿Qué significa...**")
        st.markdown(f"## **'{st.session_state.voc_palabra_actual}'**")
        
        # Mostrar mensaje si existe
        if st.session_state.voc_mensaje:
            if "✅" in st.session_state.voc_mensaje:
                st.success(st.session_state.voc_mensaje)
            else:
                st.error(st.session_state.voc_mensaje)
        
        # Mostrar opciones
        cols = st.columns(2)
        for i, opcion in enumerate(st.session_state.voc_opciones):
            with cols[i % 2]:
                disabled = st.session_state.voc_respondido
                if st.button(
                    opcion, 
                    key=f"voc_{i}_{st.session_state.voc_palabra_actual}", 
                    use_container_width=True,
                    disabled=disabled
                ):
                    if opcion == st.session_state.voc_definicion_correcta:
                        st.session_state.voc_puntos += 15
                        st.session_state.voc_respondido = True
                        st.session_state.voc_mensaje = "✅ ¡Correcto! +15 puntos"
                        st.balloons()
                    else:
                        st.session_state.voc_respondido = True
                        st.session_state.voc_mensaje = f"❌ Incorrecto. El significado es: {st.session_state.voc_definicion_correcta}"
                    st.rerun()
        
        # Botón para siguiente pregunta
        if st.session_state.voc_respondido:
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("➡️ Siguiente Palabra", use_container_width=True):
                    self.generar_pregunta()
                    st.rerun()
        
        return st.session_state.voc_puntos
