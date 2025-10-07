import matplotlib.pyplot as plt
import numpy as np

# Our three growth rates
r = [0.01676, 0.00549, -0.04500]

# Our initial population
P = 100

# Our two time frames
SHORT_TERM = 30
LONG_TERM = 70

# Our three different populations
p = [[P], [P], [P]]

# Now we gather our "simulation" data
# Following the equation P(t) = P(t-1) * (r + 1)
for _ in range(LONG_TERM ):
    for i in range(3):
        p[i].append(p[i][-1] * (r[i] + 1))

def config_plt():
    plt.xlabel("t", fontsize=14)
    plt.ylabel("P(t)", fontsize=14, rotation='horizontal', labelpad=15)
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()

# Plot the collected data for short term
t = np.arange(SHORT_TERM + 1)
for i, pop in enumerate(p):
    plt.plot(t, pop[:SHORT_TERM + 1], label = f"$r = {r[i]}$")
config_plt()
plt.savefig('./basic/short_term.png', dpi=300)
plt.close()

# Plot the collected data for long term
t = np.arange(LONG_TERM + 1)
for i, pop in enumerate(p):
    plt.plot(t, pop, label = f"$r = {r[i]}$")
config_plt()
plt.savefig('./basic/long_term.png', dpi=300)
plt.close()