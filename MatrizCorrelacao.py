from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
np.set_printoptions(threshold=sys.maxsize)

def converterDatasetSklearnParaPandas(dataset):
    datasetPandas = pd.DataFrame(
        data= dataset.data,
        columns= dataset.feature_names
    )
    datasetPandas['target'] = pd.Series(dataset.target)
    return datasetPandas

dataset = datasets.load_breast_cancer()
datasetPandas = converterDatasetSklearnParaPandas(dataset)

correlacao = datasetPandas.corr()
plt.matshow(correlacao)
plt.show()
