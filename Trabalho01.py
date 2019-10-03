#Matheus Teixeira Lemos 15.2.8032
import numpy as np
import math
import matplotlib.pyplot as plt
from statistics import mode 
import pandas as pd

K = 5

#Leitura e divisão dos dados
dados=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', delimiter=",")
dados = dados.sample(frac=1)
numeroLinhas = dados.shape[0]
numeroColunas = dados.shape[1]
quantidadeTeste = np.int(numeroLinhas * 0.3)
quantidadeTreino = numeroLinhas - quantidadeTeste
tabelaTreino = dados.iloc[0:quantidadeTreino]
tabelaTeste = dados.iloc[quantidadeTreino:]
print("DADOS DIVIDIDOS")

#Classificação
erros = 0
positivos = 0
falsosPositivos = 0
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
    print("CLASSE CALCULADA: " + str(classe))
    if(res >= 0 and tabelaTeste.iloc[linhaTeste, numeroColunas - 1] == 4):
        erros += 1
        falsosPositivos += 1
        positivos += 1
    if(res < 0 and tabelaTeste.iloc[linhaTeste, numeroColunas - 1] == 2):
        erros += 1
print("TAXA DE ACERTOS: " + str(100 * (1 - (erros/numeroLinhas))))
print("VERDADEIROS POSITIVOS: " + str(positivos))
print("VERDADEIROS NEGATIVOS: " + str(numeroLinhas - positivos))
print("FALSOS POSITIVOS: " + str(falsosPositivos))
print("FALSOS NEGATIVOS: " + str(erros - falsosPositivos))
