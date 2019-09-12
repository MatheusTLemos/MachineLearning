import numpy as np
import statistics 
from statistics import mode 
np.random.seed(0)
#matriz
K = 3
a = np.zeros((10,2))
mean1 = [3,3]
cov1 = [[1,0], [0,1]]
#covariancia
N1 = 5
classe_1 = np.random.multivariate_normal(mean1, cov1, N1)
mean2 = [6,6]
cov2 = [[1,0], [0,1]]
N2 = 5
classe_2 = np.random.multivariate_normal(mean2, cov2, N2)
ponto_teste = [4,4]
#concatenando classe_1 com classe_2
X = np.concatenate((classe_1,classe_2))
labels = np.concatenate((np.repeat(1,len(classe_1)), np.repeat(-1, len(classe_2))))
distancia = np.zeros((len(X),1))
for i in range(0,10):
	distancia[i] = np.linalg.norm(X[i,0:1] - ponto_teste)
distanciaComLabels = np.column_stack((distancia, labels))
distanciaComLabels.sort(axis=0)
print("Valores de distancia:")
print(distanciaComLabels)
maisProximos = distanciaComLabels[:K]
print("Classes dos K vizinhos mais proximos")
print(maisProximos)
labelPontoTeste = mode([vizinho[1] for vizinho in maisProximos])
print("Ponto é da classe ")
print(labelPontoTeste)
