import matplotlib.pyplot as plt
import numpy as np

y0_1=0.1
dy0_1=0
y0_2=4
dy0_2=0
mu=1.638
N_steps=10000
t0=0
tf=20*np.pi
h=tf/N_steps
t=np.linspace(t0,tf,N_steps);
y=[];
dy=[];
y=np.append(y,y0_1)
dy=np.append(dy,dy0_1)

def vanderpol(y,dy):
    f=(dy,-y-mu*((y**2)-1)*dy)
    return f
def k1(h,y_n,dy_n,vanderpol):
    f_n=vanderpol(y_n,dy_n)
    return h*f_n[0],h*f_n[1]
def k2(h,y_n,dy_n,vanderpol):
    k_1=k1(h,y_n,dy_n,vanderpol)
    f_n=vanderpol(y_n+(k_1[0]/2.),dy_n+(k_1[1]/2.))
    return h*f_n[0],h*f_n[1]
def k3(h,y_n,dy_n,vanderpol):
    k_1=k1(h,y_n,dy_n,vanderpol)
    k_2=k2(h,y_n,dy_n,vanderpol)
    f_n=vanderpol(y_n-k_1[0]+2*k_2[0],dy_n-k_1[1]+2*k_2[1])
    return h*f_n[0],h*f_n[1]
def rungekutta3(h,y_n,dy_n,vanderpol):
    k_1=k1(h,y_n,dy_n,vanderpol)
    k_2=k2(h,y_n,dy_n,vanderpol)
    k_3=k3(h,y_n,dy_n,vanderpol)
    y_next=y_n+(1/6.)*(k_1[0]+4*k_2[0]+k_3[0])
    dy_next=dy_n+(1/6.)*(k_1[1]+4*k_2[1]+k_3[1])
    return y_next,dy_next

for i in range(1,N_steps):
    new=rungekutta3(h,y[i-1],dy[i-1],vanderpol)
    y=np.append(y,new[0])
    dy=np.append(dy,new[1])

name=plt.figure(1)
name.clf()
first=name.add_subplot(211)
first.plot(t,y)
second=name.add_subplot(212)
second.plot(y,dy)
plt.savefig('grafico1.png')
plt.draw()
plt.show()
