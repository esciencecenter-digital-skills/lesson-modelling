# Load libraries
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Set initial value problem
## Dynamics
def dydt(y, t):
    return 0.1*y

## Initial value
y0 = 0.5

# Set times to solve for
ts = np.linspace(0, 10, 100)

# Integrate numerically
ys = odeint(dydt, y0, ts)

# Plot solution
plt.plot(ts, ys)
plt.show()
