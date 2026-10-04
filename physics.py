#physics.py

import math

def small_angle_pendulum(A, t, angular_freq):
    theta = A * math.cos(angular_freq * t)
    omega = -A * angular_freq * math.sin(angular_freq * t)
    alpha = - (angular_freq ** 2) * theta
    return theta, omega, alpha

def rk4_step(theta_0, omega_0, angular_freq, dt):
    def f_pp(x):
        return -(angular_freq ** 2) * math.sin(x)
    
    k1 = omega_0 * dt 
    m1 = dt * f_pp(theta_0)

    k2 = dt * (omega_0 + 0.5 * m1)
    m2 = dt * f_pp(theta_0 + 0.5 * k1)

    k3 = dt * (omega_0 + 0.5 * m2)
    m3 = dt * f_pp(theta_0 + 0.5 * k2)

    k4 = dt * (omega_0 + m3)
    m4 = dt * f_pp(theta_0 + k3)

    theta = theta_0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    omega = omega_0 + (m1 + 2 * m2 + 2 * m3 + m4) / 6

    return theta, omega, f_pp(theta)


