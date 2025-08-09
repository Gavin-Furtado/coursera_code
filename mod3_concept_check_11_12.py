import numpy as np
import matplotlib.pyplot as plt

class CRP():
    def __init__(self, crp_vector):
        self.q = np.array(crp_vector, dtype=float)
        if self.q.shape != (3,):
            raise ValueError('CRP vector must be a 3-element vector')

    def tilde_matrix(self,q):
        '''
        Converts a CRP vector into skew-symmetric (tilde) matrix.
        '''
        q = np.asarray(q).flatten()
        q_tilde = np.array([
            [0,-q[2],q[1]],
            [q[2],0,-q[0]],
            [-q[1],q[0],0]
        ])
        return q_tilde
    
    def crp2dcm(self):
        '''
        Converts CRP to DCM
        '''
        q = self.q
        q_tilde = self.tilde_matrix(q)
        factor = 1/(1+np.dot(q.T,q))
        I = np.eye(3)

        C = factor *(((1- np.dot(q.T,q))*I) + (2*(np.outer(q,q.T))) - 2*q_tilde)

        return C    
    
    def zeta(self,C):
        zeta = np.sqrt(np.trace(C)+1)
        return zeta
    
    def dcm2crp(self,C,zeta):
        q = 1/(zeta**2) * np.array([C[1][2]-C[2][1],
                                    C[2][0]-C[0][2],
                                    C[0][1]-C[1][0]])
        return q
    
    def addition(self,q1,q2):
        '''
        Attitude addition between two quaternions
        '''
        numerator = q2 + q1 - np.cross(q2,q1)
        denominator = 1 - (np.dot(q2,q1))
        q = numerator/denominator

        return q

def main():
    crp = np.array([0.1,0.2,0.3])
    
    convert_crp2dcm = CRP(crp)
    dcm = convert_crp2dcm.crp2dcm()
    
    ## DCM

    DCM = np.array([[0.333333, -0.666667, 0.666667],
                    [0.871795, 0.487179, 0.0512821],
                    [-0.358974, 0.564103, 0.74359]]) 
    
    zeta = convert_crp2dcm.zeta(DCM)
    crp = convert_crp2dcm.dcm2crp(DCM,zeta)   
    

    print(f'Direction Cosine Matrix (DCM):')
    print(np.round(dcm,10))

    print(f'CRP = {crp}')

    ## Question 4
    crp1 = np.array([-0.1,-0.2,-0.3])
    crp2 = np.array([-0.3,0.3,0.1])

    crp_addition = convert_crp2dcm.addition(crp1,crp2)

    print(f'CRP Addition = {crp_addition}')

if __name__=='__main__':
    main()