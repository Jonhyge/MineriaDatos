from itertools import groupby
import pandas as pd
import numpy as np
import random

def Practica_3():

    file_name = "Play_Store_Apps_limpio.csv"

    #Cantidad de aplicaciones por categoria
    df1 = pd.read_csv(file_name)
    df_C = df1.groupby(["Categoria"])[['ID']].count()
    df_C.reset_index(inplace  = True)
    df_C.set_index("Categoria", inplace = True)
    df_C.to_csv('PlayStore_Operacion1.csv')

    #Cantidad de aplicaciones por categoria por año
    df2 = pd.read_csv(file_name)
    df2['Año de lanzamiento'] = df2['Año de lanzamiento'].fillna(0).astype(np.int64)
    df2 = df2[df2['Año de lanzamiento'] != 0]
    df_D = df2.groupby(["Año de lanzamiento","Categoria"])[['ID']].count()
    df_D.reset_index(inplace=True)
    df_D.set_index("Año de lanzamiento", inplace=True)
    df_D.to_csv('PlayStore_Operacion2.csv')


    #Inclusion de anuncios en las aplicaciones a lo largo de los años
    df3 = pd.read_csv(file_name)
    df3['Año de lanzamiento'] = df3['Año de lanzamiento'].fillna(0).astype(np.int64)
    df3 = df3[df3['Año de lanzamiento'] != 0]
    df_P = df3.groupby(["Año de lanzamiento"],as_index=False)["Contiene anuncios"].value_counts()
    df_P.to_csv('PlayStore_Operacion3.csv')



Practica_3()