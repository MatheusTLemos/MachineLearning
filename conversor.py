from sklearn import datasets
import pandas as pd

def converterDatasetSklearnParaPandas(dataset):
    datasetPandas = pd.DataFrame(
        data= dataset.data,
        columns= dataset.feature_names
    )
    datasetPandas['target'] = pd.Series(dataset.target)
    return datasetPandas
