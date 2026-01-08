import tkinter as tk
from tkinter import ttk, messagebox

class Vista_principal(tk.Frame):
    def __init__(self, root, controlador):
        super().__init__(root, width=400, height=400)
        self.root = root
        self.controlador = controlador
        self.pack(padx=20, pady=10)

        self.Formulario()
        self.botones_formulario()
        self.Tabla_usuarios()


    #contenido del formulario
    def Formulario(self):
        self.titulo = tk.Label(self, text="Formulario")
        self.titulo.config(font=("Arial", 18, "bold"))
        self.titulo.grid(row=0, column=0, pady=20, columnspan=4)

        #label de los datos
        self.label_cedula = tk.Label(self, text="Cedula: ")
        self.label_cedula.config(font=("Arial", 12, "bold"))
        self.label_cedula.grid(row=1, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=("Arial", 12, "bold"))
        self.label_nombre.grid(row=2, column=0, padx=10, pady=10)
        
        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.config(font=("Arial", 12, "bold"))
        self.label_apellido.grid(row=3, column=0, padx=10, pady=10)

        self.label_edad = tk.Label(self, text="Edad: ")
        self.label_edad.config(font=("Arial", 12, "bold"))
        self.label_edad.grid(row=4, column=0, padx=10, pady=10)

        self.label_trabajo = tk.Label(self, text="Trabajo: ")
        self.label_trabajo.config(font=("Arial", 12, "bold"))
        self.label_trabajo.grid(row=5, column=0, padx=10, pady=10)

        #entrys de los datos
        self.cedula = tk.StringVar()
        self.entry_cedula = tk.Entry(self, textvariable=self.cedula)
        self.entry_cedula.config()
        self.entry_cedula.grid(row=1, column=1, padx=10, pady=10, sticky="snew", columnspan=2)

        self.boton_buscar = tk.Button(self, text="Buscar",command=self.Buscar_usuario)
        self.boton_buscar.config(width=20, height=1, background="#1B10AE", fg="White",
                                 font=("arial", 10, "bold"))
        self.boton_buscar.grid(row=1, column=3, padx=10, pady=10)

        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config()
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="snew", columnspan=3)

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable=self.apellido)
        self.entry_apellido.config()
        self.entry_apellido.grid(row=3, column=1, padx=10, pady=10, sticky="snew", columnspan=3)

        self.edad = tk.StringVar()
        self.entry_edad = tk.Entry(self, textvariable=self.edad)
        self.entry_edad.config()
        self.entry_edad.grid(row=4, column=1, padx=10, pady=10, sticky="snew", columnspan=3)

        self.trabajo = tk.StringVar()
        self.entry_trabajo = tk.Entry(self, textvariable=self.trabajo)
        self.entry_trabajo.config()
        self.entry_trabajo.grid(row=5, column=1, padx=10, pady=10, sticky="snew", columnspan=3)

    def botones_formulario(self):
        
        self.boton_registrar = tk.Button(self, text="Registrar", command=self.Guardar_usuario)
        self.boton_registrar.config(width=20, height=2,
                                    background="#00F5FF",
                                    activebackground="#00E5EE",
                                    fg="white",
                                    activeforeground="white",
                                    font=("arial", 10, "bold"),
                                    cursor="hand2")
        self.boton_registrar.grid(row=6, column=0, padx=10, pady=20)

        self.boton_modificar = tk.Button(self, text="Modificar", command=self.Modificar_usuario)
        self.boton_modificar.config(width=20, height=2,
                                    background="#00EE76",
                                    activebackground="#00CD66",
                                    fg="white",
                                    activeforeground="white",
                                    font=("arial", 10, "bold"),
                                    cursor="hand2")
        self.boton_modificar.grid(row=6, column=1, padx=10, pady=20)

        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.Eliminar_usuario)
        self.boton_eliminar.config(width=20, height=2,
                                    background="#EE4000",
                                    activebackground="#CD3700",
                                    fg="white",
                                    activeforeground="white",
                                    font=("arial", 10, "bold"),
                                    cursor="hand2")
        self.boton_eliminar.grid(row=6, column=2, padx=10, pady=20)

        self.boton_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar_entrys)
        self.boton_limpiar.config(width=20, height=2,
                                    background="#EE4000",
                                    activebackground="#CD3700",
                                    fg="white",
                                    activeforeground="white",
                                    font=("arial", 10, "bold"),
                                    cursor="hand2")
        self.boton_limpiar.grid(row=6, column=3, padx=10, pady=20)
    
    def limpiar_entrys(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_trabajo.delete(0, tk.END)


    def Tabla_usuarios(self):
        usuarios = self.controlador.Mostrar_datos()
        columns = ("Nombre", "Apellido", "Edad", "Trabajo")
        self.table = ttk.Treeview(self, columns=columns)
        self.table.grid(row=7, column=0, columnspan=4, sticky="snew")

        #añadiendo columnas a la tabla
        self.table.heading("#0", text="Cedula")
        self.table.heading("#1", text="Nombre")
        self.table.heading("#2", text="Apellido")
        self.table.heading("#3", text="Edad")
        self.table.heading("#4", text="Trabajo")

        #configurando columnas
        self.table.column("#0", width=120, anchor="center")
        self.table.column("#1", width=150, anchor="center")
        self.table.column("#2", width=150, anchor="center")
        self.table.column("#3", width=150, anchor="center")
        self.table.column("#4", width=150, anchor="center")

        #Cargando usuarios para mostrar
        for cedula, nombre, apellido, edad, trabajo in usuarios:
            self.table.insert("", 0, text=cedula, values=(nombre, apellido, edad, trabajo))

    #------------- funciones para enviar informacion al controlador ---------

    def Buscar_usuario(self):
        cedula = self.cedula.get()
        persona = self.controlador.Buscar_usuario(cedula)
        self.limpiar_entrys()
        if not persona == None:
            for id_cedula, nombre, apelido, edad, trabajo  in persona:
                self.entry_cedula.insert(0, id_cedula)
                self.entry_nombre.insert(0, nombre)
                self.entry_apellido.insert(0, apelido)
                self.entry_edad.insert(0, edad)
                self.entry_trabajo.insert(0, trabajo)

    def Guardar_usuario(self):
        cedula = self.cedula.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        edad = self.edad.get()
        trabajo = self.trabajo.get()

        self.controlador.Guardar_datos(cedula, nombre, apellido, edad, trabajo)
        #actulizar tabla
        self.Tabla_usuarios()

    def Modificar_usuario(self):
        cedula = self.cedula.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        edad = self.edad.get()
        trabajo = self.trabajo.get()

        self.controlador.Modificar_datos(cedula, nombre, apellido, edad, trabajo)
        self.Tabla_usuarios()

    def Eliminar_usuario(self):
        cedula = self.cedula.get()
        self.controlador.Eliminar_datos(cedula)
        self.Tabla_usuarios()


    #------------- funciones que llama el controlador------------------------ 

    def Mostrar_exitoso(self, mensaje):
        titulo = "exitoso"
        messagebox.showinfo(titulo, mensaje)

    def Mostrar_error(self, mensaje):
        titulo = "Error"
        messagebox.showerror(titulo, mensaje)
        

    def Mostrar_info(self, mensaje):
        titulo = "informacion"
        messagebox.showinfo(titulo, mensaje)