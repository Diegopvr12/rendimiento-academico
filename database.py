"""Manejo de base de datos para EduPlay"""
from helpers import cargar_usuarios, guardar_usuarios, crear_usuario_si_no_existe, verificar_logros
from datetime import datetime

class Database:
    def __init__(self):
        self.usuarios = cargar_usuarios()
    
    def obtener_usuario(self, nombre):
        """Obtiene datos de un usuario"""
        return crear_usuario_si_no_existe(self.usuarios, nombre)
    
    def actualizar_puntos(self, usuario, puntos, juego):
        """Actualiza puntos de un usuario"""
        if usuario in self.usuarios:
            user = self.usuarios[usuario]
            user['puntos'] += puntos
            user['juegos_completados'] += 1
            
            user['historial'].append({
                'fecha': datetime.now().strftime('%Y-%m-%d %H:%M'),
                'juego': juego,
                'puntos': puntos
            })
            
            nuevos = verificar_logros(usuario, user)
            user['nivel'] = user['puntos'] // 100 + 1
            
            guardar_usuarios(self.usuarios)
            return True, nuevos
        return False, []
    
    def obtener_ranking(self):
        """Obtiene ranking de usuarios"""
        ranking = []
        for usuario, datos in self.usuarios.items():
            ranking.append({
                'usuario': usuario,
                'puntos': datos['puntos'],
                'juegos': datos['juegos_completados'],
                'nivel': datos['nivel']
            })
        return sorted(ranking, key=lambda x: x['puntos'], reverse=True)[:20]
    
    def obtener_estadisticas_globales(self):
        """Obtiene estadísticas globales"""
        total_usuarios = len(self.usuarios)
        total_puntos = sum(u['puntos'] for u in self.usuarios.values())
        total_juegos = sum(u['juegos_completados'] for u in self.usuarios.values())
        
        return {
            'total_usuarios': total_usuarios,
            'total_puntos': total_puntos,
            'total_juegos': total_juegos
        }
