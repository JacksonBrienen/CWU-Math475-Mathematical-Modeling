import matplotlib.pyplot as plt
import numpy as np

# Our growth rate in the "best of cases"
r = -0.045

# Our initial population
P = 100

# Our two time frames
SHORT_TERM = 30
LONG_TERM = 70

# fixed hunting amounts
f = [3, 4, 5, 6]

# populations for each hunting type
p = [[P] for _ in range(len(f))]

# Now we gather our "simulation" data
# Following the equation P(t) = P(t-1) * (r + 1) - f for amount hunting
for _ in range(LONG_TERM ):
    for i in range(len(f)):
        p[i].append(p[i][-1] * (r + 1) + f[i])

def config_plt():
    plt.xlabel("t", fontsize=14)
    plt.ylabel("P(t)", fontsize=14, rotation='horizontal', labelpad=15)
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()

# Plot the collected data for amount hunting
t = np.arange(SHORT_TERM + 1)
for i, pop in enumerate(p):
    plt.plot(t, pop[:SHORT_TERM + 1], label = f"$f = {f[i]}$")
config_plt()
plt.savefig('./introduction/amount_short_term.png', dpi=300)
plt.close()

t = np.arange(LONG_TERM + 1)
for i, pop in enumerate(p):
    plt.plot(t, pop, label = f"$f = {f[i]}$")
config_plt()
plt.savefig('./introduction/amount_long_term.png', dpi=300)
plt.close()