from tkinter import *

root = Tk()
root.title("Calculadora")
root.geometry("200x290")
root.resizable(False, False)

e = Entry(root, width=20, borderwidth=2, font=14, justify='right')
e.grid(row=1, columnspan=3)
e.get()

space = Label(root, text=" ")
space.grid(row=0, column=2, columnspan=3)

limpo = "                                                                                                       "
l = Label(root, text=limpo)
l.place(relx=1,
        rely=0.0,
        anchor='ne')

def numero1():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "1")

def numero2():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "2")

def numero3():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "3")

def numero4():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "4")

def numero5():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "5")

def numero6():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "6")

def numero7():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "7")

def numero8():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "8")

def numero9():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "9")

def numero0():
    final = e.get()
    e.delete(0, 'end')
    e.insert(0, final + "0")

def limpar():
    e.delete(0, 'end')
    l = Label(root, text=limpo)
    l.place(relx = 1, rely = 0.0, anchor ='ne')

def somar():
    global operador
    operador = "soma"
    primeiro_numero = e.get()
    global p_num
    p_num = float(primeiro_numero)
    e.delete(0, 'end')

    l = Label(root, text=limpo)
    l.place(relx = 1, rely = 0.0, anchor ='ne')

    preview = Label(root, fg="#696969", text=str(primeiro_numero)+" +")
    preview.place(relx = 1.0, rely = 0.0, anchor ='ne')



def dividir():
    global operador
    operador = "divisao"
    primeiro_numero = e.get()
    global p_num
    p_num = float(primeiro_numero)
    e.delete(0, 'end')

    l = Label(root, text=limpo)
    l.place(relx = 1, rely = 0.0, anchor ='ne')

    preview = Label(root, fg="#696969", text=str(primeiro_numero)+" /")
    preview.place(relx = 1.0, rely = 0.0, anchor ='ne')

def subtrair():
    global operador
    operador = "subtracao"
    primeiro_numero = e.get()
    global p_num
    p_num = float(primeiro_numero)
    e.delete(0, 'end')

    l = Label(root, text=limpo)
    l.place(relx = 1, rely = 0.0, anchor ='ne')

    preview = Label(root, fg="#696969", text=str(primeiro_numero)+" -")
    preview.place(relx = 1.0, rely = 0.0, anchor ='ne')

def multiplicar():
    global operador
    operador = "multiplicacao"
    primeiro_numero = e.get()
    global p_num
    p_num = float(primeiro_numero)
    e.delete(0, 'end')

    l = Label(root, text=limpo)
    l.place(relx = 1, rely = 0.0, anchor ='ne')

    preview = Label(root, fg="#696969", text=str(primeiro_numero)+" *")
    preview.place(relx = 1.0, rely = 0.0, anchor ='ne')

def result():
    segundo_numero = float(e.get())
    e.delete(0, 'end')

    if operador == "soma":
        op = "+"
        resposta = (p_num + segundo_numero)
    if operador == "multiplicacao":
        op = "*"
        resposta = (p_num * segundo_numero)
    if operador == "subtracao":
        op = "-"
        resposta = (p_num - segundo_numero)
    if operador == "divisao":
        op = "/"
        resposta = (p_num / segundo_numero)

    e.insert(0, resposta)


    l.place(relx = 1, rely = 0.0, anchor ='ne')

    historico = Label(root, fg="#696969", text=str(p_num) + " " + str(op) + " " + str(segundo_numero) + " =")
    historico.place(relx = 1.0, rely = 0.0, anchor ='ne')

Num1 = Button(root, text="1", command=numero1, width=8, height=2).grid(row=2, column=0)
Num2 = Button(root, text="2", command=numero2, width=8, height=2).grid(row=2, column=1)
Num3 = Button(root, text="3", command=numero3, width=8, height=2).grid(row=2, column=2)
Num4 = Button(root, text="4", command=numero4, width=8, height=2).grid(row=3, column=0)
Num5 = Button(root, text="5", command=numero5, width=8, height=2).grid(row=3, column=1)
Num6 = Button(root, text="6", command=numero6, width=8, height=2).grid(row=3, column=2)
Num7 = Button(root, text="7", command=numero7, width=8, height=2).grid(row=4, column=0)
Num8 = Button(root, text="8", command=numero8, width=8, height=2).grid(row=4, column=1)
Num9 = Button(root, text="9", command=numero9, width=8, height=2).grid(row=4, column=2)
Num0 = Button(root, text="0", command=numero0, width=8, height=2).grid(row=5, column=0)

Somar = Button(root, text="+", command = somar, width=8, height=2).grid(row=6, column=0)
Dividir = Button(root, text="/", command = dividir, width=8, height=2).grid(row=7, column=0)
Multiplicar = Button(root, text="*", command = multiplicar, width=8, height=2).grid(row=7, column=1)
Subtrair = Button(root, text="-", command = subtrair, width=8, height=2).grid(row=7, column=2)

Limpar = Button(root, text="Limpar", command=limpar, width=18, height=2).grid(row=5, column=1, columnspan=2)
Resultado = Button(root, text="=", command = result, width=18, height=2).grid(row=6, column=1, columnspan=2)

root.mainloop()
