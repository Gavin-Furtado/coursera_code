import numpy as np

def tilde_matrix(vec):
    tilde = np.array([[0, -vec[2], vec[1]],
                      [vec[2], 0, -vec[0]],
                      [-vec[1], vec[0], 0]])
    return tilde

def mrp2dcm(sigma):
    I = np.eye(3)
    sig_norm = np.linalg.norm(sigma)
    sigma_tilde = tilde_matrix(sigma)
    C = I + (8*(sigma_tilde @ sigma_tilde) - (4*(1-sig_norm**2))*sigma_tilde)/(1+sig_norm**2)**2
    return C

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

def quat2mrp(q):
    sig1 = q[1]/(1+q[0])
    sig2 = q[2]/(1+q[0])
    sig3 = q[3]/(1+q[0])

    return np.array([sig1,sig2,sig3])

def main():
    sigma_BN = np.array([0.1,0.2,0.3])
    # sigma_RB = np.array([-0.1,0.3,0.1])
    sigma_RN = np.array([0.5,0.3,0.1])

    DCM_BN = mrp2dcm(sigma_BN)
    # DCM_RB = mrp2dcm(sigma_RB)
    DCM_RN = mrp2dcm(sigma_RN)

    # DCM_RN = DCM_RB @ DCM_BN
    DCM_BR = DCM_BN @ DCM_RN.T

    # quat_RN = dcm2quat(DCM_RN)
    # mrp_RN = quat2mrp(quat_RN)

    quat_BR = dcm2quat(DCM_BR)
    mrp_BR = quat2mrp(quat_BR)

    # print(np.linalg.norm(mrp_RN))
    print(np.linalg.norm(mrp_BR))

    # print(mrp_RN)
    print(mrp_BR)        

if __name__ == '__main__':
    main()