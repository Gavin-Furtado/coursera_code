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

def main():
    sigma = np.array([0.1,0.2,0.3])
    dcm = mrp2dcm(sigma)
    print(f'MRP to DCM = {dcm}')

    # converting from dcm to mrp
    sig1 =  (-0.7692308)/(1+0.53846163)
    sig2 =  0.15384603/(1+0.53846163)
    sig3 =  0.30769213/(1+0.53846163)

    print(sig1,sig2,sig3)
    print(np.sqrt(sig1**2 + sig2**2 + sig3**2))

if __name__ == '__main__':
    main()