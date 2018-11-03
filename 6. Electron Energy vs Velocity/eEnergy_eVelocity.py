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

#FIGURE 4 - Electron momentum as a function of beta
def func4(x,a,b):
    return gamma*x*popt[0]

popt4, pcov4 = curve_fit(func4,beta,pc)
best4 = func4(beta,popt4[0],popt4[1])

plt.plot(beta,pc,'bo',markersize=5)
plt.plot(beta,best4,'r-',linewidth=1)
plt.xlabel(r'$\beta$')
plt.ylabel('pc (keV)')
plt.errorbar(beta,pc,xerr=beta_err,yerr=pc_err,fmt='.')
plt.title("Electron Energy as a Function of its Velocity\n(Relative to the Speed of Light)")
plt.plot(beta,pc,'bo',markersize=5)
plt.axis([0,1,0,3000])
plt.grid(True)
plt.savefig('beta_momentum.png')
