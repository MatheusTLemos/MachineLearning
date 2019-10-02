import numpy as np
import math
import matplotlib.pyplot as plt
from statistics import mode 
import pandas as pd

#Leitura e divisão dos dados
dados=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', delimiter=",")
numeroLinhas = dados.shape[0]
numeroColunas = dados.shape[1]
quantidadeTeste = np.int(numeroLinhas * 0.7)
quantidadeTreino = numeroLinhas - quantidadeTeste
tabelaTreino = dados.iloc[0:quantidadeTeste]
tabelaTeste = dados.iloc[quantidadeTeste:]

#Classificação
for linhaTeste in range(quantidadeTeste - 1):
    distancias = []
    for linhaTreino in range(quantidadeTreino - 1):
        distancia = 0
        for prop in range(1, numeroColunas - 1):
            valorTesteNaPropriedadeAtual = float(tabelaTeste.iloc[linhaTeste, prop] if tabelaTeste.iloc[linhaTeste, prop] != '?' else 999999)
            valorTreinoNaPropriedadeAtual = float(tabelaTreino.iloc[linhaTreino, prop] if tabelaTreino.iloc[linhaTreino, prop] != '?' else -999999)
            distancia += math.pow(valorTesteNaPropriedadeAtual - valorTreinoNaPropriedadeAtual, 2)
        distancia = math.sqrt(distancia)
        print(distancia)
