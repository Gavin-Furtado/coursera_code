import numpy as np

q0 = 0.235702
q1 = 0.471405
q2 = -0.471405
q3 = 0.707107

dcm_bn = np.array([[-0.529403, -0.467056, 0.708231],
                   [-0.474115, -0.529403, -0.703525],
                   [0.703525, -0.708231, 0.0588291]])

def quaternion_to_dcm(q0,q1,q2,q3):
    dcm = np.array([[((q0**2)+(q1**2)-(q2**2)-(q3**2)), 2*((q1*q2)+(q0*q3)), 2*((q1*q3)-(q0*q2))],
                      [2*((q1*q2)-(q0*q3)), ((q0**2)-(q1**2)+(q2**2)-(q3**2)), 2*((q2*q3)+(q0*q1))],
                      [2*((q1*q3)+(q0*q2)), 2*((q2*q3)-(q0*q1)), ((q0**2)-(q1**2)-(q2**2)+(q3**2))]])
    
    return dcm

def dcm_to_ep(dcm):
    q0_sq = 0.25*(1 + np.trace(dcm))
    q1_sq = 0.25*(1 + 2*dcm[0][0] - np.trace(dcm))
    q2_sq = 0.25*(1 + 2*dcm[1][1] - np.trace(dcm))
    q3_sq = 0.25*(1 + 2*dcm[2][2] - np.trace(dcm))

    if q0_sq > q1_sq and q0_sq > q2_sq and q0_sq > q3_sq:
        print("q0_sq is the greatest")
        q0 = np.sqrt(q0_sq)
        q1 = 0.25*(dcm[1][2] - dcm[2][1])/q0
        q2 = 0.25*(dcm[2][0] - dcm[0][2])/q0 
        q3 = 0.25*(dcm[0][1] - dcm[1][0])/q0

    elif q1_sq > q0_sq and q1_sq > q2_sq and q1_sq > q3_sq:
        print("q1_sq is the greatest")
        q1 = np.sqrt(q1_sq)
        q0 = 0.25*(dcm[1][2] - dcm[2][1])/q1
        q2 = 0.25*(dcm[0][1] - dcm[1][0])/q1
        q3 = 0.25*(dcm[2][0] - dcm[0][2])/q1

    elif q2_sq > q0_sq and q2_sq > q1_sq and q2_sq > q3_sq:
        print("q2_sq is the greatest")
        q2 = np.sqrt(q2_sq)
        q0 = 0.25*(dcm[2][0] - dcm[0][2])/q2
        q1 = 0.25*(dcm[0][1] + dcm[1][0])/q2
        q3 = 0.25*(dcm[1][2] + dcm[2][1])/q2

    else:
        print("q3_sq is the greatest")
        q3 = np.sqrt(q3_sq)
        q0 = 0.25*(dcm[0][1] - dcm[1][0])/q3
        q1 = 0.25*(dcm[2][0] + dcm[0][2])/q3
        q2 = 0.25*(dcm[1][2] + dcm[2][1])/q3

    return q0, q1, q2, q3

def dcm_321(phi, theta, psi):
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

# Question 1
q_dcm = quaternion_to_dcm(q0,q1,q2,q3)
print(q_dcm)

# Question 2
q0,q1,q2,q3 = dcm_to_ep(dcm_bn)
print(f'q0 = {q0}, q1 = {q1}, q2 = {q2}, q3 = {q3}')

# Question 3
mat_dcm_321 = dcm_321(-10,10,20)
q0,q1,q2,q3 = dcm_to_ep(mat_dcm_321)
print(f'q0 = {q0}, q1 = {q1}, q2 = {q2}, q3 = {q3}')


# Module 3 Concept check 3 Question 2
# matrix = dcm_321(120,-10,20)
# print(matrix)
