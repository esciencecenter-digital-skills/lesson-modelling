# Load libraries
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Set initial value problem
## Dynamics
def dydt(y, t, r = 1, k = 1):
    return r*y*(1 - y / k)

## Initial value
y0 = 0.1

# Set times to solve for
ts = np.linspace(0, 30, 100)

# Integrate numerically
ys = odeint(dydt, y0, ts, args = (0.5, 25))

# Plot solution
plt.plot(ts, ys)
plt.show()
