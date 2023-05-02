import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Practica_4():
    plt.style.use('dark_background')
    df = pd.read_csv("PlayStore_Operacion1.csv")
    x = df['Categoria']
    y = df['ID']
    plt.figure(figsize=(8,5))
    plt.figure(figsize=(8, 5))
    plt.pie(y, labels=x)
    plt.title("Aplicaciones por categoria")
    plt.savefig("App_por_Categoria.png")
    plt.show()
    
    #Gráfica 2
    df = pd.read_csv("PlayStore_Operacion2.csv")
    x = df['Año de lanzamiento'].astype(str) +"\n"+ df["Categoria"]
    y = df['ID']
    plt.figure(figsize=(27,5))
    plt.xlabel('Categoria/Año', fontsize=15)
    plt.ylabel('Aplicaciones', fontsize=15)
    plt.bar(x, y)
    plt.title("Aplicaciones lanzadas por cada categoria de cada año")
    plt.savefig("Aplicaciones por Categoria-Año.png")
    plt.show()
    
    #Gráfica 3
    df = pd.read_csv("PlayStore_Operacion3.csv")
    x = df['Año de lanzamiento'].astype(str) +"\n"+ df["Contiene anuncios"].astype(str)
    y = df['count']
    plt.figure(figsize=(18, 9))
    plt.xlabel('Años', fontsize=15)
    plt.ylabel('Cantidad de aplicaciones', fontsize=15)
    plt.bar(x, y, label="Aplicaciones")
    plt.title("Cantidad de aplicaciones con anuncios por años")
    plt.savefig("Anuncios en aplicaciones.png")
    plt.show()


Practica_4()