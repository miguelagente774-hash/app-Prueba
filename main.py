#prueba de que si se suben los cambios a git
#segunda prueba
#prueba 3
#pruba numero 4
import tkinter as tk
from controller.controller import Controlador_principal

class Miapp():
    def __init__(self, root):
        self.root = root
        self.root.title("Mi App")
        self.root.resizable(0, 0)

        Controlador_principal(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = Miapp(root)
    root.mainloop()
