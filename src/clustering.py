import matplotlib.pyplot as plt 
import numpy as np  
from sklearn.cluster import KMeans

def show_data(x):
    plt.scatter(x[:,0],x[:,1], label='True Position')  
    plt.show()

def cluster_data(x, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(x) 
    return kmeans.cluster_centers_, kmeans.labels_

def show_clustered_data(x, labels):
    plt.scatter(X[:,0],X[:,1], c=labels, cmap='rainbow')
    plt.show()
