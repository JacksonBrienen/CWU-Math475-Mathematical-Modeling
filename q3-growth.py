import matplotlib.pyplot as plt
import numpy as np

def config_plt():
    plt.xlabel("t", fontsize=14)
    plt.ylabel("P(t)", fontsize=14, rotation='horizontal', labelpad=15)
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()

# Our growth rate in the "best of cases"
r = 0.01676

hs = [0, 0.005, 0.01, 0.015]

# Our initial population
P = 100

ps = [[P] for _ in range(len(hs))]

while ps[-1][-1] < 200:
    for n, h in enumerate(hs):
        ps[n].append(ps[n][-1] * (1 + r - h))

T = len(ps[0])

t = np.arange(T)
for n, h in enumerate(hs):
    plt.plot(t, ps[n], label=f'$h={h}$')
plt.plot(t, [200 for _ in range(T)], label=f'$P(t)=200$', linestyle='--', color='black')

plt.xlim(0, 400)
plt.ylim(50, 300)
config_plt()
plt.savefig('./hunting_strategy/percentage_growth.png', dpi=300)
plt.close()


fs = [0, 1, 2, 3]
ps = [[P] for _ in range(len(fs))]

while ps[1][-1] < 200:
    for n, f in enumerate(fs):
        ps[n].append(ps[n][-1] * (1 + r) - f)

T = len(ps[0])

t = np.arange(T)
for n, f in enumerate(fs):
    plt.plot(t, ps[n], label=f'$f={f}$')
plt.plot(t, [200 for _ in range(T)], label=f'$P(t)=200$', linestyle='--', color='black')

plt.xlim(0, 75)
plt.ylim(50, 250)
config_plt()
plt.legend(fontsize=14, loc='upper left')
plt.savefig('./hunting_strategy/amount_growth.png', dpi=300)
plt.close()