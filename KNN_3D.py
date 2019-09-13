import numpy as np
from statistics import mode 
np.random.seed(0)
K = 3
a = np.zeros((10,2))
mean1 = [3,3]
cov1 = [[1,0], [0,1]]
N1 = 5
classe_1 = np.random.multivariate_normal(mean1, cov1, N1)
mean2 = [6,6]
cov2 = [[1,0], [0,1]]
N2 = 5
classe_2 = np.random.multivariate_normal(mean2, cov2, N2)
X = np.concatenate((classe_1,classe_2))
labels = np.concatenate((np.repeat(1,len(classe_1)), np.repeat(-1, len(classe_2))))
seq = np.arange(1, 7.5, 0.5)
matrizLabels = np.zeros((len(seq),   len(seq)))
for i_grid in range(0,  len(seq)):
    for j_grid in range(0,  len(seq)):
        ponto_teste = [seq[i_grid],  seq[j_grid]]
        distancia = np.zeros((len(X),1))
        for i in range(0,10):
            distancia[i] = np.linalg.norm(X[i] - ponto_teste)
        distanciaComLabels = np.column_stack((distancia, labels))
        distanciaComLabels = sorted(distanciaComLabels,  key=lambda x: x[0])
        maisProximos = distanciaComLabels[:K]
        labelPontoTeste = mode([vizinho[1] for vizinho in maisProximos])
        matrizLabels[i_grid,  j_grid] = labelPontoTeste
print(matrizLabels)
