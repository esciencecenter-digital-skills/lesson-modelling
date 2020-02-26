# Load libraries
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Set initial value problem
## Dynamics
def dydt(y, t, b = 1, g = 0.1, m = 0):
    S, I, R = y
    return [- b*S*I,
            + b*S*I - g*I - m*I,
                    + g*I]
## Initial value
y0 = (0.99, 0.01, 0)

# Set times to solve for
ts = np.linspace(0, 100, 1000)

# Integrate numerically
b = 0.5
g = 0.1
m = 0.05
ys = odeint(dydt, y0, ts, args = (b, g, m))

# Extract information
Ss = ys[:, 0]
Is = ys[:, 1]
Rs = ys[:, 2]
Ds = 1 - Ss - Is - Rs

# Plot information
plt.plot(ts, Ss, label = 'S')
plt.plot(ts, Is, label = 'I')
plt.plot(ts, Rs, label = 'R')
plt.plot(ts, Ds, label = 'D')
plt.legend()
plt.show()
