import numpy as np
import matplotlib.pyplot as plt

def quaternion_to_dcm(q0,q1,q2,q3):
    dcm = np.array([[((q0**2)+(q1**2)-(q2**2)-(q3**2)), 2*((q1*q2)+(q0*q3)), 2*((q1*q3)-(q0*q2))],
                      [2*((q1*q2)-(q0*q3)), ((q0**2)-(q1**2)+(q2**2)-(q3**2)), 2*((q2*q3)+(q0*q1))],
                      [2*((q1*q3)+(q0*q2)), 2*((q2*q3)-(q0*q1)), ((q0**2)-(q1**2)-(q2**2)+(q3**2))]])
    
    return dcm

v1_b = np.array([0.8273,0.5541,-0.0920])
v2_b = np.array([-0.8285,0.5522,-0.0955])
v1_n = np.array([-0.1517,-0.9669,0.2050])
v2_n = np.array([-0.8393,0.4494,-0.3044])

v1_b = v1_b/np.linalg.norm(v1_b)
v2_b = v2_b/np.linalg.norm(v2_b)
v1_n = v1_n/np.linalg.norm(v1_n)
v2_n = v2_n/np.linalg.norm(v2_n)

B1 = np.outer(v1_b,v1_n.T)
B2 = np.outer(v2_b,v2_n.T)

B = 0.5*B1 + 0.5*B2

S = B + B.T
sigma = np.trace(B)

Z = np.array([B[1][2] - B[2][1], B[2][0] - B[0][2], B[0][1]-B[1][0]]).T

K = np.zeros((4,4))
K[0,0] = sigma
K[0, 1:4] = Z.T
K[1:4, 0] = Z
K[1:4, 1:4] = S - sigma*np.eye(3)

# Find the eigenvector corresponding to the maximum eigenvalue
eigvals, eigvecs = np.linalg.eig(K)
max_index = np.argmax(eigvals)
q_opt = eigvecs[:, max_index]  # This is [q0, q1, q2, q3]

# Normalize quaternion
q_opt = q_opt / np.linalg.norm(q_opt)

print("Quaternion (q0, q1, q2, q3):", q_opt)
print("Max eigenvalue:", eigvals[max_index])


DCM = quaternion_to_dcm(q_opt[0],q_opt[1],q_opt[2],q_opt[3])
print(DCM)

print(DCM@v2_n)


