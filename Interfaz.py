import tkinter as tk
import tkinter.ttk as ttk
import resolver


def clear():
    etiquetaF.place_forget()
    for i in tabla.get_children():
        tabla.delete(i)

def antr():
    clear()
    etiquetac0.place_forget()
    etiquetac1.place_forget()
    etiquetac2.place_forget()
    etiquetac3.place_forget()
    etiquetac4.place_forget()
    etiquetac5.place_forget()
    etiquetac6.place_forget()
    Etresultado.place_forget()

    if variable.get()=='3':
        elementosx = [x1.get(),x2.get(),x3.get(),x4.get()]
        elementosy = [y1.get(), y2.get(),y3.get(),y4.get()]

        print(elementosx)
        print(elementosy)

        deltas,datos,resultado,espaciados = resolver.inicio(elementosx,elementosy,4,px.get())

        print(datos)
        print(deltas)
        print(resultado)

    if variable.get()=='4':
        elementosx = [x1.get(), x2.get(), x3.get(), x4.get(),x5.get()]
        elementosy = [y1.get(), y2.get(), y3.get(), y4.get(),y5.get()]

        print(elementosx)
        print(elementosy)


        deltas,datos,resultado,espaciados = resolver.inicio(elementosx, elementosy, 5, px.get())
        print(datos)
        print(deltas)
        print(resultado)
    if variable.get()=='5':
        elementosx = [x1.get(), x2.get(), x3.get(), x4.get(),x5.get(),x6.get()]
        elementosy = [y1.get(), y2.get(), y3.get(), y4.get(),y5.get(),y6.get()]

        print(elementosx)
        print(elementosy)

        deltas,datos,resultado,espaciados = resolver.inicio(elementosx, elementosy, 6, px.get())
        print(datos)
        print(deltas)
        print(resultado)

    if variable.get()=='6':
        elementosx = [x1.get(), x2.get(), x3.get(), x4.get(),x5.get(),x6.get(),x7.get()]
        elementosy = [y1.get(), y2.get(), y3.get(), y4.get(),y5.get(),y6.get(),y7.get()]

        print(elementosx)
        print(elementosy)

        deltas,datos,resultado,espaciados = resolver.inicio(elementosx, elementosy, 7, px.get())
        print(datos)
        print(deltas)
        print(resultado)
    if(espaciados):
        tabla.place(x=160, y=100)
        if variable.get() == '3':
            tabla["displaycolumns"] = ("1", "2")
            tabla.insert("",index=0 ,text=deltas[0][0], values=(deltas[1][0], deltas[2][0]))
            tabla.insert("", index=1, text=deltas[0][1], values=(deltas[1][1], ''))
            tabla.insert("", index=2, text=deltas[0][2], values=('', ''))

            etiquetac0.config(text="C0 ="+str(datos[0]))
            etiquetac1.config(text="C1 ="+str(datos[1]))
            etiquetac2.config(text="C2 =" + str(datos[2]))
            etiquetac3.config(text="C3 =" + str(datos[3]))

            etiquetac0.place(x=600,y=100)
            etiquetac1.place(x=600, y=140)
            etiquetac2.place(x=600, y=180)
            etiquetac3.place(x=600, y=220)
            Etresultado.config(text="P("+str(entradapx.get())+") = "+str(resultado))
            Etresultado.place(x=180,y=400)

        if variable.get() == '4':
            tabla["displaycolumns"] = ("1", "2", "3")
            tabla.insert("", index=0, text=deltas[0][0], values=(deltas[1][0], deltas[2][0], deltas[3][0]))
            tabla.insert("", index=1, text=deltas[0][1], values=(deltas[1][1], deltas[2][1],''))
            tabla.insert("", index=2, text=deltas[0][2], values=(deltas[1][2], '',''))
            tabla.insert("", index=3, text=deltas[0][3], values=('', '',''))
            tabla.place(x=160, y=100)

            etiquetac0.config(text="C0 =" + str(datos[0]))
            etiquetac1.config(text="C1 =" + str(datos[1]))
            etiquetac2.config(text="C2 =" + str(datos[2]))
            etiquetac3.config(text="C3 =" + str(datos[3]))
            etiquetac4.config(text="C4 =" + str(datos[4]))

            etiquetac0.place(x=600, y=100)
            etiquetac1.place(x=600, y=140)
            etiquetac2.place(x=600, y=180)
            etiquetac3.place(x=600, y=220)
            etiquetac4.place(x=600, y=260)

            Etresultado.config(text="P(" + str(entradapx.get()) + ") = " + str(resultado))
            Etresultado.place(x=180, y=400)

        if variable.get() == '5':
            tabla["displaycolumns"] = ("1", "2", "3", "4")
            tabla.insert("", index=0, text=deltas[0][0], values=(deltas[1][0], deltas[2][0], deltas[3][0],deltas[4][0]))
            tabla.insert("", index=1, text=deltas[0][1], values=(deltas[1][1], deltas[2][1],deltas[3][1] ,''))
            tabla.insert("", index=2, text=deltas[0][2], values=(deltas[1][2], deltas[2][2],'', ''))
            tabla.insert("", index=3, text=deltas[0][3], values=(deltas[1][3],'', '', ''))
            tabla.insert("", index=4, text=deltas[0][4], values=('', '', '', ''))

            etiquetac0.config(text="C0 =" + str(datos[0]))
            etiquetac1.config(text="C1 =" + str(datos[1]))
            etiquetac2.config(text="C2 =" + str(datos[2]))
            etiquetac3.config(text="C3 =" + str(datos[3]))
            etiquetac4.config(text="C4 =" + str(datos[4]))
            etiquetac5.config(text="C5 =" + str(datos[5]))

            etiquetac0.place(x=600, y=100)
            etiquetac1.place(x=600, y=140)
            etiquetac2.place(x=600, y=180)
            etiquetac3.place(x=600, y=220)
            etiquetac4.place(x=600, y=260)
            etiquetac5.place(x=600, y=300)

            Etresultado.config(text="P(" + str(entradapx.get()) + ") = " + str(resultado))
            Etresultado.place(x=180, y=400)
        if variable.get() == '6':
            tabla["displaycolumns"] = ("1", "2", "3", "4", "5")

            tabla.insert("", index=0, text=deltas[0][0],
                         values=(deltas[1][0], deltas[2][0], deltas[3][0], deltas[4][0], deltas[5][0]))
            tabla.insert("", index=1, text=deltas[0][1], values=(deltas[1][1], deltas[2][1], deltas[3][1],deltas[4][1], ''))
            tabla.insert("", index=2, text=deltas[0][2], values=(deltas[1][2], deltas[2][2],deltas[3][2] ,'', ''))
            tabla.insert("", index=3, text=deltas[0][3], values=(deltas[1][3], deltas[2][3],'', '', ''))
            tabla.insert("", index=4, text=deltas[0][4], values=(deltas[1][4],'', '', '', ''))
            tabla.insert("", index=5, text=deltas[0][4], values=('', '', '', '', ''))

            etiquetac0.config(text="C0 =" + str(datos[0]))
            etiquetac1.config(text="C1 =" + str(datos[1]))
            etiquetac2.config(text="C2 =" + str(datos[2]))
            etiquetac3.config(text="C3 =" + str(datos[3]))
            etiquetac4.config(text="C4 =" + str(datos[4]))
            etiquetac5.config(text="C5 =" + str(datos[5]))
            etiquetac6.config(text="C6 =" + str(datos[6]))

            etiquetac0.place(x=600, y=100)
            etiquetac1.place(x=600, y=140)
            etiquetac2.place(x=600, y=180)
            etiquetac3.place(x=600, y=220)
            etiquetac4.place(x=600, y=260)
            etiquetac5.place(x=600, y=300)
            etiquetac6.place(x=600, y=340)

            Etresultado.config(text="P(" + str(entradapx.get()) + ") = " + str(resultado))
            Etresultado.place(x=180, y=400)

    else:
        etiquetaF.place(x=180, y=300)




#Creamos la ventana

root = tk.Tk() #creamos la ventana
root.title("Analisis Numerico")
root.resizable(0,0)
root.geometry("800x500")

#variable de entrada
x1 = tk.DoubleVar()
x2 = tk.DoubleVar()
x3 = tk.DoubleVar()
x4 = tk.DoubleVar()
x5 = tk.DoubleVar()
x6 = tk.DoubleVar()
x7= tk.DoubleVar()

y1 = tk.DoubleVar()
y2 = tk.DoubleVar()
y3 = tk.DoubleVar()
y4 = tk.DoubleVar()
y5 = tk.DoubleVar()
y6 = tk.DoubleVar()
y7= tk.DoubleVar()

px = tk.DoubleVar()
def callback(*args):
    if variable.get()=='3':
        entradax5.place_forget()
        entradax6.place_forget()
        entradax7.place_forget()
        entraday5.place_forget()
        entraday6.place_forget()
        entraday7.place_forget()
    if variable.get()=='4':
        entradax5.place(x=20,y=290)
        entradax6.place_forget()
        entradax7.place_forget()
        entraday5.place(x=80, y=290)
        entraday6.place_forget()
        entraday7.place_forget()
    if variable.get()=='5':
        entradax5.place(x=20, y=290)
        entradax6.place(x=20, y=330)
        entradax7.place_forget()
        entraday5.place(x=80, y=290)
        entraday6.place(x=80, y=330)
        entraday7.place_forget()
    if variable.get()=='6':
        entradax5.place(x=20, y=290)
        entradax6.place(x=20, y=330)
        entradax7.place(x=20, y=370)
        entraday5.place(x=80, y=290)
        entraday6.place(x=80, y=330)
        entraday7.place(x=80, y=370)


grados=[3,4,5,6]

variable = tk.StringVar(root)
variable.set(grados[0])



etiqueta1 = tk.Label(text="Inerpolacion de Newton con datos igualmente espaciados", font=("Arial", 20))
etiqueta1.place(x=80,y=10)
etiqueta2 = tk.Label(text="X", font=("Arial", 15))
etiqueta2.place(x=20,y=100)
etiqueta3= tk.Label(text="Y", font=("Arial", 15))
etiqueta3.place(x=80, y=100)


etiquetac0= tk.Label(text="C0", font=("Arial", 12))

etiquetac1= tk.Label(text="C1", font=("Arial", 12))

etiquetac2= tk.Label(text="C2", font=("Arial", 12))

etiquetac3= tk.Label(text="C3", font=("Arial", 12))

etiquetac4= tk.Label(text="C4", font=("Arial", 12))

etiquetac5= tk.Label(text="C5", font=("Arial", 12))

etiquetac6= tk.Label(text="C6", font=("Arial", 12))

Etresultado= tk.Label(text="P(x)", font=("Arial", 12))


entradax1 = tk.Entry(width=6,textvariable=x1,font=("Arial", 14))
entradax2 = tk.Entry(width=6,textvariable=x2,font=("Arial", 14))
entradax3 = tk.Entry(width=6,textvariable=x3,font=("Arial", 14))
entradax4 = tk.Entry(width=6,textvariable=x4,font=("Arial", 14))


entradax6 = tk.Entry(width=6,textvariable=x6,font=("Arial", 14))
entradax5 = tk.Entry(width=6,textvariable=x5,font=("Arial", 14))
entradax7 = tk.Entry(width=6,textvariable=x7,font=("Arial", 14))

entraday1 = tk.Entry(width=6,textvariable=y1,font=("Arial", 14))
entraday2 = tk.Entry(width=6,textvariable=y2,font=("Arial", 14))
entraday3 = tk.Entry(width=6,textvariable=y3,font=("Arial", 14))
entraday4 = tk.Entry(width=6,textvariable=y4,font=("Arial", 14))


entraday6 = tk.Entry(width=6,textvariable=y6,font=("Arial", 14))
entraday5 = tk.Entry(width=6,textvariable=y5,font=("Arial", 14))
entraday7 = tk.Entry(width=6,textvariable=y7,font=("Arial", 14))


entradax1.place(x=20, y=130)
entradax2.place(x=20, y=170)
entradax3.place(x=20, y=210)
entradax4.place(x=20,y=250)

entraday1.place(x=80, y=130)
entraday2.place(x=80, y=170)
entraday3.place(x=80, y=210)
entraday4.place(x=80,y=250)

opcion=tk.OptionMenu(root,variable,*grados)
opcion.config(width=2, font=('Helvetica', 12))
opcion.pack()
opcion.place(x=320,y=70)

etiqueta3 = tk.Label(text="n:", font=("Arial", 12))
etiqueta3.place(x=300,y=70)
variable.trace("w", callback)

etiquetapx = tk.Label(text="P(x) =", font=("Arial", 12))
etiquetapx.place(x=50,y=400)
entradapx = tk.Entry(width=4,textvariable=px,font=("Arial", 14))
entradapx.place(x=100, y=400)

boton1 = tk.Button(text="Resolver",command=antr)
boton1.place(x=20,y=450)

tabla = ttk.Treeview(root, columns=("1", "2", "3", "4", "5"))
tabla.column('#0', width=70)
tabla.column('1', width=70)
tabla.column('2', width=70)
tabla.column('3', width=70)
tabla.column('4', width=70)
tabla.column('5', width=70)

tabla.heading("#0", text="\u0394y0")
tabla.heading("1", text="\u03942y0")
tabla.heading("2", text="\u03943y0")
tabla.heading("3", text="\u03944y0")
tabla.heading("4", text="\u03945y0")
tabla.heading("5", text="\u03946y0")

etiquetaF= tk.Label(text="NO ESTAN IGUALMENTE ESPACIADOS", font=("Arial", 15))

root.mainloop()