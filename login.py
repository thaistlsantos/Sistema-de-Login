# importando a biblioteca: https://docs.python.org/pt-br/3/library/tk.html

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# --------- criando a janela/ atribuindo uma janela a uma variável
janela = Tk()
janela.title('TLS Consultoria em TI - Painel de Acesso')
janela.geometry('600x300')
janela.configure(background='white')
janela.resizable(width=False, height=False)

# --------- carregar as imagens
logo = PhotoImage(file='icons/logo.png')

# --------- criação dos WIDGETS
# --------- lado esquerdo
LeftFrame = Frame(janela, width=200, height=300, bg='#BDE9D4', relief='raise')
LeftFrame.pack(side=LEFT)

# --------- lado direito com diminuição de pixel para mostrar uma divisão 
RightFrame = Frame(janela, width=395, height=300, bg='#BDE9D4', relief='raise')
RightFrame.pack(side=RIGHT)


LogoLabel = Label(LeftFrame, image=logo, bg='#BDE9D4')
LogoLabel.place(x=0, y=50)

# ------ criação de usuario
UserLabel = Label(RightFrame, text="Login: ", font=("Britannic Bold", 15), bg='#BDE9D4', fg='#737373')
UserLabel.place(x=30, y=76)

UserEntry = ttk.Entry(RightFrame, width = 30)
UserEntry.place(x=150, y=80)

PassLabel = Label(RightFrame, text="Password: ", font=("Britannic Bold", 15), bg='#BDE9D4', fg='#737373')
PassLabel.place(x=15, y=116)

PassEntry = ttk.Entry(RightFrame, width = 30)
PassEntry.place(x=150, y=120)


janela.mainloop()
