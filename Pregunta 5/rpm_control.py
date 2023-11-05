#### ICM2813: Drone height control ####
# 
# Professor: David E. Acuña-Ureta, PhD
# E-mail: david.acuna@uc.cl
#
#######################################

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib import animation


#### Parameters and variables ####

# Model parameters
g = 9.8                     # gravity acceleration
m = 0.27                    # drone mass
l = 0.2                     # radius of the drone (spherical approximation)
viscosity = 0.0000174       # viscosity: air = 0.0000174; hidrogen = 0.00084; xenon = 0.000212
cf = 6*np.pi*viscosity*l    # friction coefficient

# Simulation parameters
Th = 40     # time horizon
Ts = 0.03   # sample time
t0 = 0.0    # initial time
ref = 300     # reference rpm
theta0 = 0.0    # initial condition for position
w0 = 0.0   # initial condition for w
c0 = 0.0    # initial control
Kp = 1.5    # controller: proportional
Ki = 0.2    # controller: integrative
Kd = 0.3    # controller: derivative

# Variables
t = [t0]        # time signal
theta = [theta0]        # position signal
w = [w0]      # velocity signal
c = [c0]        # control signal
e = [0.0, 0.0, 0.0]  # error signal

#### Simulation ####

def model(z, t, c):
    w = z[1]
    d_theta = w
    return [d_theta]

while(t[-1] < Th):
    t.append(t[-1] + Ts)
    e.append(ref - w[-1])
    c.append(c[-1] + (Kp + Ts*Ki + Kd/Ts)*e[-1] + (-Kp - 2*Kd/Ts)*e[-2] + (Kd/Ts)*e[-3])
    sol = odeint(model, [theta[-1], w[-1]], t[-2:], (c[-1],))
    theta.append(sol[1, 0])
    w.append(sol[1, 1])

plt.plot(t, theta)
plt.ylabel('Altura (m)')
plt.xlabel('Tiempo (s)')
plt.show()