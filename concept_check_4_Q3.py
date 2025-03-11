import numpy as np

mat_BN = np.array([[1/3, 2/3, -2/3],
                   [0, 1/np.sqrt(2),1/np.sqrt(2)],
                   [4/(3*np.sqrt(2)), -1/(3*np.sqrt(2)), 1/(3*np.sqrt(2))]])

mat_FN = np.array([[3/4,-2/4,np.sqrt(3)/4],
                   [-1/2, 0, np.sqrt(3)/2],
                   [-np.sqrt(3)/4, -np.sqrt(3)/2, -1/4]])

mat_BF = mat_BN @ mat_FN.T

print(mat_BF)