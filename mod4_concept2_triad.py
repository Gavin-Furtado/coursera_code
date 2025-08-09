import numpy as np
import matplotlib.pyplot as plt

def dcm2quat(dcm):
    q0_sq = 0.25*(1 + np.trace(dcm))
    q1_sq = 0.25*(1 + 2*dcm[0][0] - np.trace(dcm))
    q2_sq = 0.25*(1 + 2*dcm[1][1] - np.trace(dcm))
    q3_sq = 0.25*(1 + 2*dcm[2][2] - np.trace(dcm))

    if q0_sq >= q1_sq and q0_sq >= q2_sq and q0_sq >= q3_sq:
        print("q0_sq is the greatest")
        q0 = np.sqrt(q0_sq)
        q1 = 0.25*(dcm[1][2] - dcm[2][1])/q0
        q2 = 0.25*(dcm[2][0] - dcm[0][2])/q0 
        q3 = 0.25*(dcm[0][1] - dcm[1][0])/q0

    elif q1_sq >= q0_sq and q1_sq >= q2_sq and q1_sq >= q3_sq:
        print("q1_sq is the greatest")
        q1 = np.sqrt(q1_sq)
        q0 = 0.25*(dcm[1][2] - dcm[2][1])/q1
        q2 = 0.25*(dcm[0][1] + dcm[1][0])/q1
        q3 = 0.25*(dcm[2][0] + dcm[0][2])/q1

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

    q = np.array([q0, q1, q2, q3])
    q /= np.linalg.norm(q)

    if q[0] < 0:  # optional: short rotation convention
        q = -q

    return q

v1_b = np.array([0.8273,0.5541,-0.0920])
v2_b = np.array([-0.8285,0.5522,-0.0955])
v1_n = np.array([-0.1517,-0.9669,0.2050])
v2_n = np.array([-0.8393,0.4494,-0.3044])

v1_b = v1_b/np.linalg.norm(v1_b)
v2_b = v2_b/np.linalg.norm(v2_b)
v1_n = v1_n/np.linalg.norm(v1_n)
v2_n = v2_n/np.linalg.norm(v2_n)

t1_b = v1_b.copy()
t2_b = np.cross(v1_b,v2_b)/np.linalg.norm(np.cross(v1_b,v2_b))
t3_b = np.cross(t1_b,t2_b)

t1_n = v1_n.copy()
t2_n = np.cross(v1_n,v2_n)/np.linalg.norm(np.cross(v1_n,v2_n))
t3_n = np.cross(t1_n,t2_n)

BT_est = np.array([t1_b,
                   t2_b,
                   t3_b]).T

NT = np.array([t1_n,
               t2_n,
               t3_n]).T

BN_est = BT_est @ NT.T

print(BN_est)

# Question 2
BN_est = np.array([[0.969846,0.17101,0.173648],
                   [-0.200706,0.96461,0.17101],
                   [-0.138258,-0.200706,0.969846]])

BN_true = np.array([[0.963592,0.187303,0.190809],
                    [-0.223042,0.956645, 0.187303],
                    [-0.147454,-0.223042,0.963592]])

B_bar_B = BN_est @ BN_true.T

quat = dcm2quat(B_bar_B)

angle = np.rad2deg(2*np.arccos(quat[0]))
print(quat)
print(angle)