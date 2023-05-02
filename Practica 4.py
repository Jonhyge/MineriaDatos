import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Practica_4():

    df = pd.read_csv("PlayStore_Operacion1.csv")
    x = df['Categoria']
    y = df['ID']
    plt.figure(figsize=(8,5))
    plt.xlabel('Categoria', fontsize=17)
    plt.ylabel('Aplicaciones', fontsize=17)
    plt.scatter(x, y)
    plt.plot(x, y, label = "Aplicaciones")
    plt.title("Aplicaciones por categoria")
    plt.legend()
    plt.savefig("App_por_Categoria.png")
    plt.show()
    
    #Gráfica 2
    df = pd.read_csv("PlayStore_Operacion2.csv")
    x = df['Sexo']
    y = df['Nombre']
    plt.figure(figsize=(8,5))
    plt.xlabel('Sexo', fontsize=15)
    plt.ylabel('Atletas', fontsize=15)
    plt.bar(x, y, label = "Atletas")
    plt.title("Comparación entre el Sexo de los Atletas")    
    plt.legend()
    plt.savefig("img/Gráficas/Grafica2 - Participantes por Sexo.png")
    plt.show()
    
    #Gráfica 3
    df = pd.read_csv("csv_operacion/csv_operacion3.csv")
    x = df['Comité']
    y = df['Medalla']
    plt.figure(figsize=(8,5))
    plt.pie(y, labels=x)
    plt.title("Distribución de Medallas entre Países Participantes")
    plt.savefig("img/Gráficas/Grafica3 - Medallas por Comité(Total).png")
    plt.show()


Practica_4()