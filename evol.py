from scipy.integrate import odeint
import numpy as  np
import matplotlib.pyplot as plt
t = np.linspace(0,10,100)
def repdyn(x,t,a1,a2):
    return (x**2)*(a1 + 2*a2) - (x**3)*(a1+a2) - x*(a2)
def rep(x,t):
    return x*((x-x**2) + 3*(2*x-1-x**2))
a =10
b =0
c =4
d =3
a1 = a-c
a2 = d-b  

sol = odeint(repdyn,0.5,t,args=(a1,a2))
plt.plot(t,sol)
plt.show()
