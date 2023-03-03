import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()                      #CREA LA VENTANA DEL PROGRAMA
    root.title('Catálogo de películas')
    #root.iconbitmap('"RUTA"') --> Esto es para añadirle un ícono a la parte de arriba al programa
    #root.resizable(0, 0)  --> para el tamaño de la ventana. 0 es falso, por lo q no se podra ensanchar o alargar
                                                            #1 es verdadero
    app = Frame(root = root)

    barra_menu(root)

    app.mainloop()

if __name__ == '__main__':
    main()
