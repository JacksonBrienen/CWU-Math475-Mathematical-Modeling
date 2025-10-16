import matplotlib.pyplot as plt
import numpy as np

# Our growth rate in the "best of cases"
r = -0.045

# Our initial population
P = 100

# Our two time frames
SHORT_TERM = 60
LONG_TERM = 150

# fixed hunting amounts
f = [3, 2, 2, 2]

# populations for each hunting type
p = [P]

# Now we gather our "simulation" data
# Following the equation P(t) = P(t-1) * (r + 1) - f for amount hunting
for t in range(1, LONG_TERM + 1):
    p.append(p[-1] * (r + 1) + f[t % 4])

def config_plt():
    plt.xlabel("t", fontsize=14)
    plt.ylabel("P(t)", fontsize=14, rotation='horizontal', labelpad=15)
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()

# Plot the collected data for amount hunting
t = np.arange(SHORT_TERM + 1)
plt.plot(t, p[:SHORT_TERM + 1], label = r"$f = \overline{2.25}$")
plt.plot(t, [50 for _ in range(len(t))], linestyle='--', color='black', alpha=0.5, label = "$P(t) = 50$")
config_plt()
plt.savefig('./introduction_strategy/50_short_term.png', dpi=300)
plt.close()

t = np.arange(LONG_TERM + 1)
plt.plot(t, [50 for _ in range(len(t))], linestyle='--', color='black', alpha=0.5, label = "$P(t) = 50$")
plt.plot(t, p, label = r"$f = \overline{2.25}$")
config_plt()
plt.savefig('./introduction_strategy/50_long_term.png', dpi=300)
plt.close()