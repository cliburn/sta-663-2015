
import numpy as np

def euclidean_dist(u, v):
    w = u - v
    return np.sum(np.sqrt(w**2))
    
# def euclidean_dist(u, v):
#     """Returns Euclidean distance betwen numpy vectors u and v."""
#     w = u - v
#     return np.sqrt(np.sum(w**2))