import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

beta_fb = np.array([0.359211,0.898027,0.179605,0.179605])

beta_bn = np.array([0.774597,0.258199,0.516398,0.258199])

class EulerParameter:
    def __init__(self,q0,q1,q2,q3):
        self.q = np.array([q0,q1,q2,q3], dtype=float)

    def normalize(self):
        self.q = self.q/np.linalg.norm(self.q)

    def inverse(self):
        q0,q1,q2,q3 = self.q
        return EulerParameter(q0,-q1,-q2,-q3)

    def multiply_matrix_method(self, other):
        q2 = self.q
        G = np.array([
            [q2[0],-q2[1],-q2[2],-q2[3]],
            [q2[1], q2[0], q2[3], -q2[2]],
            [q2[2], -q2[3], q2[0], q2[1]],
            [q2[3], q2[2], -q2[1], q2[0]]
        ])

        q1 = other.q
        q3 = G @ q1
        return EulerParameter(*q3)

def main():
    q_BN = EulerParameter(0.774597, 0.258199, 0.516398, 0.258199)  # q - N to B
    q_FB = EulerParameter(0.359211, 0.898027, 0.179605, 0.179605)  # q - B to F

    # q_BN.normalize()
    # q_FB.normalize()

    q_FN = q_FB.multiply_matrix_method(q_BN)
    # q_FN.normalize()

    print("q_BN:", q_BN.q)
    print("q_FB:", q_FB.q)
    print("Combined q_FN:", q_FN.q)

    # q_BN = EulerParameter(-0.377964, 0.755929, 0.377964, 0.377964)  # q - N to B
    # q_FN = EulerParameter(0.359211, 0.898027, 0.179605, 0.179605)  # q - B to F

    # # q_BN.normalize()
    # # q_FN.normalize()

    # q_NB = q_BN.inverse()
    # q_FB = q_FN.multiply_matrix_method(q_NB)
    # # q_FB.normalize()

    # print("q_BN:", q_BN.q)
    # print("q_FN:", q_FN.q)
    # print("Combined q_FB:", q_FB.q)


if __name__ == "__main__":
    main()