from scipy.integrate import odeint
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
def repaug2(x,t,a1,a2,eps):
    return (x**2)*(a1+2*a2+eps*x**2)-(x**3)*(a1+a2+eps*x**2)-x*(a2)
a =5
b =0
c =4
d =3
eps=1
a1 = a-c
a2 = d-b  
x = np.linspace(0,1,100)
plt.plot(t,repaug2(x,t,a1,a2,eps))
plt.show()
#for i in range(1,10):
#    x0 = i/10
#    sol = odeint(repdyn,x0,t,args=(a1,a2))
#    plt.plot(t,sol)
#plt.show()
for i in range(1,100):
    x0 = i/100
    sol = odeint(repaug2,x0,t,args=(a1,a2,eps))
    plt.plot(t,sol)
plt.plot(t,sol)
plt.show()
