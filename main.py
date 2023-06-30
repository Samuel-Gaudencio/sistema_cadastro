from pymongo import MongoClient
import datetime
from tkinter import *

cliente = MongoClient('mongodb://127.0.0.1:27017/')

db = cliente.dbapp

conexao = db.students


def data():
    date = datetime.date.today()
    date = datetime.datetime.strftime(date, '%d-%m-%Y')
    return date


def margin(altura):
    margem = Canvas(root, bg='#1d1d1d', width=600, height=altura, relief='ridge', highlightthickness=0)
    margem.pack()


def cadastrar():
    casdastro = conexao.insert_one({'nome': e_nome.get().title(), 'sobrenome': e_sobre.get().title(), 'curso': e_curso.get().title(),
                                    'turno': e_turno.get().title(), 'data_matricula': data()})
    e_nome.delete(0, END)
    e_sobre.delete(0, END)
    e_curso.delete(0, END)
    e_turno.delete(0, END)
    try:
        label_confi.configure(text='Cadastro realizado com sucesso!!')
    except:
        label_confi.configure(text='Não foi possivel cadastrar...')

    label_confi.grid(row=8, column=0, columnspan=2)


root = Tk()
root.geometry('400x300')
root.configure(bg='#1d1d1d')
root.maxsize(400, 300)
root.minsize(400, 300)


title = Label(root, text='Cadastro De Alunos', bg='#1d1d1d', fg='#fff', font=('Montserrat', 20, 'bold'))
title.grid(row=0, column=0, columnspan=2)

label_nome = Label(root, text='Nome: ', bg='#1d1d1d', fg='#fff', font=('Montserrat', 12, 'bold'), pady=10)
label_nome.grid(row=1, column=0)

e_nome = Entry(root, bg='#2d2d2d', font=('Montserrat', 12), fg='#fff', relief=FLAT, justify=CENTER, borderwidth=4)
e_nome.grid(row=1, column=1)

label_sobre = Label(root, text='Sobrenome: ', bg='#1d1d1d', fg='#fff', font=('Montserrat', 12, 'bold'))
label_sobre.grid(row=2, column=0)

e_sobre = Entry(root, bg='#2d2d2d', font=('Montserrat', 12), fg='#fff', relief=FLAT, justify=CENTER, borderwidth=4)
e_sobre.grid(row=2, column=1)

label_curso = Label(root, text='Curso: ', bg='#1d1d1d', fg='#fff', font=('Montserrat', 12, 'bold'), pady=10)
label_curso.grid(row=3, column=0)

e_curso = Entry(root, bg='#2d2d2d', font=('Montserrat', 12), fg='#fff', relief=FLAT, justify=CENTER, borderwidth=4)
e_curso.grid(row=3, column=1)

label_turno = Label(root, text='Turno: ', bg='#1d1d1d', fg='#fff', font=('Montserrat', 12, 'bold'))
label_turno.grid(row=4, column=0)

e_turno = Entry(root, bg='#2d2d2d', font=('Montserrat', 12), fg='#fff', relief=FLAT, justify=CENTER, borderwidth=4)
e_turno.grid(row=4, column=1)

button_cadas = Button(root, text='Cadastrar', bg='#C69749', fg="#FFF", font=('Montserrat', 12, 'bold'), relief=FLAT,
                      activebackground='#C69749', activeforeground="#fff", command=cadastrar, padx=20)
padding = Canvas(root, bg='#1d1d1d', width=400, height=20, borderwidth=0, highlightthickness=0)
padding.grid(row=5, columnspan=2, column=0)
button_cadas.grid(row=6, column=0, columnspan=2)
padding.grid(row=7, column=0, columnspan=2)
label_confi = Label(root, text='', bg='#1d1d1d', fg='#fff', font=('Montserrat', 14, 'bold'), padx=10)

root.mainloop()
