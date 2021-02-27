# importando a biblioteca: https://docs.python.org/pt-br/3/library/tk.html

from tkinter import *
from tkinter import messagebox

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


janela.mainloop()
