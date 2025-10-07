import matplotlib.pyplot as plt
import numpy as np

# Our growth rate in the "best of cases"
r = 0.01676

# Our initial population
P = 100

# Our two time frames
SHORT_TERM = 30
LONG_TERM = 70

# fixed amount hunting rates
fixed_amount = [1, 2, 3, 4]

# fixed percentage hunting rates
fixed_percent = [0.005, 0.01, 0.015, 0.02] # 0.5% to 2%

# populations for each hunting type
fa_pop = [[P] for _ in range(4)]
fp_pop = [[P] for _ in range(4)]

# Now we gather our "simulation" data
# Following the equation P(t) = P(t-1) * (r + 1) - f for fixed hunting
# Following the equation P(t) = P(t-1) * (r + 1 - f) for percentage hunting
for _ in range(LONG_TERM ):
    for i in range(4):
        fa_pop[i].append(fa_pop[i][-1] * (r + 1) - fixed_amount[i])
        fp_pop[i].append(fp_pop[i][-1] * (r + 1 - fixed_percent[i]))

def config_plt():
    plt.xlabel("t", fontsize=14)
    plt.ylabel("P(t)", fontsize=14, rotation='horizontal', labelpad=15)
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()

# Plot the collected data for fixed hunting
t = np.arange(SHORT_TERM + 1)
for i, pop in enumerate(fa_pop):
    plt.plot(t, pop[:SHORT_TERM + 1], label = f"$f = {fixed_amount[i]}$")
config_plt()
plt.savefig('./hunting/fixed_short_term.png', dpi=300)
plt.close()

t = np.arange(LONG_TERM + 1)
for i, pop in enumerate(fa_pop):
    plt.plot(t, pop, label = f"$f = {fixed_amount[i]}$")
config_plt()
plt.savefig('./hunting/fixed_long_term.png', dpi=300)
plt.close()

# Plot the collected data for percentage hunting
t = np.arange(SHORT_TERM + 1)
for i, pop in enumerate(fp_pop):
    plt.plot(t, pop[:SHORT_TERM + 1], label = f"$f = {fixed_percent[i]}$")
config_plt()
plt.savefig('./hunting/percentage_short_term.png', dpi=300)
plt.close()

t = np.arange(LONG_TERM + 1)
for i, pop in enumerate(fp_pop):
    plt.plot(t, pop, label = f"$f = {fixed_percent[i]}$")
config_plt()
plt.savefig('./hunting/percentage_long_term.png')
plt.close()