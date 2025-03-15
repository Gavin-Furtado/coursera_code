import numpy as np

def dcm(phi, theta, psi):
    rotation_1 = np.array([[1,0,0],
                        [0,np.cos(np.radians(phi)),np.sin(np.radians(phi))],
                        [0,-np.sin(np.radians(phi)),np.cos(np.radians(phi))]])

    rotation_2 = np.array([[np.cos(np.radians(theta)),0,-np.sin(np.radians(theta))],
                        [0,1,0],
                        [np.sin(np.radians(theta)),0,np.cos(np.radians(theta))]])

    rotation_3 = np.array([[np.cos(np.radians(psi)),np.sin(np.radians(psi)),0],
                        [-np.sin(np.radians(psi)),np.cos(np.radians(psi)),0],
                        [0,0,1]])
    
    dcm = (rotation_1 @ rotation_2) @ rotation_3

    return dcm

def calculate_attitude(dcm):
    phi = np.degrees(np.arctan2(dcm[1][2],dcm[2][2]))
    theta = np.degrees(-np.arcsin(dcm[0][2]))
    psi = np.degrees(np.arctan2(dcm[0][1],dcm[0][0]))

    return phi, theta, psi

def calculate_313_attitude(dcm):
    phi = np.degrees(np.arctan2(dcm[1][2],dcm[2][2]))
    theta = np.degrees(-np.arcsin(dcm[0][2]))
    psi = np.degrees(np.arctan2(dcm[0][1],dcm[0][0]))

    return phi, theta, psi

# Question 2
# mat_BN = dcm(30,20,10)
# mat_RN = dcm(5,5,-5)
# mat_BR = mat_BN @ mat_RN.T
# phi, theta, psi = calculate_attitude(mat_BR)

# print(phi,theta, psi)

# Question 2
# 3-2-1 DCM from inertial to body frame

mat_BN = dcm(30,20,10)
# print(mat_BN)
# phi, theta, psi = calculate_attitude(mat_BN)
# print(phi,theta,psi)

