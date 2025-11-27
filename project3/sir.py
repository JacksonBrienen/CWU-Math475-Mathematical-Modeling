import numpy as np
from scipy.integrate import solve_ivp

class Model():
    def __init__(self, N, I0):
        S0 = N - I0
        R0 = 0
        # initial values for diff eq
        self.y0 = [S0, I0, R0]

    def simulate(self, t, alpha, beta, intrv=200):
        solution = solve_ivp(
            fun=sir_model,
            t_span=(0 , t),
            y0 = self.y0,
            args=(alpha, beta),
            t_eval=np.linspace(0, t, intrv)
        )
        return solution.t, solution.y


def sir_model(t, y, alpha, beta):
    S, I, R = y
    
    # The differential equations from your image
    dSdt = -alpha * S * I
    dIdt = alpha * S * I - beta * I
    dRdt = beta * I
    
    return [dSdt, dIdt, dRdt]