import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as ols

#Aplicaciones lanzadas por año
def Practica_6():

    plt.style.use('dark_background')

    df = pd.read_csv("PlayStore_Operacion2.csv")
    df.reset_index(drop=True, inplace=True)
    df['Año de lanzamiento']=df['Año de lanzamiento'].fillna(0).astype(np.int64)
    df_T = df.groupby('Año de lanzamiento')['ID'].sum(numeric_only= False)
    df_T = df_T.reset_index()

    features = df_T["Año de lanzamiento"]
    labels = df_T["ID"]


    slope, intercept, r, p, std_err = stats.linregress(features, labels)
    def lineFunc(x):
        return slope * x + intercept

    lineY = list(map(lineFunc, features))
    print(lineY)

    plt.figure(figsize=(8,5))
    plt.ylabel('Aplicaciones', fontsize=15)
    plt.xlabel('Año', fontsize=15)
    plt.scatter(features, labels, c="blue", label="Total aplicaciones")
    plt.plot(features, lineY, c="red", label="Regresion lineal")
    plt.title("Apps lanzadas por año")
    plt.legend()
    plt.savefig("Regresion_Lineal.png")
    plt.show()    

Practica_6()