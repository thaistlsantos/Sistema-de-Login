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
janela.iconbitmap(default='icons/Logoicon.ico')
# janela.attributes('-alpha', 0.9)----- transparencia se desejar.

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
UserLabel = Label(RightFrame, text="Usuário: ", font=("Britannic Bold", 15), bg='#BDE9D4', fg='#737373')
UserLabel.place(x=40, y=76)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=80)

PassLabel = Label(RightFrame, text="Senha: ", font=("Britannic Bold", 15), bg='#BDE9D4', fg='#737373')
PassLabel.place(x=47, y=113)

PassEntry = ttk.Entry(RightFrame, width=30, show='*')
PassEntry.place(x=150, y=120)

# ---------- Criação de botão
LoginButton = ttk.Button(RightFrame, text='Entrar', width=30)
LoginButton.place(x=100, y=180)

def Register():
    # removendo os widgtes de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # inserindo wigtes de cadastro
    NomeLabel = Label(RightFrame, text="Nome: ", font=("Britannic Bold", 15), bg='#BDE9D4', fg='#737373')
    NomeLabel.place(x=47, y=0)

    NomeEntry = Entry(RightFrame, width=30)
    NomeEntry.place(x=150, y=5)

    EmailLabel = Label(RightFrame, text="E-mail: ", font=("Britannic Bold", 15), bg='#BDE9D4', fg='#737373')
    EmailLabel.place(x=47, y=38)

    EmailEntry = Entry(RightFrame, width=30)
    EmailEntry.place(x=150, y=42)

    Register = ttk.Button(RightFrame, text='Cadastrar', width=30)
    Register.place(x=100, y=180)


    def BacktoLogin():
        #removendo o wigtes de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        # trazendo os widgtes de login
        LoginButton.place(x=100, y=180)
        RegisterButton.place(x=100, y=220)

    Back = ttk.Button(RightFrame, text='Voltar', width=30, command= BacktoLogin)
    Back.place(x=100, y=220)
    

RegisterButton = ttk.Button(RightFrame, text='Registrar', width=30, command= Register)
RegisterButton.place(x=100, y=220)






janela.mainloop()
