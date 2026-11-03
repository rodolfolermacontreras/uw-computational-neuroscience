"""
Week 6 quiz Q9: steady-state output of a linear recurrent network.

tau dv/dt = -v + W.u + M.v  ->  steady state (dv/dt = 0):
    v_ss = W.u + M.v_ss
    (I - M) v_ss = W.u
    v_ss = (I - M)^-1 (W.u)
"""
import numpy as np

W = np.array([
    [0.6, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.6, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.6, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.6, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.6],
])

u = np.array([0.6, 0.5, 0.6, 0.2, 0.1])

M = np.array([
    [-0.125, 0, 0.125, 0.125, 0],
    [0, -0.125, 0, 0.125, 0.125],
    [0.125, 0, -0.125, 0, 0.125],
    [0.125, 0.125, 0, -0.125, 0],
    [0, 0.125, 0.125, 0, -0.125],
])

if __name__ == "__main__":
    I = np.eye(5)
    h = W @ u
    v_ss = np.linalg.solve(I - M, h)
    print("h = W.u =", h)
    print("v_ss   =", v_ss)
    print("v_ss (rounded) =", np.round(v_ss, 3))
