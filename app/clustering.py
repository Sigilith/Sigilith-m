import numpy as np
from sklearn.cluster import KMeans


def cluster_vectors(vectors, k):
    # Clustering the vectors into k behavioral families
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(vectors)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return labels, centroids
