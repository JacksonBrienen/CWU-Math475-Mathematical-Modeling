import matplotlib.pyplot as plt
import numpy as np

# Our growth rate in the "best of cases"
r = 0.01676

# Our initial population
P = 100

# Our two time frames
SHORT_TERM = 30
LONG_TERM = 70

# fixed percentage hunting rates
h = [0, 0.01, r, 0.02]

# populations for each hunting type
p = [[P] for _ in range(len(h))]

# Now we gather our "simulation" data
# Following the equation P(t) = P(t-1) * (r + 1 - h) for percentage hunting
for _ in range(LONG_TERM ):
    for i in range(len(h)):
        p[i].append(p[i][-1] * (r + 1 - h[i]))

def config_plt():
    plt.xlabel("t", fontsize=14)
    plt.ylabel("P(t)", fontsize=14, rotation='horizontal', labelpad=15)
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()

# Plot the collected data for percentage hunting
t = np.arange(SHORT_TERM + 1)
for i, pop in enumerate(p):
    plt.plot(t, pop[:SHORT_TERM + 1], label = f"$h = {h[i]}$")
config_plt()
plt.savefig('./hunting/percentage_short_term.png', dpi=300)
plt.close()

t = np.arange(LONG_TERM + 1)
for i, pop in enumerate(p):
    plt.plot(t, pop, label = f"$h = {h[i]}$")
config_plt()
plt.savefig('./hunting/percentage_long_term.png', dpi=300)
plt.close()