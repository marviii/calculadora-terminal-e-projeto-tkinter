#import
from tkinter import *
from tkinter import ttk

#criando janela
window = Tk()
window.title('projeto calculadora')
window.geometry('290x410')
window.config(background='#000000')

#frame para dividir a janela em 2 partes, visor e teclado
frame_display = Frame(window, width=290, height=70, background='#82b58e')
frame_display.grid(row=0,column=0)

frame_teclas = Frame(window, width=290, height=350, background='#212020')
frame_teclas.grid(row=1,column=0)

#variavel para armazenar todos valores para o eval
todos_valores = ''

#configurando visor usando label
valor_texto = StringVar()


#função para passar valores para tela
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

#função para calcular os valores armazenados com eval
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

#função para limpar a tela com a tecla C
def limpar():
    global todos_valores #global para atualizar em todas funçoes que usam todos_valores
    todos_valores = ''
    valor_texto.set('')

#stringvar e textvariable=valor_texto para poder alterar o texto do label como string
app_label = Label(frame_display, textvariable=valor_texto, width=16, height= 2, padx=0, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 23'), bg='#82b58e')
app_label.place(x=0, y=0)



#teclas
b1 = Button(frame_teclas, command=limpar, text='C', width=11, height=2, bg='#db3548', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=3, y=3)
b2 = Button(frame_teclas, command=lambda: entrar_valores('%'), text='%', width=5, height=2, bg='#e36b2b', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=147, y=3)
b3 = Button(frame_teclas, command=lambda: entrar_valores('/'), text='/', width=5, height=2, bg='#e36b2b', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=219, y=3)

b4 = Button(frame_teclas, command=lambda: entrar_valores('7'), text='7', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=3, y=70)
b5 = Button(frame_teclas, command=lambda: entrar_valores('8'), text='8', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=75, y=70)
b6 = Button(frame_teclas, command=lambda: entrar_valores('9'), text='9', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=147, y=70)
b7 = Button(frame_teclas, command=lambda: entrar_valores('*'), text='*', width=5, height=2, bg='#e36b2b', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=219, y=70)

b8 = Button(frame_teclas, command=lambda: entrar_valores('4'), text='4', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=3, y=138)
b9 = Button(frame_teclas, command=lambda: entrar_valores('5'), text='5', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=75, y=138)
b10 = Button(frame_teclas, command=lambda: entrar_valores('6'), text='6', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=147, y=138)
b11 = Button(frame_teclas, command=lambda: entrar_valores('-'), text='-', width=5, height=2, bg='#e36b2b', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=219, y=138)

b12 = Button(frame_teclas, command=lambda: entrar_valores('3'), text='3', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=3, y=206)
b13 = Button(frame_teclas, command=lambda: entrar_valores('2'), text='2', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=75, y=206)
b14 = Button(frame_teclas, command=lambda: entrar_valores('1'), text='1', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=147, y=206)
b15 = Button(frame_teclas, command=lambda: entrar_valores('+'), text='+', width=5, height=2, bg='#e36b2b', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=219, y=206)

b16 = Button(frame_teclas, command=lambda: entrar_valores('0'), text='0', width=11, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=3, y=274)
b17 = Button(frame_teclas, command=lambda: entrar_valores('.'), text='.', width=5, height=2, bg='#cccbca', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=147, y=274)
b18 = Button(frame_teclas, command=calcular, text='=', width=5, height=2, bg='#e36b2b', font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=219, y=274)

#executar janela
window.mainloop()