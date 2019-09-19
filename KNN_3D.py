import numpy as np
import matplotlib.pyplot as plt
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
seq = np.arange(0, 9, 0.5)
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
fig = plt.figure()
fig.suptitle('Resultado KNN')  
fig, ax1 = plt.subplots(nrows=1)
ax1.scatter(classe_1[:,0], classe_1[:,1], c='blue', alpha=0.9)
ax1.scatter(classe_2[:,0], classe_2[:,1], c='red', alpha=0.9)
ax1.contour(seq, seq, matrizLabels, levels=0, linewidths=1, colors='k')
contrl = ax1.contourf(seq, seq, matrizLabels, levels=1, alpha=0.3, colors=['red', 'blue'])
