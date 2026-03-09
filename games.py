"""Juegos educativos para EduPlay"""
import streamlit as st
import random

# ============================================
# JUEGO DE MATEMÁTICAS (VERSIÓN QUE FUNCIONA)
# ============================================
class JuegoMatematicas:
    def __init__(self):
        # Inicializar variables
        if 'math_puntos' not in st.session_state:
            st.session_state.math_puntos = 0
        
        # Generar primera pregunta
        self.generar_pregunta()
    
    def generar_pregunta(self):
        """Genera una nueva pregunta"""
        # Elegir operador
        self.operador = random.choice(['+', '-', '×'])
        
        if self.operador == '+':
            self.num1 = random.randint(1, 20)
            self.num2 = random.randint(1, 20)
            self.resultado = self.num1 + self.num2
        
        elif self.operador == '-':
            self.num1 = random.randint(5, 20)
            self.num2 = random.randint(1, self.num1)
            self.resultado = self.num1 - self.num2
        
        else:  # ×
            self.num1 = random.randint(2, 10)
            self.num2 = random.randint(2, 10)
            self.resultado = self.num1 * self.num2
        
        # Generar opciones
        self.opciones = [self.resultado]
        while len(self.opciones) < 4:
            op = self.resultado + random.randint(-5, 5)
            if op not in self.opciones and op > 0:
                self.opciones.append(op)
        
        random.shuffle(self.opciones)
        self.respondido = False
    
    def jugar(self):
        st.markdown("## 🧮 Matemáticas Rápidas")
        st.caption("Pon a prueba tu agilidad mental")
        
        # Mostrar puntos
        st.metric("Puntos", st.session_state.math_puntos)
        
        # Mostrar la pregunta (FORMA SIMPLE Y SEGURA)
        st.markdown(f"### **{self.num1} {self.operador} {self.num2} = ?**")
        
        # Crear 4 botones en 2 columnas
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(f"**{self.opciones[0]}**", key="btn1", use_container_width=True, disabled=self.respondido):
                if self.opciones[0] == self.resultado:
                    st.session_state.math_puntos += 10
                    st.success("✅ ¡Correcto! +10 puntos")
                else:
                    st.error(f"❌ Incorrecto. La respuesta era {self.resultado}")
                self.respondido = True
                st.rerun()
            
            if st.button(f"**{self.opciones[1]}**", key="btn2", use_container_width=True, disabled=self.respondido):
                if self.opciones[1] == self.resultado:
                    st.session_state.math_puntos += 10
                    st.success("✅ ¡Correcto! +10 puntos")
                else:
                    st.error(f"❌ Incorrecto. La respuesta era {self.resultado}")
                self.respondido = True
                st.rerun()
        
        with col2:
            if st.button(f"**{self.opciones[2]}**", key="btn3", use_container_width=True, disabled=self.respondido):
                if self.opciones[2] == self.resultado:
                    st.session_state.math_puntos += 10
                    st.success("✅ ¡Correcto! +10 puntos")
                else:
                    st.error(f"❌ Incorrecto. La respuesta era {self.resultado}")
                self.respondido = True
                st.rerun()
            
            if st.button(f"**{self.opciones[3]}**", key="btn4", use_container_width=True, disabled=self.respondido):
                if self.opciones[3] == self.resultado:
                    st.session_state.math_puntos += 10
                    st.success("✅ ¡Correcto! +10 puntos")
                else:
                    st.error(f"❌ Incorrecto. La respuesta era {self.resultado}")
                self.respondido = True
                st.rerun()
        
        # Botón siguiente pregunta
        if self.respondido:
            if st.button("➡️ Siguiente Pregunta", key="next", use_container_width=True):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.math_puntos


# ============================================
# JUEGO DE GEOGRAFÍA (SIMPLIFICADO)
# ============================================
class JuegoGeografia:
    def __init__(self):
        if 'geo_puntos' not in st.session_state:
            st.session_state.geo_puntos = 0
        
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
        self.generar_pregunta()
    
    def generar_pregunta(self):
        self.pais = random.choice(list(self.capitales.keys()))
        self.capital_correcta = self.capitales[self.pais]
        
        otras = random.sample([c for p, c in self.capitales.items() if p != self.pais], 3)
        self.opciones = [self.capital_correcta] + otras
        random.shuffle(self.opciones)
        self.respondido = False
    
    def jugar(self):
        st.markdown("## 🌍 Geografía")
        st.metric("Puntos", st.session_state.geo_puntos)
        
        st.markdown(f"### ¿Cuál es la capital de **{self.pais}**?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(self.opciones[0], key="geo1", use_container_width=True, disabled=self.respondido):
                if self.opciones[0] == self.capital_correcta:
                    st.session_state.geo_puntos += 20
                    st.success("✅ ¡Correcto! +20 puntos")
                else:
                    st.error(f"❌ Incorrecto. La capital es {self.capital_correcta}")
                self.respondido = True
                st.rerun()
            
            if st.button(self.opciones[1], key="geo2", use_container_width=True, disabled=self.respondido):
                if self.opciones[1] == self.capital_correcta:
                    st.session_state.geo_puntos += 20
                    st.success("✅ ¡Correcto! +20 puntos")
                else:
                    st.error(f"❌ Incorrecto. La capital es {self.capital_correcta}")
                self.respondido = True
                st.rerun()
        
        with col2:
            if st.button(self.opciones[2], key="geo3", use_container_width=True, disabled=self.respondido):
                if self.opciones[2] == self.capital_correcta:
                    st.session_state.geo_puntos += 20
                    st.success("✅ ¡Correcto! +20 puntos")
                else:
                    st.error(f"❌ Incorrecto. La capital es {self.capital_correcta}")
                self.respondido = True
                st.rerun()
            
            if st.button(self.opciones[3], key="geo4", use_container_width=True, disabled=self.respondido):
                if self.opciones[3] == self.capital_correcta:
                    st.session_state.geo_puntos += 20
                    st.success("✅ ¡Correcto! +20 puntos")
                else:
                    st.error(f"❌ Incorrecto. La capital es {self.capital_correcta}")
                self.respondido = True
                st.rerun()
        
        if self.respondido:
            if st.button("➡️ Siguiente País", key="geo_next", use_container_width=True):
                self.generar_pregunta()
                st.rerun()
        
        return st.session_state.geo_puntos
