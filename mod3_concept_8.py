import numpy as np

q = np.array([0.408248,0.0,0.408248,0.816497])

dt = 0.1
t_final = 600
steps = int(t_final/dt) 

quat = np.zeros((steps,4))
quat[0] = [q[0],q[1],q[2],q[3]]
body_rate_list = np.zeros((steps,3))

for t in range(1,steps):
    time = t*dt
    body_rate = np.deg2rad(20*np.array([np.sin(0.1*time),0.01,np.cos(0.1*time)]))
    
    q = quat[t-1]

    init_quat_mat = 0.5*np.array([[-q[1],-q[2],-q[3]],
                              [q[0],-q[3],q[2]],
                              [q[3],q[0],-q[1]],
                              [-q[2],q[1],q[0]]])
    quat_dot = init_quat_mat @ body_rate

    quat[t] = quat[t-1] + quat_dot*dt
    quat[t] = quat[t]/np.linalg.norm(quat[t])
    body_rate_list[t] = body_rate

# Index corresponding to t = 42 seconds
index_42s = int(42 / dt)
q0_42, q1_42, q2_42, q3_42 = quat[index_42s]

# Vector norm of quaternion (q1, q2, q3)
quat_vec_norm = np.sqrt(q1_42**2 + q2_42**2 + q3_42**2)
print(f"Quaternion vector norm at t = 42 s: {quat_vec_norm:.6f}")