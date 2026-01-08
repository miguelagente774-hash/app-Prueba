import sqlite3 as sql

class ConexionDB:
    def __init__(self, nombre_db="_internal/database/usuarios.db"):
        self.nombre_db = nombre_db
        self.conexion = sql.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()
        self.Crear_tablas()
        

    def Crear_tablas(self):
        Conexion = self.conexion
        cursor = Conexion.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS usuarios(
        id_cedula INTERGER,
        nombre VARCHAR(100),
        apellido VARCHAR(100),
        edad INTERGER,
        trabajo VARCHAR(100),
        PRIMARY KEY(id_cedula)
        )
        """
        cursor.execute(sql)
        Conexion.commit()

    def Cerrar(self):
        self.conexion.commit()
        self.conexion.close()