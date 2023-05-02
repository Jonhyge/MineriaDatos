import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import fisher_exact
import statsmodels.api as sm
import statsmodels.formula.api as ols



def Practica_5():
        #Hipotesis a probar
        #La cantidad de descargas tiene relacion con el promedio rating de la aplicacion
    plt.style.use('dark_background')
    df = pd.read_csv("Play_Store_Apps_limpio.csv")
    df = df[df['Maximo Instalaciones'].notna()]
    df_T = df.groupby('Rating')['Maximo Instalaciones'].sum(numeric_only= False)
    df_T.to_csv('PlayStore_Operacion4_Hipotesis.csv')

    df = pd.read_csv("PlayStore_Operacion4_Hipotesis.csv")
    x = df['Rating']
    y = df['Maximo Instalaciones']
    plt.figure(figsize=(9,9))
    plt.xlabel('Rating', fontsize=15)
    plt.ylabel('Descargas en miles de millones', fontsize=15)
    plt.bar(x, y, label="Descargas")
    plt.title("Hipotesis - La cantidad de descargas tiene relacion con el rating de la aplicacion")
    plt.legend()
    plt.savefig("Comprobacion de Hipotesis.png")
    plt.show()    

Practica_5()