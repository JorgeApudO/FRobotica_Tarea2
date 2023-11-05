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
sigma = 7.13*10**(-6) #sigma in motor 1 defined in Pregunta 4
A = 40.82 #A in motor 1 defined in Pregunta 4

# Simulation parameters
Th = 1000  # time horizon
Ts = 0.03   # sample time
t0 = 0.0    # initial time
ref = 80     # reference
y0 = 0.0    # initial condition for position
dy0 = 0.0   # initial condition for velocity
c0 = 0.0    # initial control
Kp = 0.21   # controller: proportional
Ki = 0.1   # controller: integrative
Kd = 0.00  # controller: derivative

# Variables
t = [t0]        # time signal
y = [y0]        # position signal
dy = [dy0]      # velocity signal
c = [c0]        # control signal
e = [0.0, 0.0]  # error signal


# Animation
bool_animate = False # bool to either generate a MP4 file (True) or not (False)


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


#### Animation ####

if bool_animate:
    fig = plt.figure()
    ax = plt.axes(xlim=(-5, 5), ylim=(-1, max(y) + 1.5))
    drone = mpimg.imread('drone.png')
    imagebox = OffsetImage(drone, zoom=0.5)
    ab = AnnotationBbox(imagebox, (0.0, 0.0), xycoords='data', frameon=False)

    def init():
        ax.add_artist(ab)
        return ab,

    def animate(i):
        ab.xybox = (0, y[i])
        return ab,

    subsampling = 1
    anim = animation.FuncAnimation(fig, animate,
                                init_func=init,
                                frames=range(0,len(y)-1, subsampling),
                                interval=int(Ts*subsampling*1000),
                                blit=True)

    anim.save('height_control.mp4', writer = 'ffmpeg', fps = len(y)//Th)
    #anim.save('height_control.gif', writer=animation.PillowWriter(fps=30))