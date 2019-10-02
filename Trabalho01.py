import numpy as np
import math
import matplotlib.pyplot as plt
from statistics import mode 
import pandas as pd

K = 5

#Leitura e divisão dos dados
dados=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', delimiter=",")
numeroLinhas = dados.shape[0]
numeroColunas = dados.shape[1]
quantidadeTeste = np.int(numeroLinhas * 0.7)
quantidadeTreino = numeroLinhas - quantidadeTeste
tabelaTreino = dados.iloc[0:quantidadeTeste]
tabelaTeste = dados.iloc[quantidadeTeste:]

#Classificação
erros = 0
for linhaTeste in range(quantidadeTeste - 1):
    distancias = []
    for linhaTreino in range(quantidadeTreino - 1):
        distancia = 0
        for prop in range(1, numeroColunas - 2):
            valorTesteNaPropriedadeAtual = float(tabelaTeste.iloc[linhaTeste, prop] if tabelaTeste.iloc[linhaTeste, prop] != '?' else 999999)
            valorTreinoNaPropriedadeAtual = float(tabelaTreino.iloc[linhaTreino, prop] if tabelaTreino.iloc[linhaTreino, prop] != '?' else -999999)
            distancia += math.pow(valorTesteNaPropriedadeAtual - valorTreinoNaPropriedadeAtual, 2)
        distancia = math.sqrt(distancia)
        distancias.append((distancia, tabelaTreino.iloc[linhaTreino, numeroColunas - 1]))
    distancias.sort()
    vizinhos = distancias[0:K]
    res = 0
    for vizinho in vizinhos:
        (dist, classe) = vizinho
        if(classe == 2):
            res += 1
        else:
            res -= 1
    if(res >= 0 and tabelaTeste.iloc[linhaTeste, numeroColunas - 1] == 4):
        erros += 1
    if(res < 0 and tabelaTeste.iloc[linhaTeste, numeroColunas - 1] == 2):
        erros -= 1
print("QUANTIDADE DE ERROS: " + str(erros))
