# Matheus Teixeira Lemos 15.2.8032
import pandas as pd
import numpy as np
from itertools import combinations
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

def converterDatasetSklearnParaPandas(dataset):
    datasetPandas = pd.DataFrame(
        data= dataset.data,
        columns= dataset.feature_names
    )
    datasetPandas['target'] = pd.Series(dataset.target)
    return datasetPandas

def calcularAcuracia(real, obtido):
    acertos = 0
    total = sum(1 for i in real)
    for x in range(0, total):
        if real[x] == obtido[x]:
            acertos += 1
    return acertos
        

dataset = datasets.load_breast_cancer()
datasetPandas = converterDatasetSklearnParaPandas(dataset)

labels = dataset.target

knn = KNeighborsClassifier(n_neighbors=5)

melhorDataset = pd.DataFrame()
melhorAcuracia = 0

for x in range(0,10):
    combinacoes = list(combinations(datasetPandas.columns,x))
    for combinacao in combinacoes:
        dataAux = pd.DataFrame()  
        for coluna in combinacao:
            if coluna != "target":
                dataAux[[coluna]] = datasetPandas[[coluna]]
        treinamento = dataAux.head(500)
        treinamentoLabels = labels[0:500]
        teste = dataAux.tail(69)
        testeLabels = labels[500:569]
        if treinamento.shape[0] > 0:
            knn.fit(treinamento, treinamentoLabels)
            res = knn.predict(teste)
            acuracia = calcularAcuracia(testeLabels, res)
            if acuracia > melhorAcuracia:
                melhorAcuracia = acuracia
                melhorDataset = dataAux

print("Melhor dataset: ")
print(melhorDataset)
