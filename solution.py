import matplotlib.pyplot as plt
import numpy as np

f = lambda x, a, b: (b/a) * np.log(x) - x + 1

t = np.linspace(0, 2, 100)

plt.plot(t, f(t, 0.5, 0.33), label=r'$\frac{\beta}{\alpha}=\frac{0.33}{0.5}$')
plt.plot(t, f(t, 1, 1), label=r'$\frac{\beta}{\alpha}=1$')
plt.plot(t, f(t, 0.5, 0.66), label=r'$\frac{\beta}{\alpha}=\frac{0.66}{0.5}$')



plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(-0.5)
plt.xlabel('Time ($t$)', fontsize=14)
plt.ylabel(r'$\frac{\beta}{\alpha}\ln(t)-t+1$', fontsize=14)
plt.legend(fontsize=14)
plt.tight_layout()
plt.grid()
plt.savefig('./plots/solution.png', dpi=200)