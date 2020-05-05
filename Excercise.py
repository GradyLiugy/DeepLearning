import numpy as np
import matplotlib.pyplot as plt 

X = np.array([[1,2,3],[0,1,2],[3,0,1]])
print(X)
# print(X.shape)

W = np.array([[2, 0, 1], [0, 1, 2],[1,0,2]])
print(W)
# print(W.shape)

Y = X * W

print(Y)