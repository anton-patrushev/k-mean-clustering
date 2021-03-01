import sklearn.cluster as cluster


def fit_cluster(clusters_quantity: int, points: list):
    kmeans_cluster = cluster.KMeans(clusters_quantity)
    kmeans_cluster.fit(points)

    return kmeans_cluster
