from scipy.integrate import odeint
from scipy.optimize import newton
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
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
    gamma1=1
    gamma2=0
    delta=0
    eps=3
    a1 = a-c
    a2 = d-b  
    return (x**2)*(a1+eps*x**gamma1+2*(a2+delta*x**gamma2)) - (x**3)*(a1+eps*x**gamma1+a2+delta*x**gamma2) - x*(a2+delta*x**gamma2)
fs=15
a =5
b =0
c =4
d =3
gamma1=1
gamma2=0
delta=0
eps=3
a1 = a-c
a2 = d-b  
x = np.linspace(0,1,100)
root = newton(repgenroot,0.5)
print(root)
plt.plot(x,repgen(x,t,a1,a2,eps,delta,gamma1,gamma2))
axis=plt.gca()
axis.set_xlim([0,1])
plt.axhline(y=0,c='0.7',ls='dashed')
plt.axvline(x=root,c='0.7',ls='dashed')
plt.xlabel(r'$x$',fontsize=fs)
plt.ylabel(r'$\varphi(x)$',fontsize=fs,rotation=0)
axis.yaxis.set_label_coords(x=-0.1,y=0.9)
plt.show()
#for i in range(1,10):
#    x0 = i/10
#    sol = odeint(repdyn,x0,t,args=(a1,a2))
#    plt.plot(t,sol)
#plt.show()
runs=10
for i in range(1,runs):
    x0 = i/runs
    sol = odeint(repgen,x0,t,args=(a1,a2,eps,delta,gamma1,gamma2))
    plt.plot(t,sol)
#sol =odeint(repgen,root,t,args=(a1,a2,eps,delta,gamma1,gamma2))
#plt.plot(t,sol)
plt.axhline(y=0.75,c="red",ls='dashed')
plt.axhline(y=root,c="green",ls='dashed')
axes=plt.gca()
axes.set_xlim([0,10])
axes.set_ylim([0,1])
plt.xlabel(r'$t$',fontsize=fs)
axes.yaxis.set_label_coords(x=-0.1,y=0.9)
plt.ylabel(r'$x(t)$',fontsize=fs,rotation=0)
plt.show()
