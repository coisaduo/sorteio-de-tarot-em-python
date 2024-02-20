import random
import os
from tkinter import *
from tkinter import ttk
from random import sample
from PIL import Image, ImageTk

# tela inicial/menu
janela = Tk()
janela.title("Chaos")

# definindo tamanho do menu
largura_janela = 700
altura_janela = 300
janela.geometry(f"{largura_janela}x{altura_janela}")

# Criando um frame para conter as cartas
cartas_frame = ttk.Frame(janela)
cartas_frame.pack()

# Configurando o layout da grade para 3x3
for i in range(3):
    cartas_frame.columnconfigure(i, weight=1)
    cartas_frame.rowconfigure(i, weight=1)

# numero de cartas
num_cartas = 22

# Arcanos maiores do tarot
arcanos = {
    1: 'O Louco',
    2: 'O Mago',
    3: 'A Sacerdotista',
    4: 'A Imperatriz',
    5: 'O Imperador',
    6: 'O Hierofante',
    7: 'Os Enamorados',
    8: 'O Carro',
    9: 'A Força',
    10: 'O Eremita',
    11: 'A Roda da Fortuna',
    12: 'A Justiça',
    13: 'O Enforcado',
    14: 'A Morte',
    15: 'A Temperança',
    16: 'O Diabo',
    17: 'A Torre',
    18: 'A Estrela',
    19: 'A Lua',
    20: 'O Sol',
    21: 'O Julgamento',
    22: 'O Mundo'
}

# dicionário com os caminhos das imagens das cartas
diretorio_cartas = 'C:\\Users\\COMPACO25\\Documents\\python\\baraio\\imagens'
cartas = {}
for i in range(num_cartas):
    caminho_imagem = os.path.join(diretorio_cartas, f"{i}.jpg")
    cartas[f'Carta {i+1}'] = caminho_imagem

# lista pra armazenar a imagem das cartas
imagens_cartas = []

# carrega as imagens da carta
for nome_arquivo in cartas.values():
    imagem = Image.open(nome_arquivo)
    imagem = imagem.resize((100, 180))
    imagem = ImageTk.PhotoImage(imagem)
    imagens_cartas.append(imagem)
                                  
# Rótulos para as cartas
texto_cartas = []

# Sorteando as cartas e exibindo na grade 3x3
def sortear_carta(quantidade=9):
    #random.shuffle(list(arcanos.keys()))
    cartas_selecionadas = sample(list(arcanos.keys()), quantidade)

    # Limpando rótulos anteriores, se houver
    for texto in texto_cartas:
        texto.destroy()

    # Exibindo as cartas na grade 3x3
    for i, numero in enumerate(cartas_selecionadas):
        nome_arcano = arcanos[numero]
        caminho_imagem = cartas[f'Carta {numero}']
        if i < 6:
            texto = Label(cartas_frame, text=f"{nome_arcano} ({numero})", font=("Consolas", 16), anchor='center')
            texto.grid(row=i // 3, column=i % 3)
        else:
            texto = Label(cartas_frame, text=f"{nome_arcano} ({numero})", font=("Consolas", 16), anchor='center')
            texto.grid(row=2, column=1 + (i - 6))
        texto_cartas.append(texto)

        # exibindo imagem da carta
        imagem_carta = imagens_cartas[numero - 1]
        label_imagem = Label(cartas_frame, image=imagem_carta)
        label_imagem.grid(row=i // 3, column=i % 3)  # Definindo a posição da imagem dentro do loop
        texto_cartas.append(label_imagem)

# Botões de sorteio
botao_simples = Button(janela, text="Arcano Primordial", command=lambda: sortear_carta(1))
botao_trindade = Button(janela, text="Trindade Arcana", command=lambda: sortear_carta(3))
botao_chaos = Button(janela, text="Círculo Arcano", command=lambda: sortear_carta(7))

# posicionando os botões pra ficarem mais pra baixo
botao_simples.pack(side=BOTTOM, pady=15)
botao_trindade.pack(side=BOTTOM, pady=15)
botao_chaos.pack(side=BOTTOM, pady=15)

# Executando a janela principal
janela.mainloop()
