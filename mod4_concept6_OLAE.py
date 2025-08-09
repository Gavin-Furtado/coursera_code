import numpy as np

# Input vectors (body and inertial)
v_b_list = [
    np.array([0.8273, 0.5541, -0.0920]),
    np.array([-0.8285, 0.5522, -0.0955])
]

v_n_list = [
    np.array([-0.1517, -0.9669, 0.2050]),
    np.array([-0.8393, 0.4494, -0.3044])
]

def normalize(v):
    return v / np.linalg.norm(v)

def tilde(v):
    return np.array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])

# Normalize all vectors
v_b_list = [normalize(v) for v in v_b_list]
v_n_list = [normalize(v) for v in v_n_list]

# Construct S matrix and d vector
S_blocks = []
d_blocks = []
weights = []

for vb, vn in zip(v_b_list, v_n_list):
    s_i = vb + vn
    d_i = vb - vn
    S_i = tilde(s_i)
    S_blocks.append(S_i)
    d_blocks.append(d_i)
    weights.append(1.0)  # equal weighting for both vectors

print(S_blocks, d_blocks, weights)

# Stack S and d
S = np.vstack(S_blocks)
d = np.hstack(d_blocks)
W = np.diag(np.repeat(weights, 3))  # 3x3 block diagonal weights

print(S, d, W)

# Compute CRP vector q
STWS = S.T @ W @ S
STWd = S.T @ W @ d

# Find CRPs
q = np.linalg.inv(STWS) @ STWd

def calc_BN_est(q):
    I = np.eye(3)
    q_tilde = tilde(q)
    BN_est = np.linalg.inv(I + q_tilde) @ (I - q_tilde)

    return BN_est

BN_est = calc_BN_est(q)
print(BN_est)