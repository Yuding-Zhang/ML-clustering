import matplotlib.pyplot as plt
import numpy as np
# from algorithms.HierarchicalClustering import Hierarchical
from sklearn.preprocessing import normalize
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

import pandas as pd


dataset = dict()
with open('../data/generatePoints.txt', 'r') as data:
    for line in data:
        points_serial_number, points_x, points_y = line.strip().split()
        points_serial_number, points_x, points_y = int(points_serial_number), float(points_x), float(points_y)
        dataset[points_serial_number] = (points_x, points_y)

dataset = list(dataset.values())

data_scaled = normalize(dataset)
data_scaled = pd.DataFrame(data_scaled)


plt.figure(figsize=(10, 7))
plt.title("Dendrograms1")
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
plt.axhline(y=6, color='r', linestyle='--')
plt.savefig('../images/HC/result_1.png')
plt.show()


cluster = AgglomerativeClustering(n_clusters=6, linkage='ward')  # 直接调用算法
cluster.fit_predict(data_scaled)
points_cluster = cluster.fit(data_scaled).labels_
print(points_cluster)

plt.figure(figsize=(10, 7))
x, y = zip(*dataset)
plt.scatter(x, y, c=cluster.labels_)
plt.savefig('../images/HC/result_2.png')
plt.show()

