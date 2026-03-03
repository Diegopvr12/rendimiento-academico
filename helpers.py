"""Funciones auxiliares para EduPlay"""
import json
import os
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/usuarios.json")

def cargar_usuarios():
    """Carga los usuarios desde el archivo JSON"""
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    """Guarda los usuarios en el archivo JSON"""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=2, ensure_ascii=False)

def crear_usuario_si_no_existe(usuarios, nombre):
    """Crea un usuario si no existe"""
    if nombre not in usuarios:
        usuarios[nombre] = {
            'puntos': 0,
            'juegos_completados': 0,
            'racha': 0,
            'ultima_conexion': datetime.now().strftime('%Y-%m-%d'),
            'logros': [],
            'historial': [],
            'nivel': 1
        }
        guardar_usuarios(usuarios)
    return usuarios[nombre]

def calcular_nivel(puntos):
    """Calcula el nivel según los puntos"""
    return puntos // 100 + 1

def formatear_numero(num):
    """Formatea números grandes"""
    if num < 1000:
        return str(num)
    elif num < 1000000:
        return f"{num/1000:.1f}K"
    return f"{num/1000000:.1f}M"

def verificar_logros(usuario, datos):
    """Verifica y asigna nuevos logros"""
    nuevos_logros = []
    
    if datos['puntos'] >= 100 and "🏆 100 Puntos" not in datos['logros']:
        nuevos_logros.append("🏆 100 Puntos")
    if datos['puntos'] >= 500 and "🏆 500 Puntos" not in datos['logros']:
        nuevos_logros.append("🏆 500 Puntos")
    if datos['juegos_completados'] >= 10 and "🎮 10 Juegos" not in datos['logros']:
        nuevos_logros.append("🎮 10 Juegos")
    if datos['juegos_completados'] >= 50 and "🎮 50 Juegos" not in datos['logros']:
        nuevos_logros.append("🎮 50 Juegos")
    
    datos['logros'].extend(nuevos_logros)
    return nuevos_logros
