import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 1. Define the SIR model function
# This function takes time (t), the state variables (y), and parameters (alpha, beta)
# y is a list [S, I, R]
def sir_model(t, y, alpha, beta):
    S, I, R = y
    
    # The differential equations from your image
    dSdt = -alpha * S * I
    dIdt = alpha * S * I - beta * I
    dRdt = beta * I
    
    return [dSdt, dIdt, dRdt]

# 2. Set the parameters (alpha and beta)
# We assume some known values for this example
# beta = 0.08 0.0734
# beta = 0.0734
beta = 0.0734
alpha = beta*(np.log(0.332)/(0.332 - 1))  # Transmission rate coefficient
     # Recovery rate (1/beta = avg. recovery time, e.g., 10 days)

# 3. Set the initial conditions
N = 1.0       # Total population
I0 = 15/250         # Initial number of infected
R0 = 0.0         # Initial number of recovered
S0 = N - I0 - R0   # Initial number of susceptible
y0 = [S0, I0, R0]  # Initial state vector

# 4. Set the time span to solve for
# We'll solve for 150 time units (e.g., days)
t_span = (0, 110)
# Get output at specific points (e.g., every day)
t_eval = np.linspace(t_span[0], t_span[1], 111)

err1 = 10000
err2 = 10000
best = 1
for b in range(600, 900):
    bt = b * 0.0001
    at = bt*(np.log(0.332)/(0.332 - 1))
    other_solution = solve_ivp(
        fun=sir_model, 
        t_span=t_span, 
        y0=y0, 
        args=(at, bt),
        t_eval=[0, 16, 31, 47, 62, 78, 109]
    )

    e1 = np.sum(np.abs(other_solution.y[0] - np.array([235/250, 201/250, 153.5/250, 121/250, 108/250, 97/250, 83/250])))
    e2 = np.sum(np.abs(other_solution.y[1] - np.array([15/250, 22/250, 29/250, 21/250, 8/250, 8/250, 0/250])))
    if (e1 < err1 and e2 < err2):
        err1 = e1
        err2 = e2
        best = bt
print(best)
print(err1)
print(err2)

# 5. Solve the ODE system
# 'args' passes the parameters to the model function
solution = solve_ivp(
    fun=sir_model, 
    t_span=t_span, 
    y0=y0, 
    args=(alpha, beta),
    t_eval=t_eval
)

other_solution = solve_ivp(
    fun=sir_model, 
    t_span=t_span, 
    y0=y0, 
    args=(alpha, beta),
    t_eval=[0, 16, 31, 47, 62, 78, 109]
)
print(np.sum(np.abs(other_solution.y[0] - np.array([235/250, 201/250, 153.5/250, 121/250, 108/250, 97/250, 83/250]))))
print(np.sum(np.abs(other_solution.y[1] - np.array([15/250, 22/250, 29/250, 21/250, 8/250, 8/250, 0/250]))))
# 6. Plot the results
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label='Susceptible (S)')
plt.plot(solution.t, solution.y[1], label='Infected (I)')
plt.scatter(
    [0, 16, 31, 47, 62, 78, 109],
    [235/250, 201/250, 153.5/250, 121/250, 108/250, 97/250, 83/250],
    label = "Data Susceptible"
)
plt.scatter(
    [0, 16, 31, 47, 62, 78, 109],
    [15/250, 22/250, 29/250, 21/250, 8/250, 8/250, 0/250],
    label = "Data Infected"
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Time ($t$)', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.legend(fontsize=14)
plt.tight_layout()
plt.savefig('./plots/exp2.png')