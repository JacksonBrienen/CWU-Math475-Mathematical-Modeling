import matplotlib.pyplot as plt
import numpy as np

def config_plt():
    plt.xlabel("t", fontsize=14)
    plt.ylabel("P(t)", fontsize=14, rotation='horizontal', labelpad=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=14)
    plt.tight_layout()

# Our growth rate in the "best of cases"
r = 0.01676

# Our initial population
P = 100
TARGET = 200

# Our Time Frames
SHORT_TERM = 110
LONG_TERM = 250

def sim(target, initial, r, h):
    p = [initial]

    tau = np.ceil(np.log(target / initial) / np.log(1 + r - h))

    for t in range(1, LONG_TERM + 1):
        if t <= tau:
            p.append(p[-1] * (r + 1 - h))
        elif p[-1] < TARGET:
            p.append(p[-1] * (r + 1) - 3)
        else:
            p.append(p[-1] * (r + 1) - 4)
    return p

p0 = sim(TARGET, P, r, 0)
p1 = sim(TARGET, P, r, 0.005)
p2 = sim(TARGET, P, r, 0.01)

t = np.arange(LONG_TERM + 1)
plt.plot(t, p0, label = "$h = 0$")
plt.plot(t, p1, label = "$h = 0.005$")
plt.plot(t, p2, label = "$h = 0.01$")
plt.plot(t, [200 for _ in range(len(t))], linestyle='--', color='black', alpha=0.5, label = "$P(t) = 200$")
config_plt()
plt.savefig('./hunting_strategy/strategic_model_long_term.png', dpi=300)
plt.close()

t = np.arange(SHORT_TERM + 1)
plt.plot(t, p0[:SHORT_TERM + 1], label = "$h = 0$")
plt.plot(t, p1[:SHORT_TERM + 1], label = "$h = 0.005$")
plt.plot(t, p2[:SHORT_TERM + 1], label = "$h = 0.01$")
plt.plot(t, [200 for _ in range(len(t))], linestyle='--', color='black', alpha=0.5, label = "$P(t) = 200$")
config_plt()
plt.savefig('./hunting_strategy/strategic_model_short_term.png', dpi=300)
plt.close()