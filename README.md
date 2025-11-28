# Project 2
## Dependencies
We use Python 3.13.7 with Matplotlib 3.10.6, NumPy 2.3.3, and SciPy 1.16.2.

To install dependencies use `pip install -r requirements.txt`.

## Stochastic Modeling of Bobcat Populations

We continue to model bobcat populations. For the models we investigate, we continue to assume an initial population $P(0)=100$.

### 1. Deterministic Exponential Model

We construct the simple deterministic exponential model, similar to that in [project 1](https://github.com/JacksonBrienen/CWU-Math475-Mathematical-Modeling/tree/project1). We now use a constant birth rate of $b=0.4$ and a survival rate of $s=0.68$, and examine the population over 20 years. This forms the main formula we use for the rest of the paper:

$P(t) = (s+b)P(t-1)$

### 2. Demographic Stochasticity

We now adjust the deterministic model to have birth rates and survival rates vary. So we now have,

$b \sim \mathcal{N}(0.4, 0.01)$

$s \sim \mathcal{N}(0.68, 0.07)$

We conduct 50 trials and compare results with the deterministic model. We conclude this section analyzing how sensitive the model is to the standard deviations of $b$ and $s$.

### 3. Environmental Stochasticity

We now adjust the deterministic model to introduce a catastrophe which occurs every 12 years on average. During a catastrophe birth rates and survival rates both decrease by 30%.

We again conduct 50 trials and compare results with the deterministic model. We analyze how sensitive this model is to the frequency of catastrophes. Finally, we conclude with a comparison to the demographic stochasticity model.
