from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

def getData():
    iris = load_iris()
    data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                        columns= iris['feature_names'] + ['target'])

    data1 = data1.loc[:, 'sepal length (cm)':'sepal width (cm)']
                     
    scaler1 = StandardScaler()
    scaler2 = Normalizer()

    x = data1

    x_train = x[1:int(len(x)*.8)]
    x_test = x[1:-int(len(x)*.8)]


    x_train = scaler1.fit(x_train).transform(x_train)
    x_train = scaler2.fit(x_train).transform(x_train)
    x_test = scaler1.fit(x_train).transform(x_train)
    x_test = scaler2.fit(x_train).transform(x_train)
    print(x_train)
    return x_train