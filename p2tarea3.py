import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

sigma=10
beta=8/3.
rho=28

x0=3
y0=3
z0=3
f0=[x0,y0,z0]
s0=0

def f_to_solve(s,f,o=sigma,b=beta,r=rho):
    x,y,z=f
    return [o*(y-x),x*(r-z)-y,x*y-b*z]

r=ode(f_to_solve)
r.set_integrator('dopri5',max_step=0.1,first_step=0.01)
r.set_initial_value(f0,s0)

s=np.linspace(s0,100,10000)
x=np.zeros(len(s))
y=np.zeros(len(s))
z=np.zeros(len(s))

for i in range(len(s)):
    r.integrate(s[i])
    x[i],y[i],z[i]=r.y

fig=plt.figure(1)
fig.clf()
ax=fig.add_subplot(111,projection='3d')
ax.set_aspect('auto')
ax.plot(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('grafico2.png')
plt.show()
