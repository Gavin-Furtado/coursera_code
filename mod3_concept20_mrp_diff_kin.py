import numpy as np

mrp = np.zeros([60,3])
mrp[0] = np.array([0.4,0.2,-0.1])

# Time
dt = 1 # second
t_final = 60
t = np.arange(0,t_final,dt)



def rk4(f, y0, t, args=()):
    """
    Runge-Kutta 4th Order Integrator

    Parameters:
    - f     : function dy/dt = f(t, y, *args)
    - y0    : initial condition (can be scalar or vector)
    - t     : array of time points (must be evenly spaced)
    - args  : additional arguments for function f

    Returns:
    - y     : array of integrated values at each time step
    """
    y = np.zeros((len(t), len(np.atleast_1d(y0))))
    y[0] = y0

    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        ti = t[i - 1]
        yi = y[i - 1]

        k1 = f(ti,         yi,          *args)
        k2 = f(ti + dt/2,  yi + dt/2*k1, *args)
        k3 = f(ti + dt/2,  yi + dt/2*k2, *args)
        k4 = f(ti + dt,    yi + dt*k3,   *args)

        y[i] = yi + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

        # Short rotation check
        if np.dot(y[i], y[i]) > 1:
            y[i] = -y[i] / np.dot(y[i], y[i])

    return y

def tilde(vec):
    return np.array([[0, -vec[2], vec[1]],
                     [vec[2],0,-vec[0]],
                     [-vec[1],vec[0],0]])

def calc_mrp_dot(t, sigma, *args):
    """Computes MRP time derivative using the kinematic equation."""
    # Angular velocity in body frame [deg/s]
    omega = 20 * np.array([
        np.sin(0.1 * t),
        0.01,
        np.cos(0.1 * t)
    ])
    omega = np.deg2rad(omega)  # Convert to radians

    sig_norm = np.dot(sigma, sigma)
    I = np.eye(3)
    sigma_tilde = tilde(sigma)
    B = (1 - sig_norm) * I + 2 * sigma_tilde + 2 * np.outer(sigma, sigma)
    sigma_dot = 0.25 * B @ omega
    return sigma_dot

sigma = rk4(calc_mrp_dot,mrp[0],t)

# Find norm at t = 42 seconds
sigma_42 = sigma[42]
norm_sigma_42 = np.linalg.norm(sigma_42)

print(f"MRP at t = 42 sec: {sigma_42}")
print(f"MRP norm at t = 42 sec: {norm_sigma_42:.6f}")