from sklearn.cluster import KMeans
import numpy as np

# dummy training data (you can improve later)
X = np.array([
    [80, 2, 0.7, 0.6, 0.5],
    [40, 10, 0.5, 0.3, 0.2],
    [60, 5, 0.8, 0.8, 0.3],
    [30, 12, 0.3, 0.2, 0.1]
])

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)


def predict_cluster(features):
    vector = [[
        features["avg_popularity"],
        features["diversity"],
        features["energy"],
        features["valence"],
        features["repetition"]
    ]]
    
    return kmeans.predict(vector)[0]