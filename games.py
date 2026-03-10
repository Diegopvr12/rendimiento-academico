"""Juegos educativos para EduPlay"""
import streamlit as st
import random

# ============================================
# JUEGO DE MATEMÁTICAS (CON 4 OPCIONES)
# ============================================
class JuegoMatematicas:
    def __init__(self):
        # Inicializar variables de sesión
        if 'math_puntos' not in st.session_state:
            st.session_state.math_puntos = 0
        if 'math_preguntas' not in st.session_state:
            st.session_state.math_preguntas = 0
        if 'math_aciertos' not in st.session_state:
            st.session_state.math_aciertos = 0
        if 'math_estado' not in st.session_state:
            st.session_state.math_estado = self.generar_pregunta()
    
    def generar_pregunta(self):
        """Genera una nueva pregunta con 4 opciones"""
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
        
        # Generar 4 opciones SIEMPRE
        opciones = [resultado]
        
        # Generar 3 opciones incorrectas variadas
        intentos = 0
        while len(opciones) < 4 and intentos < 50:
            if operador in ['+', '-']:
                incorrecta = resultado + random.randint(-5, 5)
            else:
                incorrecta = resultado + random.randint(-8, 8)
            
            if incorrecta > 0 and incorrecta not in opciones:
                opciones.append(incorrecta)
            intentos += 1
        
        # Si no se generaron 4 opciones, completar con valores por defecto
        while len(opciones) < 4:
            opciones.append(resultado + len(opciones) + 1)
        
        random.shuffle(opciones)
        
        return {
            'num1': num1,
            'num2': num2,
            'operador': operador,
            'resultado': resultado,
            'opciones': opciones,
            'respondido': False,
            'mensaje': None
        }
    
    def jugar(self):
        st.markdown("### 🧮 Matemáticas Rápidas")
        st.caption("Pon a prueba tu agilidad mental")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Puntos", st.session_state.math_puntos)
        with col2:
            if st.session_state.math_preguntas > 0:
                precision = (st.session_state.math_aciertos / st.session_state.math_preguntas) * 100
                st.metric("Precisión", f"{precision:.0f}%")
        with col3:
            st.metric("Preguntas", st.session_state.math_preguntas)
        
        if st.session_state.math_estado['mensaje']:
            if "✅" in st.session_state.math_estado['mensaje']:
                st.success(st.session_state.math_estado['mensaje'])
            else:
                st.error(st.session_state.math_estado['mensaje'])
        
        # Mostrar pregunta
        num1 = st.session_state.math_estado['num1']
        num2 = st.session_state.math_estado['num2']
        operador = st.session_state.math_estado['operador']
        
        st.markdown(f"## **{num1} {operador} {num2} = ?**")
        
        # Mostrar 4 opciones en 2 columnas
        opciones = st.session_state.math_estado['opciones']
        respondido = st.session_state.math_estado['respondido']
        
        # Crear 2 columnas
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(f"**{opciones[0]}**", key="math_1", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[0])
            
            if st.button(f"**{opciones[1]}**", key="math_2", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[1])
        
        with col2:
            if st.button(f"**{opciones[2]}**", key="math_3", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[2])
            
            if st.button(f"**{opciones[3]}**", key="math_4", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[3])
        
        # Botón siguiente pregunta
        if st.session_state.math_estado['respondido']:
            if st.button("➡️ Siguiente Pregunta", key="math_next", use_container_width=True):
                st.session_state.math_estado = self.generar_pregunta()
                st.rerun()
        
        return st.session_state.math_puntos
    
    def verificar_respuesta(self, respuesta):
        st.session_state.math_preguntas += 1
        
        if respuesta == st.session_state.math_estado['resultado']:
            st.session_state.math_puntos += 10
            st.session_state.math_aciertos += 1
            st.session_state.math_estado['mensaje'] = "✅ ¡Correcto! +10 puntos"
            st.balloons()
        else:
            st.session_state.math_estado['mensaje'] = f"❌ Incorrecto. La respuesta era {st.session_state.math_estado['resultado']}"
        
        st.session_state.math_estado['respondido'] = True
        st.rerun()


# ============================================
# JUEGO DE ESPAÑOL (CON 4 OPCIONES)
# ============================================
class JuegoEspanol:
    def __init__(self):
        if 'esp_puntos' not in st.session_state:
            st.session_state.esp_puntos = 0
        if 'esp_preguntas' not in st.session_state:
            st.session_state.esp_preguntas = 0
        if 'esp_aciertos' not in st.session_state:
            st.session_state.esp_aciertos = 0
        if 'esp_estado' not in st.session_state:
            st.session_state.esp_estado = self.generar_pregunta()
    
    def generar_pregunta(self):
        preguntas = [
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
            },
            {
                'pregunta': '¿Qué es un verbo?',
                'opciones': ['Acción', 'Persona', 'Lugar', 'Cosa'],
                'correcta': 'Acción'
            },
            {
                'pregunta': '¿Cuál es el antónimo de "rápido"?',
                'opciones': ['Lento', 'Veloz', 'Ágil', 'Raudo'],
                'correcta': 'Lento'
            },
            {
                'pregunta': '¿Qué palabra es un adjetivo?',
                'opciones': ['Hermoso', 'Correr', 'Casa', 'Rápidamente'],
                'correcta': 'Hermoso'
            },
            {
                'pregunta': '¿Cuál es el sinónimo de "bello"?',
                'opciones': ['Hermoso', 'Feo', 'Grande', 'Pequeño'],
                'correcta': 'Hermoso'
            },
            {
                'pregunta': '¿Qué son los artículos?',
                'opciones': ['el, la, los, las', 'correr, saltar', 'grande, pequeño', 'casa, perro'],
                'correcta': 'el, la, los, las'
            }
        ]
        
        pregunta = random.choice(preguntas)
        return {
            'pregunta': pregunta['pregunta'],
            'correcta': pregunta['correcta'],
            'opciones': pregunta['opciones'],
            'respondido': False,
            'mensaje': None
        }
    
    def jugar(self):
        st.markdown("### 📚 Español")
        st.caption("Pon a prueba tu conocimiento del idioma")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Puntos", st.session_state.esp_puntos)
        with col2:
            if st.session_state.esp_preguntas > 0:
                precision = (st.session_state.esp_aciertos / st.session_state.esp_preguntas) * 100
                st.metric("Precisión", f"{precision:.0f}%")
        with col3:
            st.metric("Preguntas", st.session_state.esp_preguntas)
        
        if st.session_state.esp_estado['mensaje']:
            if "✅" in st.session_state.esp_estado['mensaje']:
                st.success(st.session_state.esp_estado['mensaje'])
            else:
                st.error(st.session_state.esp_estado['mensaje'])
        
        st.markdown(f"### {st.session_state.esp_estado['pregunta']}")
        
        # Mostrar 4 opciones
        opciones = st.session_state.esp_estado['opciones']
        respondido = st.session_state.esp_estado['respondido']
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(opciones[0], key="esp_1", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[0])
            
            if st.button(opciones[1], key="esp_2", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[1])
        
        with col2:
            if st.button(opciones[2], key="esp_3", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[2])
            
            if st.button(opciones[3], key="esp_4", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[3])
        
        if st.session_state.esp_estado['respondido']:
            if st.button("➡️ Siguiente Pregunta", key="esp_next", use_container_width=True):
                st.session_state.esp_estado = self.generar_pregunta()
                st.rerun()
        
        return st.session_state.esp_puntos
    
    def verificar_respuesta(self, respuesta):
        st.session_state.esp_preguntas += 1
        
        if respuesta == st.session_state.esp_estado['correcta']:
            st.session_state.esp_puntos += 15
            st.session_state.esp_aciertos += 1
            st.session_state.esp_estado['mensaje'] = "✅ ¡Correcto! +15 puntos"
            st.balloons()
        else:
            st.session_state.esp_estado['mensaje'] = f"❌ Incorrecto. La respuesta es: {st.session_state.esp_estado['correcta']}"
        
        st.session_state.esp_estado['respondido'] = True
        st.rerun()


# ============================================
# JUEGO DE GEOGRAFÍA (CON 4 OPCIONES)
# ============================================
class JuegoGeografia:
    def __init__(self):
        if 'geo_puntos' not in st.session_state:
            st.session_state.geo_puntos = 0
        if 'geo_preguntas' not in st.session_state:
            st.session_state.geo_preguntas = 0
        if 'geo_aciertos' not in st.session_state:
            st.session_state.geo_aciertos = 0
        if 'geo_estado' not in st.session_state:
            st.session_state.geo_estado = self.generar_pregunta()
    
    def generar_pregunta(self):
        capitales = {
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
            'Uruguay': 'Montevideo',
            'Portugal': 'Lisboa',
            'Grecia': 'Atenas',
            'Turquía': 'Ankara',
            'Suecia': 'Estocolmo'
        }
        
        pais = random.choice(list(capitales.keys()))
        capital = capitales[pais]
        
        # Seleccionar 3 capitales incorrectas
        otras_capitales = [c for p, c in capitales.items() if p != pais]
        otras = random.sample(otras_capitales, 3)
        
        opciones = [capital] + otras
        random.shuffle(opciones)
        
        return {
            'pais': pais,
            'capital': capital,
            'opciones': opciones,
            'respondido': False,
            'mensaje': None
        }
    
    def jugar(self):
        st.markdown("### 🌍 Geografía")
        st.caption("Adivina las capitales del mundo")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Puntos", st.session_state.geo_puntos)
        with col2:
            if st.session_state.geo_preguntas > 0:
                precision = (st.session_state.geo_aciertos / st.session_state.geo_preguntas) * 100
                st.metric("Precisión", f"{precision:.0f}%")
        with col3:
            st.metric("Preguntas", st.session_state.geo_preguntas)
        
        if st.session_state.geo_estado['mensaje']:
            if "✅" in st.session_state.geo_estado['mensaje']:
                st.success(st.session_state.geo_estado['mensaje'])
            else:
                st.error(st.session_state.geo_estado['mensaje'])
        
        st.markdown(f"### ¿Cuál es la capital de **{st.session_state.geo_estado['pais']}**?")
        
        # Mostrar 4 opciones
        opciones = st.session_state.geo_estado['opciones']
        respondido = st.session_state.geo_estado['respondido']
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(opciones[0], key="geo_1", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[0])
            
            if st.button(opciones[1], key="geo_2", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[1])
        
        with col2:
            if st.button(opciones[2], key="geo_3", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[2])
            
            if st.button(opciones[3], key="geo_4", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[3])
        
        if st.session_state.geo_estado['respondido']:
            if st.button("➡️ Siguiente País", key="geo_next", use_container_width=True):
                st.session_state.geo_estado = self.generar_pregunta()
                st.rerun()
        
        return st.session_state.geo_puntos
    
    def verificar_respuesta(self, respuesta):
        st.session_state.geo_preguntas += 1
        
        if respuesta == st.session_state.geo_estado['capital']:
            st.session_state.geo_puntos += 20
            st.session_state.geo_aciertos += 1
            st.session_state.geo_estado['mensaje'] = "✅ ¡Correcto! +20 puntos"
            st.balloons()
        else:
            st.session_state.geo_estado['mensaje'] = f"❌ Incorrecto. La capital de {st.session_state.geo_estado['pais']} es {st.session_state.geo_estado['capital']}"
        
        st.session_state.geo_estado['respondido'] = True
        st.rerun()


# ============================================
# JUEGO DE HISTORIA (CON 4 OPCIONES)
# ============================================
class JuegoHistoria:
    def __init__(self):
        if 'hist_puntos' not in st.session_state:
            st.session_state.hist_puntos = 0
        if 'hist_preguntas' not in st.session_state:
            st.session_state.hist_preguntas = 0
        if 'hist_aciertos' not in st.session_state:
            st.session_state.hist_aciertos = 0
        if 'hist_estado' not in st.session_state:
            st.session_state.hist_estado = self.generar_pregunta()
    
    def generar_pregunta(self):
        preguntas = [
            {
                'pregunta': '¿En qué año llegó Cristóbal Colón a América?',
                'opciones': ['1492', '1498', '1500', '1485'],
                'correcta': '1492'
            },
            {
                'pregunta': '¿Quién fue el primer presidente de México?',
                'opciones': ['Guadalupe Victoria', 'Benito Juárez', 'Porfirio Díaz', 'Miguel Hidalgo'],
                'correcta': 'Guadalupe Victoria'
            },
            {
                'pregunta': '¿Qué civilización construyó Machu Picchu?',
                'opciones': ['Inca', 'Maya', 'Azteca', 'Olmeca'],
                'correcta': 'Inca'
            },
            {
                'pregunta': '¿En qué año comenzó la Segunda Guerra Mundial?',
                'opciones': ['1939', '1941', '1935', '1945'],
                'correcta': '1939'
            },
            {
                'pregunta': '¿Quiénes lideraron la Revolución Mexicana?',
                'opciones': ['Madero, Zapata y Villa', 'Hidalgo y Morelos', 'Juárez y Díaz', 'Carranza y Obregón'],
                'correcta': 'Madero, Zapata y Villa'
            },
            {
                'pregunta': '¿Qué imperio lideraba Moctezuma?',
                'opciones': ['Azteca', 'Inca', 'Maya', 'Tolteca'],
                'correcta': 'Azteca'
            },
            {
                'pregunta': '¿En qué año se independizó México?',
                'opciones': ['1821', '1810', '1824', '1857'],
                'correcta': '1821'
            },
            {
                'pregunta': '¿Quién fue Simón Bolívar?',
                'opciones': ['Libertador de América', 'Explorador español', 'Rey de España', 'Científico'],
                'correcta': 'Libertador de América'
            },
            {
                'pregunta': '¿Qué país construyó la Gran Muralla?',
                'opciones': ['China', 'Japón', 'Mongolia', 'India'],
                'correcta': 'China'
            },
            {
                'pregunta': '¿En qué siglo fue la Revolución Francesa?',
                'opciones': ['XVIII', 'XIX', 'XVII', 'XX'],
                'correcta': 'XVIII'
            },
            {
                'pregunta': '¿Quién pintó la Mona Lisa?',
                'opciones': ['Leonardo da Vinci', 'Miguel Ángel', 'Rafael', 'Donatello'],
                'correcta': 'Leonardo da Vinci'
            },
            {
                'pregunta': '¿Qué civilización construyó las pirámides?',
                'opciones': ['Egipcia', 'Romana', 'Griega', 'Persa'],
                'correcta': 'Egipcia'
            },
            {
                'pregunta': '¿Quién fue el primer emperador romano?',
                'opciones': ['Augusto', 'Julio César', 'Nerón', 'Constantino'],
                'correcta': 'Augusto'
            },
            {
                'pregunta': '¿En qué año cayó el Muro de Berlín?',
                'opciones': ['1989', '1991', '1985', '1979'],
                'correcta': '1989'
            },
            {
                'pregunta': '¿Quién es el "Padre de la Patria" en México?',
                'opciones': ['Miguel Hidalgo', 'José María Morelos', 'Vicente Guerrero', 'Agustín de Iturbide'],
                'correcta': 'Miguel Hidalgo'
            }
        ]
        
        pregunta = random.choice(preguntas)
        return {
            'pregunta': pregunta['pregunta'],
            'correcta': pregunta['correcta'],
            'opciones': pregunta['opciones'],
            'respondido': False,
            'mensaje': None
        }
    
    def jugar(self):
        st.markdown("### 📜 Historia")
        st.caption("Viaja a través del tiempo")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Puntos", st.session_state.hist_puntos)
        with col2:
            if st.session_state.hist_preguntas > 0:
                precision = (st.session_state.hist_aciertos / st.session_state.hist_preguntas) * 100
                st.metric("Precisión", f"{precision:.0f}%")
        with col3:
            st.metric("Preguntas", st.session_state.hist_preguntas)
        
        if st.session_state.hist_estado['mensaje']:
            if "✅" in st.session_state.hist_estado['mensaje']:
                st.success(st.session_state.hist_estado['mensaje'])
            else:
                st.error(st.session_state.hist_estado['mensaje'])
        
        st.markdown(f"### {st.session_state.hist_estado['pregunta']}")
        
        # Mostrar 4 opciones
        opciones = st.session_state.hist_estado['opciones']
        respondido = st.session_state.hist_estado['respondido']
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(opciones[0], key="hist_1", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[0])
            
            if st.button(opciones[1], key="hist_2", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[1])
        
        with col2:
            if st.button(opciones[2], key="hist_3", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[2])
            
            if st.button(opciones[3], key="hist_4", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[3])
        
        if st.session_state.hist_estado['respondido']:
            if st.button("➡️ Siguiente Pregunta", key="hist_next", use_container_width=True):
                st.session_state.hist_estado = self.generar_pregunta()
                st.rerun()
        
        return st.session_state.hist_puntos
    
    def verificar_respuesta(self, respuesta):
        st.session_state.hist_preguntas += 1
        
        if respuesta == st.session_state.hist_estado['correcta']:
            st.session_state.hist_puntos += 25
            st.session_state.hist_aciertos += 1
            st.session_state.hist_estado['mensaje'] = "✅ ¡Correcto! +25 puntos"
            st.balloons()
        else:
            st.session_state.hist_estado['mensaje'] = f"❌ Incorrecto. La respuesta es: {st.session_state.hist_estado['correcta']}"
        
        st.session_state.hist_estado['respondido'] = True
        st.rerun()


# ============================================
# JUEGO DE FILOSOFÍA (CON 4 OPCIONES)
# ============================================
class JuegoFilosofia:
    def __init__(self):
        if 'fil_puntos' not in st.session_state:
            st.session_state.fil_puntos = 0
        if 'fil_preguntas' not in st.session_state:
            st.session_state.fil_preguntas = 0
        if 'fil_aciertos' not in st.session_state:
            st.session_state.fil_aciertos = 0
        if 'fil_estado' not in st.session_state:
            st.session_state.fil_estado = self.generar_pregunta()
    
    def generar_pregunta(self):
        preguntas = [
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
            },
            {
                'pregunta': '¿Quién es el padre de la filosofía occidental?',
                'opciones': ['Tales de Mileto', 'Sócrates', 'Platón', 'Aristóteles'],
                'correcta': 'Tales de Mileto'
            },
            {
                'pregunta': '¿Qué corriente fundó Epicuro?',
                'opciones': ['Epicureísmo', 'Estoicismo', 'Cinicismo', 'Escepticismo'],
                'correcta': 'Epicureísmo'
            },
            {
                'pregunta': '¿Qué es el "imperativo categórico" de Kant?',
                'opciones': ['Regla moral universal', 'Ley física', 'Tipo de gobierno', 'Teoría del conocimiento'],
                'correcta': 'Regla moral universal'
            },
            {
                'pregunta': '¿Qué filósofo dijo "Solo sé que nada sé"?',
                'opciones': ['Sócrates', 'Platón', 'Aristóteles', 'Descartes'],
                'correcta': 'Sócrates'
            },
            {
                'pregunta': '¿Quién escribió "El contrato social"?',
                'opciones': ['Rousseau', 'Voltaire', 'Montesquieu', 'Hobbes'],
                'correcta': 'Rousseau'
            }
        ]
        
        pregunta = random.choice(preguntas)
        return {
            'pregunta': pregunta['pregunta'],
            'correcta': pregunta['correcta'],
            'opciones': pregunta['opciones'],
            'respondido': False,
            'mensaje': None
        }
    
    def jugar(self):
        st.markdown("### 🤔 Filosofía")
        st.caption("Explora el mundo de las ideas")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Puntos", st.session_state.fil_puntos)
        with col2:
            if st.session_state.fil_preguntas > 0:
                precision = (st.session_state.fil_aciertos / st.session_state.fil_preguntas) * 100
                st.metric("Precisión", f"{precision:.0f}%")
        with col3:
            st.metric("Preguntas", st.session_state.fil_preguntas)
        
        if st.session_state.fil_estado['mensaje']:
            if "✅" in st.session_state.fil_estado['mensaje']:
                st.success(st.session_state.fil_estado['mensaje'])
            else:
                st.error(st.session_state.fil_estado['mensaje'])
        
        st.markdown(f"### {st.session_state.fil_estado['pregunta']}")
        
        # Mostrar 4 opciones
        opciones = st.session_state.fil_estado['opciones']
        respondido = st.session_state.fil_estado['respondido']
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(opciones[0], key="fil_1", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[0])
            
            if st.button(opciones[1], key="fil_2", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[1])
        
        with col2:
            if st.button(opciones[2], key="fil_3", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[2])
            
            if st.button(opciones[3], key="fil_4", use_container_width=True, disabled=respondido):
                self.verificar_respuesta(opciones[3])
        
        if st.session_state.fil_estado['respondido']:
            if st.button("➡️ Siguiente Pregunta", key="fil_next", use_container_width=True):
                st.session_state.fil_estado = self.generar_pregunta()
                st.rerun()
        
        return st.session_state.fil_puntos
    
    def verificar_respuesta(self, respuesta):
        st.session_state.fil_preguntas += 1
        
        if respuesta == st.session_state.fil_estado['correcta']:
            st.session_state.fil_puntos += 25
            st.session_state.fil_aciertos += 1
            st.session_state.fil_estado['mensaje'] = "✅ ¡Correcto! +25 puntos"
            st.balloons()
        else:
            st.session_state.fil_estado['mensaje'] = f"❌ Incorrecto. La respuesta es: {st.session_state.fil_estado['correcta']}"
        
        st.session_state.fil_estado['respondido'] = True
        st.rerun()
