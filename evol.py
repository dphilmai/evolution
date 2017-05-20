from scipy.integrate import odeint
from scipy.optimize import newton
import numpy as  np
import matplotlib.pyplot as plt
t = np.linspace(0,10,100)
def repdyn(x,t,a1,a2):
    return (x**2)*(a1 + 2*a2) - (x**3)*(a1+a2) - x*(a2)
def poly(x,a1,a2):
    return (x**2)*(a1 + 2*a2) - (x**3)*(a1+a2) - x*(a2)  
def polynominal(x,t):
    return x*((x-x**2) + 3*(2*x-1-x**2))
def repaug(x,t,a1,a2,eps):
    return (x**2)*(a1+2*a2+3*eps) - (x**3)*(a1+a2+2*eps) - x*(a2+eps)
def repaug1(x,t,a1,a2,eps):
    return (x**2)*(a1+2*a2+eps*x) - (x**3)*(a1+a2+eps*x) - x*(a2)
def repaug2(x,t,a1,a2,eps,gamma):
    return (x**2)*(a1+2*a2+eps*x**gamma)-(x**3)*(a1+a2+eps*x**gamma)-x*(a2)

def repgen(x,t,a1,a2,eps,delta,gamma1,gamma2):
    return (x**2)*(a1+eps*x**gamma1+2*(a2+delta*x**gamma2)) - (x**3)*(a1+eps*x**gamma1+a2+delta*x**gamma2) - x*(a2+delta*x**gamma2)
def repgenroot(x):
    a =5
    b =0
    c =4
    d =3
    gamma1=2
    gamma2=1
    delta=1
    eps=1
    a1 = a-c
    a2 = d-b  
    return (x**2)*(a1+eps*x**gamma1+2*(a2+delta*x**gamma2)) - (x**3)*(a1+eps*x**gamma1+a2+delta*x**gamma2) - x*(a2+delta*x**gamma2)
a =5
b =0
c =4
d =3
gamma1=2
gamma2=1
delta=1
eps=1
a1 = a-c
a2 = d-b  
x = np.linspace(0,1,100)
root = newton(repgenroot,0.8)
print(root)
plt.plot(x,repgen(x,t,a1,a2,eps,delta,gamma1,gamma2))
plt.show()
#for i in range(1,10):
#    x0 = i/10
#    sol = odeint(repdyn,x0,t,args=(a1,a2))
#    plt.plot(t,sol)
#plt.show()
runs=10
for i in range(1,runs):
    x0 = i/runs
    sol = odeint(repgen,x0,t,args=(a1,a2,eps,gamma1,gamma2,delta))
    plt.plot(t,sol)
plt.plot(t,sol)
plt.show()
