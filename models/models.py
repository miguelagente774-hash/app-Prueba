from models.conexiondb import ConexionDB

class Persona():
    def __init__(self, id_cedula, nombre, apellido, edad, trabajo):
        self.id_cedula = id_cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.trabajo = trabajo


class Modelo_usuarios():
    def __init__(self):
        self.bd = ConexionDB()

    def Buscar_usuario(self, id_cedula):
        conexion = ConexionDB()
        sql = f"""
            SELECT * FROM usuarios WHERE id_cedula = {id_cedula}
        """
        conexion.cursor.execute(sql)
        resultado = conexion.cursor.fetchall()
        conexion.Cerrar()
        return resultado

    def Guardar_usuario(self, persona):
        conexion = self.bd
        sql = f"""INSERT INTO usuarios (id_cedula, nombre, apellido, edad, trabajo)
        VALUES ({persona.id_cedula}, '{persona.nombre}', '{persona.apellido}', {persona.edad}, '{persona.trabajo}')
        """
        conexion.cursor.execute(sql)
        conexion.Cerrar()
    
    def Verficar_cedula_existe(self, id_cedula):
        try:
            conexion = ConexionDB()
            sql = f"""
            SELECT id_cedula FROM usuarios WHERE id_cedula = {id_cedula} 
            """
            conexion.cursor.execute(sql)
            resultado = conexion.cursor.fetchone()
            conexion.Cerrar()
            return resultado is not None
            
        except:
            return False
        
    def eliminar_usuario(self, id_cedula):
        conexion = ConexionDB()
        sql = f"""
        DELETE FROM usuarios WHERE id_cedula = {id_cedula}
        """
        try:
            conexion.cursor.execute(sql)
            conexion.Cerrar()
            return True
        except:
            return False

    def Modificar_datos_usuario(self, persona):
        conexion = ConexionDB()
        sql = f"""
        UPDATE usuarios 
        SET nombre = '{persona.nombre}', apellido = '{persona.apellido}', edad = {persona.edad}, 
        trabajo = '{persona.trabajo}'
        WHERE id_cedula = {persona.id_cedula}
        """
        conexion.cursor.execute(sql)
        conexion.Cerrar()

    def Mostrar_usuarios(self):
        conexion = ConexionDB()
        sql = """
        SELECT * FROM usuarios 
        """
        conexion.cursor.execute(sql)
        valores = conexion.cursor.fetchall()
        conexion.Cerrar()
        return valores
