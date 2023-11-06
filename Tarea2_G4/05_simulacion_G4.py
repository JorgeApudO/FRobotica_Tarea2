#### ICM2813: Drone height control ####
# 
# Professor: David E. Acuña-Ureta, PhD
# E-mail: david.acuna@uc.cl
#
#######################################

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#### Parameters and variables ####

# Model parameters
sigma = 4.398 #sigma in motor 1 4V defined in Pregunta 4
A = 57.591 #A in motor 1 4V defined in Pregunta 4

# Simulation parameters
Th = 7  # time horizon
Ts = 0.01  # sample time
t0 = 0.0    # initial time
ref = 250    # reference
y0 = 0.0    # initial condition for position
dy0 = 0.0   # initial condition for velocity
c0 = 0.0    # initial control
Kp = 0.21  # controller: proportional
Ki = 0.1 # controller: integrative
Kd = 0 # controller: derivative

# Variables
t = [t0]        # time signal
y = [y0]        # position signal
dy = [dy0]      # velocity signal
c = [c0]        # control signal
e = [0.0, 0.0]  # error signal


#### Simulation ####

def model(z, t, c):
    return np.array([z[1], sigma*A*c - sigma*z[1]])  # y'' = sigma*A*c - sigma*y' 


while(t[-1] < Th):
    t.append(t[-1] + Ts)
    e.append(ref - dy[-1])
    c.append(c[-1] + (Kp + Ts*Ki + Kd/Ts)*e[-1] + (-Kp - 2*Kd/Ts)*e[-2] + (Kd/Ts)*e[-3])
    sol = odeint(model, [y[-1], dy[-1]], t[-2:], (c[-1],))
    y.append(sol[1, 0])
    dy.append(sol[1, 1])

plt.plot(t, dy)
plt.ylabel('Velocidad (RPM)')
plt.xlabel('Tiempo (s)')
plt.show()

