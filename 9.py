
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

iris = pd.read_csv('Iris.csv').drop('species', axis=1).values
data = iris[:5]

def single_linkage(data):
    n = data.shape[0]
    proximity_matrix = np.zeros((n, n))
   
    for i in range(n):
        for j in range(i+1, n):
            proximity_matrix[i, j] = np.min(np.linalg.norm(data[i] - data[j]))
            proximity_matrix[j, i] = proximity_matrix[i, j]
   
    return proximity_matrix

def complete_linkage(data):
    n = data.shape[0]
    proximity_matrix = np.zeros((n, n))
   
    for i in range(n):
        for j in range(i+1, n):
            proximity_matrix[i, j] = np.max(np.linalg.norm(data[i] - data[j]))
            proximity_matrix[j, i] = proximity_matrix[i, j]
   
    return proximity_matrix

single_linkage_matrix = single_linkage(data)
print("Single-linkage proximity matrix:")
print(single_linkage_matrix)

linkage_matrix = linkage(data, method='single')
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix)
plt.title('Dendrogram - Single Linkage')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

complete_linkage_matrix = complete_linkage(data)
print("\nComplete-linkage proximity matrix:")
print(complete_linkage_matrix)

linkage_matrix = linkage(data, method='complete')
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix)
plt.title('Dendrogram - Complete Linkage')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()