import matplotlib.pyplot as plt
from sir import Model

m = Model(1,1/100)
t, y = m.simulate(65, 0.5, 0.33)

plt.plot(t, y[0], 'y-', label='Susceptible ($S$)')
plt.plot(t, y[1], 'r-', label='Infected ($I$)')
plt.plot(t, y[2], 'g-', label='Recovered ($R$)')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Time ($t$)', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.legend(fontsize=14)
plt.tight_layout()
plt.savefig('./plots/simple.png', dpi=200)
plt.close()

t, y = m.simulate(65, 0.5/2, 0.33)

plt.plot(t, y[0], 'y-', label='Susceptible ($S$)')
plt.plot(t, y[1], 'r-', label='Infected ($I$)')
plt.plot(t, y[2], 'g-', label='Recovered ($R$)')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Time ($t$)', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.legend(fontsize=14)
plt.tight_layout()
plt.savefig('./plots/covid.png', dpi=200)