import sqlite3

class Conexion:
    def __init__(self, base_de_datos):
        self.base_de_datos = base_de_datos
        self.conexion = sqlite3.connect(self.base_de_datos)
        self.cursor = self.conexion.cursor()
    def crear_tabla_tareas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarea TEXT,
                fecha TEXT
            )
        """)
        self.conexion.commit()
    def insertar_tarea(self, tarea, fecha):
        self.cursor.execute("INSERT INTO tareas (tarea, fecha) VALUES (?, ?)", (tarea, fecha))
        self.conexion.commit()

    def mostrar_tareas(self):
        self.cursor.execute("SELECT * FROM tareas Order By id DESC")
        tareas = self.cursor.fetchall()
        return tareas
    def eliminar_tareas(self):
        self.cursor.execute("DELETE FROM tareas")
        self.conexion.commit()


    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()