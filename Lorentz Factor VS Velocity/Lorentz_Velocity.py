#author: Ruairí Brady (ruairi.brady@ucdconnect.ie)

#importing packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
%matplotlib inline

#loading data
data = np.loadtxt("compton_edge_data.txt")
Egam = data[:,0]
T = data[:,1]
T_err = data[:,2]
Egam_err = 2*T_err

#relativistic rest energy of electron using experimental values
m0_c2 = (2*Egam*(Egam-T))/(T)
dEm0_c2 = 4*Egam/T - 2
dTm0_c2 = (-2*Egam**2)/T**2
m0_c2_err = np.sqrt((Egam_err)**2*(dEm0_c2)**2 + (T_err)**2*(dTm0_c2**2))

#gamma
gamma = 1 + ((T**2)/(2*Egam*(Egam-T)))
dTgamma = T*(T-2*Egam)/(2*Egam*(Egam-T)**2)
dEgamma = T**2*(T-2*Egam)/(2*Egam**2*(Egam-T)**2)
gamma_err = np.sqrt((Egam_err)**2*(dEgamma)**2 + (T_err)**2*(dTgamma**2))

#beta
beta = (T*(2*Egam-T)/(T**2-2*Egam*T+2*Egam**2))
dTbeta = (4*Egam**2*(T-Egam)/(T**2-2*Egam*T +2*Egam**2)**2)
dEbeta = (4*Egam*T*(T-Egam)/(T**2-2*Egam*T +2*Egam**2)**2)
beta_err = np.sqrt((Egam_err)**2*(dEbeta)**2 + (T_err)**2*(dTbeta**2))

#pc
pc = 2*Egam-T
dTpc = -1
dEpc = 2
pc_err = np.sqrt((Egam_err)**2*(dEpc)**2 + (T_err)**2*(dTpc**2))

#ETotal
Etot = (T**2 -2*T*Egam + 2*Egam**2)/(T)

#FIGURE 5 - Gamma as a function of beta - exponential fit

def func5(x,a,b):
    return 1/(np.sqrt(a+b*x**2))

gamma2 = Etot/np.mean(m0_c2)

popt5, pcov5 = curve_fit(func5,beta, gamma2)
best5 = func5(beta, popt5[0], popt5[1])

plt.plot(beta,gamma2,'bo',markersize=5)
plt.plot(beta,best5,'r-',linewidth=1)
plt.errorbar(beta,gamma2,xerr=beta_err,yerr=gamma_err,fmt='.')
plt.xlabel(r'$\beta$')
plt.ylabel(r'$\gamma$')
plt.title('Lorentz Factor as a Function of Velocity\n(Relative to the Speed of Light)')
plt.axis([0,1,0,6])
plt.grid(True)
plt.savefig('beta_gammaNEW2.png')

uncert_b = np.sqrt(pcov5[0,0])
uncert_a = np.sqrt(pcov5[1,1])

print("a = {0:.3}".format(popt5[0]),"± {0:.2}".format(uncert_a))
print("b = {0:.3}".format(popt5[1]),"± {0:.2}".format(uncert_b))
