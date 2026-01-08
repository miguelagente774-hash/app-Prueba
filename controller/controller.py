#necesario importar los archivos models y view
from view.view import Vista_principal
from models.models import Modelo_usuarios, Persona

class Controlador_principal:
    def __init__(self, root):
        #inicializar de modelo y vista
        self.modelo = Modelo_usuarios()
        self.vista = Vista_principal(root ,self)

    def Buscar_usuario(self, id_cedula):
        try:
            verificar_id = self.modelo.Verficar_cedula_existe(id_cedula)
            if verificar_id:   
                valores = self.modelo.Buscar_usuario(id_cedula)
                return valores
            elif id_cedula == "":
                self.vista.Mostrar_info("ingrese la cedula a buscar")

            else:
                self.vista.Mostrar_info("Usuario no encontrado")

        except:
            self.vista.Mostrar_error("Por favor Introdusca la cedula a buscar!!!")

    def Guardar_datos(self, id_cedula, nombre, apellido, edad, trabajo):
            try:

                persona = Persona(id_cedula, nombre, apellido, edad, trabajo)
                resultado = self.modelo.Verficar_cedula_existe(persona.id_cedula)
                if resultado:
                    
                    self.vista.Mostrar_info("Cedula ya registrada")
                
                else:
                    self.modelo.Guardar_usuario(persona)
                    self.vista.Mostrar_exitoso(f"EL registro del usuario {persona.nombre} fue exitoso")
                    self.vista.limpiar_entrys()
            
            except:
                 self.vista.Mostrar_error("Nose pudo registrar al usuario")
    
    def Eliminar_datos(self, id_cedula):
        try:
            resultado = self.modelo.eliminar_usuario(id_cedula)
            if resultado:
                self.vista.Mostrar_exitoso("Usuario eliminado exitosamente")
                self.vista.limpiar_entrys()
            elif id_cedula == "":
                self.vista.Mostrar_info("Por favor ingrese la cedula del usuario a eliminar")
        except:
            self.vista.Mostrar_error("Verifique los datos del usuario a eliminar")

    def Modificar_datos(self, cedula, nombre, apellido, edad, trabajo):
        persona = Persona(cedula, nombre, apellido, edad, trabajo)
        try:
            verificar_cedula = self.modelo.Verficar_cedula_existe(persona.id_cedula)
            
            if verificar_cedula:
                self.modelo.Modificar_datos_usuario(persona)
                print(verificar_cedula)
                self.vista.Mostrar_exitoso("Usario actualizado correctamente")
                self.vista.limpiar_entrys()
            elif persona.id_cedula == "":
                self.vista.Mostrar_info("Por favor ingrese la cedula del usuario a modificar valores")
        except:
            self.vista.Mostrar_error("Este usuario no esta registrado")

    def Mostrar_datos(self):
        try:
            valores = self.modelo.Mostrar_usuarios()
            return valores
        except:
            self.vista.Mostrar_error("Error al cargar los usuarios")