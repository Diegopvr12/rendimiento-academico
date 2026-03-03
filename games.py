"""Juegos educativos para EduPlay"""
import streamlit as st
import random
import time

class JuegoMatematicas:
    def __init__(self):
        self.puntos = 0
        self.preguntas = 0
        self.aciertos = 0
    
    def jugar(self):
        st.markdown("### 🧮 Matemáticas Rápidas")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Puntos", self.puntos)
        with col2:
            st.metric("Aciertos", f"{self.aciertos}/{self.preguntas}" if self.preguntas > 0 else "0/0")
        
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
        
        st.markdown(f"### **{num1} {op} {num2} = ?**")
        
        opciones = [resultado]
        while len(opciones) < 4:
            op = resultado + random.randint(-3, 3)
            if op not in opciones and op > 0:
                opciones.append(op)
        
        random.shuffle(opciones)
        
        cols = st.columns(2)
        for i, opcion in enumerate(opciones):
            with cols[i % 2]:
                if st.button(f"**{opcion}**", key=f"math_{i}_{random.randint(1,1000)}", use_container_width=True):
                    self.preguntas += 1
                    if opcion == resultado:
                        self.puntos += 10
                        self.aciertos += 1
                        st.balloons()
                        st.success("✅ ¡Correcto! +10 puntos")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(f"❌ Incorrecto. La respuesta era {resultado}")
                        time.sleep(1)
                        st.rerun()
        
        return self.puntos

class JuegoVocabulario:
    def __init__(self):
        self.palabras = {
            'efímero': 'Que dura poco tiempo',
            'magnánimo': 'Que tiene grandeza de espíritu',
            'paradójico': 'Que contiene una paradoja',
            'sutil': 'Delicado, agudo',
            'inefable': 'Que no se puede explicar',
        }
    
    def jugar(self):
        st.markdown("### 📚 Vocabulario")
        
        palabra = random.choice(list(self.palabras.keys()))
        definicion = self.palabras[palabra]
        
        st.markdown(f"### **¿Qué significa...**")
        st.markdown(f"## **'{palabra}'**")
        
        opciones = [definicion]
        otras_def = random.sample(list(self.palabras.values()), 3)
        opciones.extend(otras_def)
        random.shuffle(opciones)
        
        cols = st.columns(2)
        for i, opcion in enumerate(opciones):
            with cols[i % 2]:
                if st.button(opcion, key=f"voc_{i}", use_container_width=True):
                    if opcion == definicion:
                        st.balloons()
                        st.success("✅ ¡Correcto! +15 puntos")
                        time.sleep(0.5)
                        return 15
                    else:
                        st.error(f"❌ Incorrecto. El significado es: {definicion}")
                        time.sleep(1)
                        return 0
        return 0

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
        }
    
    def jugar(self):
        st.markdown("### 🌍 Geografía")
        
        pais = random.choice(list(self.capitales.keys()))
        capital_correcta = self.capitales[pais]
        
        st.markdown(f"### **¿Cuál es la capital de...**")
        st.markdown(f"## **{pais}**")
        
        otras_capitales = random.sample(list(self.capitales.values()), 3)
        opciones = [capital_correcta] + otras_capitales
        random.shuffle(opciones)
        
        cols = st.columns(2)
        for i, opcion in enumerate(opciones):
            with cols[i % 2]:
                if st.button(opcion, key=f"geo_{i}", use_container_width=True):
                    if opcion == capital_correcta:
                        st.balloons()
                        st.success("✅ ¡Correcto! +20 puntos")
                        time.sleep(0.5)
                        return 20
                    else:
                        st.error(f"❌ Incorrecto. La capital es {capital_correcta}")
                        time.sleep(1)
                        return 0
        return 0
