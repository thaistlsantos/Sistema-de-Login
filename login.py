# importando a biblioteca: https://docs.python.org/pt-br/3/library/tk.html

from tkinter import *
from tkinter import messagebox

# criando a janela/ atribuindo uma janela a variável
janela = Tk()
janela.title('TLS Consultoria em TI - Painel de Acesso')
janela.geometry('600x300')
janela.configure('white')
# janela.resizable(width = False, twight = False) ---> ñ ser responível

janela.mainloop()
