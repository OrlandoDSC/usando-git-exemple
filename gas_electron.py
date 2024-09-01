#Função dielétrica do gás de elétron
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
arq=open('dado.dat','w')
#n=1e28
#e=1.6e-19
#eps0=8.85e-12
#m=9e-31
#omegap=np.sqrt(n*e**2/eps0*m)
omegap=9.0

def eps(omega):
    if omega == omegap:
        return 0
    elif omega<omegap:
        return 1-(omegap/omega)**2
    elif omega>omegap:
        return 1-(omegap/omega)**2
    
omega=1
for i in range(100):
    omega= 0.0001*omega+i
    y=eps(omega)
    print(omega/omegap,y)

    arq.write('{} {}\n'.format(omega/omegap,y))
arq.close() 
plt.plot(omega/omegap,y)
plt.show()









