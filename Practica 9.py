import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

plt.style.use('dark_background')
data = pd.read_csv("PlayStore_Operacion5.csv")

X = data[["Precio", "Rating"]]
plt.scatter(X["Precio"], X["Rating"], c="gray", label='Rating')
plt.ylabel("Rating")
plt.xlabel("Precio")
plt.title("El rating en relacion on el precio de las aplicaciones")
plt.legend()
plt.savefig("Clustering - 0.png")
plt.show()

K = 3

Centroids = (X.sample(n=K))
plt.scatter(X["Precio"], X["Rating"], c="gray", label='Rating')
plt.scatter(Centroids["Precio"], Centroids["Rating"], c="red", label='Puntos K')
plt.xlabel("Precio")
plt.ylabel("Rating")
plt.title("Gráfica con puntos K")
plt.legend()
plt.savefig("Clustering - Con puntos K.png")
plt.show()

diff = 1
j = 0

while (diff != 0):
    XD = X
    i = 1
    for index1, row_c in Centroids.iterrows():
        ED = []
        for index2, row_d in XD.iterrows():
            d1 = (row_c["Precio"] - row_d["Precio"]) ** 2
            d2 = (row_c["Rating"] - row_d["Rating"]) ** 2
            d = sqrt(d1 + d2)
            ED.append(d)
        X[i] = ED
        i = i + 1

    C = []
    for index, row in X.iterrows():
        min_dist = row[1]
        pos = 1
        for i in range(K):
            if row[i + 1] < min_dist:
                min_dist = row[i + 1]
                pos = i + 1
        C.append(pos)
    X["Cluster"] = C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Rating", "Precio"]]
    if j == 0:
        diff = 1
        j = j + 1
    else:
        diff = (Centroids_new['Rating'] - Centroids['Rating']).sum() + (Centroids_new['Precio'] - Centroids['Precio']).sum()
        # print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Rating", "Precio"]]

color = ['gray', 'yellow', 'cyan']
for k in range(K):
    data = X[X["Cluster"] == k + 1]
    if k == 0:
        plt.scatter(data["Precio"], data["Rating"], c=color[k], label='Rating1')
    elif k == 1:
        plt.scatter(data["Precio"], data["Rating"], c=color[k], label='Rating2')
    elif k == 2:
        plt.scatter(data["Precio"], data["Rating"], c=color[k], label='Rating3')

plt.scatter(Centroids["Precio"], Centroids["Rating"], c='red', label='Puntos K')
plt.xlabel('Precio')
plt.ylabel('Rating')
plt.title("Clustering")
plt.legend()
plt.savefig("Clustering.png")
plt.show()