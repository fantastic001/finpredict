import matplotlib.pyplot as plt 
import numpy as np  
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def show_data(x, project=False):
    if project:
        pca = PCA(n_components=2)
        x = pca.fit_transform(x)
    plt.scatter(x[:,0],x[:,1], label='True Position')  
    plt.show()

def cluster_data(x, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(x) 
    return kmeans.cluster_centers_, kmeans.labels_

def show_clustered_data(x, labels, project=False):
    if project:
        pca = PCA(n_components=2)
        x = pca.fit_transform(x)
    plt.scatter(x[:,0],x[:,1], c=labels, cmap='rainbow')
    plt.show()
