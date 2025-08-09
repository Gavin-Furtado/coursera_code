import numpy as np

sigma_1 = np.array([0.1,0.2,0.3])
sigma_2 = np.array([1.2,-0.1,-0.001])
sigma_3 = np.array([0.1,0.2,0.3])

print(f'norm of sigma_1 = {np.linalg.norm(sigma_1)}')
print(f'norm of sigma_2 = {np.linalg.norm(sigma_2)}')

norm_3 = np.linalg.norm([0.1,0.2,0.3])

shadow_set = -np.array([sigma_3[0]/norm_3**2, sigma_3[1]/norm_3**2, sigma_3[2]/norm_3**2])

print(f'shadow set = {shadow_set}')