
import tkinter as tk  # com el * estamos importando absolutamnente todo

raiz = tk.Tk() # aca le ponemos nombre a la funcion Tk() que es tkinter
raiz.title('ventana de prueva ')
raiz.geometry('650x350')
raiz.config(bg='blue')

miframe= Frame()
miframe.pack(fill= 'x', expand= 'True')#pack es para compactar
miframe.config(bg='red')
miframe.config(width='650', height=350)
miframe.config(bd=15)#medida del marco
miframe.config(relief="raised")#tipo de marco
#miframe.config(cursor='hand2')


# miframe.pack()

milabel=Label(raiz, text='hola mundo', fg='red', font=('Comic Sanns MS', 19))
milabel.pack()
#milabel=(miframe, image=miimagen)
milabel.place(x=400, y=200) #podemos evitar crear un misma variable y solo la subimosa la linea 19
milabel.config(bg='white')
milabel.config(cursor='hand2')
milabel.config(relief='raised')
milabel.config(bd=10)







raiz.mainloop() # con el mainloop es nuestra interfaz grafic

