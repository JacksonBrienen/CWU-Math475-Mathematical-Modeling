# Project 3
## Dependencies
We use Python 3.13.7 with Matplotlib 3.10.6, NumPy 2.3.3, and SciPy 1.16.2.

To install dependencies use `pip install -r requirements.txt`.

## Modeling Pandemics

We model pandemics using the basic SIR model. Where $S(t)$ is the population susceptible to a disease, $I(t)$ is the population infected by a disease, and $R(t)$ is the population recovered from a disease. The constants $\alpha$ and $\beta$ represent the infection rate and recovery rate. This forms the following differential system:

$S' = -\alpha SI$

$I' = \alpha SI - \beta I$

$R' = \beta I$

### 1. Model Behavior
We begin by using $\alpha = 0.5$ and $\beta = 0.33$ and analyze both short term and long term behavior.

### 2. Changing of Constants
We analyze how changes in the $\alpha$ and $\beta$ constants affect the behavior of the model.

### 3. Social Distancing
We look at how social distancing can effect the outcomes of a pandemic.

### 4. Comparing to Real Data
We use some real-world data to find allow use to build an SIR model which best fits it. This introduces the basic concept of parameter estimation.
