import numpy as np

q = np.array([0.4,0.2,-0.1])

dt = 0.1
t_final = 600
steps = int(t_final/dt) 

crp = np.zeros((steps,3))
crp[0] = [q[0],q[1],q[2]]
body_rate_list = np.zeros((steps,3))

def tilde_mat(vec):
    return np.array([[0,-vec[2],vec[1]],
                     [vec[2],0,-vec[0]],
                     [-vec[1],vec[0],0]])

for t in range(1, steps):
    time = t*dt
    body_rate = np.deg2rad(3*np.array([np.sin(0.1*time),0.01,np.cos(0.1*time)]))

    q = crp[t-1]
    I = np.eye(3)

    B = np.array([[1+q[0]**2, (q[0]*q[1]) -q[2], (q[0]*q[2])+q[1]],
                  [(q[1]*q[0])+q[2], 1+q[1]**2, (q[1]*q[2])-q[0]],
                  [(q[2]*q[0])-q[1], (q[2]*q[1])+q[0], 1+q[2]**2]])

    crp_dot = 0.5*B@body_rate

    # crp_dot = 0.5*(I+tilde_mat(q)+np.dot(q,q.T)) @ body_rate

    crp[t] = crp[t-1] + crp_dot*dt
    # crp[t] = crp[t]/np.linalg.norm(crp[t])
    body_rate_list[t] = body_rate

# Index corresponding to t = 42 seconds
index_42s = int(42 / dt)
q0_42, q1_42, q2_42 = crp[index_42s]

# Vector norm of quaternion (q1, q2, q3)
crp_vec_norm = np.sqrt(q0_42**2 + q1_42**2 + q2_42**2)
print(f"CRP norm at t = 42 s: {crp_vec_norm:.6f}")