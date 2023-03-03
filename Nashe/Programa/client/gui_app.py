import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.config(width=1024, height=480)
        self.pack()
        self.campos_pelicula()
        self.habilitar_campos()
        self.deshabilitar_campos()
        
    def campos_pelicula(self):
        #LISTA DE CAMPOS
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 15, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración: ')
        self.label_duracion.config(font=('Arial', 15, 'bold'))      #EN EL FONT PRIMERO VA EL TIPO DE LETRA, LUEGO EL TAMAÑO Y LUEGO SI QUEREMOS NEGRITA, CURSIVA, ETC.
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10) #EL PADX Y PADY SON EL PADDING, TANTO PARA LOS COSTADOS COMO ARRIBA Y ABAJO

        self.label_genre = tk.Label(self, text='Género: ')
        self.label_genre.config(font=('Arial', 15, 'bold'))
        self.label_genre.grid(row=2, column=0, padx=10, pady=10)    #PARA PODER POSICIONAR LAS LABELS DONDE QUERAMOS USAMOS EL GRID, CON ROW Y COLUMN PARA DESPLAZARLAS

        #ENTRYS DE CADA CAMPO
        self.mi_nombre = tk.StringVar(self)                             #Stringvar y textvariable para poder luego borrar los datos ya establecidos por el usuario y dejar en blanco el entry
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_duracion = tk.StringVar(self)
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, font=('Arial', 12)) #IMPORTANTE PONER EL FONT, PQ PARECE QUE SIN ESTO EL COLUMNSPAN NO FUNCIONA XD
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)  #COLUMNSPAN SIRVE PARA DECIR CUÁNTAS COLUMNAS VA A OCUPAR DE ESPACIO

        self.mi_genre = tk.StringVar(self)
        self.entry_genre = tk.Entry(self, textvariable=self.mi_genre)
        self.entry_genre.config(width=50, font=('Arial', 12))
        self.entry_genre.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #BOTONES
        self.boton_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#36D51B', cursor='hand2',
                                activebackground='#67EE50', activeforeground='#DAD5D6') #ACTIVEBACKGROUND Y FOREGROUND SIRVE COMO UN HOVER CUANDO SE PRESIONA EL BOTON, ES DECIR QUE
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)                        #AL PRESIONAR EL BOTON SE CAMBIAN SUS PROPIEDADES, ESTE CASO ES EL FONDO Y EL COLOR DE LA LETRA

        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),
                                  fg='#DAD5D6', bg='#04763F', cursor='hand2',
                                  activebackground='#14A961', activeforeground='#DAD5D6')
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),
                                   fg='#DAD5D6', bg='#C50808', cursor='hand2',
                                   activebackground='#EF2B2B', activeforeground='#DAD5D6')
        self.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)

        
    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genre.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genre.config(state='normal')
        self.boton_cancelar.config(state='normal')
        self.boton_guardar.config(state='normal')
        
    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genre.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genre.config(state='disabled')

        self.boton_cancelar.config(state='disabled')
        self.boton_guardar.config(state='disabled')

    def guardar_datos(self):
        

        self.deshabilitar_campos()







def barra_menu(root):
    barra__menu = tk.Menu(root)
    root.config(menu=barra__menu)

                #-------------
                #BARRA DE MENÚ
                #-------------
    menu_inicio = tk.Menu(barra__menu, tearoff = 0)           #tearoff es para que no aparezca ningún espacio de más en el menu que estamos creando
    barra__menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra__menu.add_cascade(label='Consultas')
    barra__menu.add_cascade(label='Configuración')
    barra__menu.add_cascade(label='Ayuda')


