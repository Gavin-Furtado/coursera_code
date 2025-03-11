import numpy as np

mat_BN = np.array([[-0.87097, 0.45161, 0.19355],
                   [-0.19355, -0.67742, 0.70968],
                   [0.45161, 0.58065, 0.67742]])

mat_tilde_omega = np.array([[0, -0.3, 0.2],
                            [0.3, 0, -0.1],
                            [-0.2, 0.1, 0]])

mat_BN_dot = -mat_tilde_omega @ mat_BN

print(mat_BN_dot)