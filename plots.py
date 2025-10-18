import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.lines as mlines
import numpy as np
from scipy.special import binom

# initial population
P = 100
# time period
T = 20
t = np.arange(T + 1)
# base birth rate
B = 0.4
# base survival rate
S = 0.68

def config_plt(xlabel="t", ylabel="P(t)", legend=True):
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14, rotation='horizontal', labelpad=15)
    if legend:
        plt.legend(fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()

def exponential():
    p = [P]
    for _ in range(T):
        p.append(p[-1] * (B + S))
    plt.plot(t, p, label = f"$P(t)=(b+s)P(t-1)$")
    config_plt()
    plt.xlim(0, 20)
    plt.gca().xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.savefig("./plots/exponential.png", dpi=300)
    plt.close()
    return p

def standard():
    f = lambda mu, sigma, x: (1/(sigma * np.sqrt(2 * np.pi))) * np.exp((-1/2) * np.pow((x-mu)/sigma,2))
    x = np.linspace(0, 1, 200)
    bd = f(B, 0.1, x)
    sd = f(S, 0.07, x)
    plt.plot(x, bd, color='blue', label = r'$\mathcal{N}(0.4, 0.1)$')
    plt.plot([0.4, 0.4], [0, 6], color='blue', linestyle='--', label = '$x = 0.4$')
    plt.plot(x, sd, color='orange', label = r'$\mathcal{N}(0.68, 0.07)$')
    plt.plot([0.68, 0.68], [0, 6], color='orange', linestyle='--', label = '$x = 0.68$')
    config_plt(xlabel='$x$', ylabel='$f(x)$')
    plt.ylim(-0.1, 6)
    plt.savefig("./plots/standard-distribution.png", dpi=300)
    plt.close()

def demographic(exp_p, bdev=0.1, sdev=0.07, fname="./plots/demographic.png"):
    trials = 50
    p = [[P] for _ in range(trials)]
    b = np.random.normal(B, bdev, (trials, T))
    s = np.random.normal(S, sdev, (trials, T))
    for year in range(T):
        for trial in range(trials):
            p[trial].append(p[trial][-1] * (b[trial][year] + s[trial][year]))
    
    p_med = np.median(p, axis=0)
    p_avg = np.mean(p, axis=0)
    p_min = np.min(p, axis=0)
    p_max = np.max(p, axis=0)
    p_err = np.array([p_avg - p_min, p_max - p_avg])
    # plt.errorbar(t, p_avg, yerr=p_err, fmt='o', capsize=5, label='Average w/ Error', zorder=1)
    
    plt.plot(t, p_max, label="Maximum")
    plt.plot(t, p_med, label="Median")
    plt.plot(t, p_min, label="Minimum")
    plt.plot(t, exp_p, label="Standard", linestyle='--', color='black', alpha=0.5)
    
    config_plt()
    plt.xlim(0, 20)
    plt.gca().xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.savefig(fname, dpi=300)
    plt.close()

def environmental_classes():
    dead = 0
    ok = 0
    well = 0
    p = []
    for year in t:
        pop = [P]
        for _ in range(year):
            pop.append(pop[-1] * (B+S-0.6))
        for _ in range(T-year):
            pop.append(pop[-1] * (B+S))
        c = 'red' if np.any(np.array(pop) < 1) else ('green' if pop[-1] >= P else 'blue')
        if c == 'red':
            dead += 1
        elif c == 'blue':
            ok += 1
        else:
            well += 1
        plt.plot(t, pop, linestyle = '--', color = c)
        p.append(pop)

    well_line = mlines.Line2D([], [], color='green', linestyle='--', label=f'$P(20)>P(0)$: {well}')
    ok_line = mlines.Line2D([], [], color='blue', linestyle='--', label=fr'$P(20) \geq 1$: {ok}')
    dead_line = mlines.Line2D([], [], color='red', linestyle='--', label=f'$P(20) < 1$: {dead}')
    handles, _ = plt.gca().get_legend_handles_labels()
    handles.extend([well_line, ok_line, dead_line])
    # handles.append(ok_line)
    # handles.append(dead_line)

    config_plt(legend=False)
    plt.legend(fontsize=14, handles = handles)
    plt.xlim(0, 20)
    plt.gca().xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.savefig("./plots/environmental_classes.png", dpi=300)
    plt.close()
    print('dead:', dead)
    print('ok:', ok)
    print('well:', well)
    return p
            


def environmental(cls_p):
    # odds of a catastrophe
    catastrophe = 1.0/12.0
    # catastrophe birth and survival rates
    CB = B - 0.3
    CS = S - 0.3

    trials = 100
    p = [[P] for _ in range(trials)]

    # generate catastrophe chances
    rng = np.random.default_rng()
    env = rng.random(size=(trials, T))
    for year in range(T):
        for trial in range(trials):
            if env[trial][year] < catastrophe:
                p[trial].append(p[trial][-1] * (CB + CS))
            else:
                p[trial].append(p[trial][-1] * (B + S))

    p_avg = np.mean(p, axis=0)
    p_min = np.min(p, axis=0)
    p_max = np.max(p, axis=0)

    plt.plot(t, p_max, label = 'Maximum')
    plt.plot(t, p_avg, label = 'Average')
    plt.plot(t, p_min, label = 'Minimum')
    plt.plot(t, cls_p[1], label = r'$\sigma(20)=1$', linestyle='--', color='green')
    plt.plot(t, cls_p[2], label = r'$\sigma(20)=2$', linestyle='--', color='blue')
    config_plt()
    plt.savefig("./plots/environmental.png", dpi=300)
    plt.close()

def catastrophe_rate():
    rate = lambda x, odds: binom(T, x) * np.pow(odds,x) * np.pow(1-odds, T - x)
    c = np.linspace(0, 15, 300)
    plt.plot(c, rate(c, 1/12), label = r'$c_r = \frac{1}{12}$')
    plt.plot(c, rate(c, 1/6), label = r'$c_r = \frac{1}{6}$')
    plt.plot(c, rate(c, 1/3), label = r'$c_r = \frac{1}{3}$')
    plt.plot([7, 7], [0, 0.35], label = r'$c = 7$', linestyle = '--', color = 'black')
    config_plt(xlabel='$c$', ylabel=r'$\lambda(c, c_r)$')
    plt.xlim(0,14)
    plt.ylim(0, 0.35)
    plt.savefig("./plots/catastrophe_rate.png", dpi=300)
    plt.close()


if __name__ == '__main__':
    # p = exponential()
    # standard()
    # demographic(p)
    # demographic(p, bdev=0.2, sdev=0.14, fname="./plots/demographic_higher_dev.png")
    # cls = environmental_classes()
    # environmental(cls)
    catastrophe_rate()
