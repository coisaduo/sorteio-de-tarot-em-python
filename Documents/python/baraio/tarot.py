import random
from tkinter import *
from tkinter import ttk

# Janela inicial
janela = Tk()
janela.title("Chaos")

# Criando um frame para conter as cartas
cartas_frame = ttk.Frame(janela)
cartas_frame.pack()

# Configurando o layout da grade para 3x3
for i in range(3):
    cartas_frame.columnconfigure(i, weight=1)
    cartas_frame.rowconfigure(i, weight=1)

# Arcanos maiores do tarot
arcanos = {
    'O Louco':'(   )',
    'O Mago':'(I)',
    'A Sacerdotista':'(II)',
    'A Imperatriz':'(III)',
    'O Imperador':'(IV)',
    'O Hierofante':'(V)',
    'Os Enamorados':'(VI)',
    'O Carro':'(VII)',
    'A Força':'(VIII)',
    'O Eremita':'(IX)',
    'A Roda da Fortuna':'(X)',
    'A Justiça':'(XI)',
    'O Enforcado':'(XII)',
    'A Morte':'(XIII)',
    'A Temperança':'(XIV)',
    'O Diabo':'(XV)',
    'A Torre':'(XVI)',
    'A Estrela':'(XVII)',
    'A Lua':'(XVIII)',
    'O Sol':'(XIX)',
    'O Julgamento':'(XX)',
    'O Mundo':'(XXI)'
}

# Rótulos para as cartas
texto_cartas = []

# Sorteando as cartas e exibindo na grade 3x3
def sortear_carta(quantidade=9):
    random.shuffle(list(arcanos.keys()))
    cartas_selecionadas = list(arcanos.items())[:quantidade]

    # Limpando rótulos anteriores, se houver
    for texto in texto_cartas:
        texto.destroy()

    # Exibindo as cartas na grade 3x3
    for i, (carta, numero) in enumerate(cartas_selecionadas):
        texto = Label(cartas_frame, text=f"{carta} {numero}", font=("Consolas", 16))
        texto.grid(row=i // 3, column=i % 3)
        texto_cartas.append(texto)

# Botões de sorteio
botao_simples = Button(janela, text="Simples", command=lambda: sortear_carta(1))
botao_trindade = Button(janela, text="Trindade", command=lambda: sortear_carta(3))
botao_chaos = Button(janela, text="Chaos", command=lambda: sortear_carta(9))

# Posicionando os botões
botao_simples.pack()
botao_trindade.pack()
botao_chaos.pack()

# Executando a janela principal
janela.mainloop()
