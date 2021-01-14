import numpy as np

def pathlength(x, y, z, k):
    pts = [x, y, z, k] # Corners of rectangle of height 1, length 3
    apts = np.array(pts) # Make it a numpy array
    lengths = np.sqrt(np.sum(np.diff(apts, axis=0)**2, axis=1)) # Length between corners
    total_length = np.sum(lengths)
    return total_length

print(pathlength((1, 1), (2, 1), (1, 2), (1, 1)))