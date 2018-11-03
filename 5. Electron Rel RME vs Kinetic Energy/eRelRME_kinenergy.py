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

#Figure: Relativistic rest mass energy as a function of kinetic energy
plt.plot(T,m0_c2,'bo', markersize=5)
plt.xlabel("T (keV)")
plt.ylabel('$m_0c^2$ (keV)')
plt.errorbar(T,m0_c2,xerr=T_err,yerr=m0_c2_err,fmt='.')
plt.title("The Relativistic Rest Mass Energy of the Electron\nas a Function of its Kinetic Energy")
plt.axis([0,2500, 460, 600])
plt.grid(True)
plt.plot([0, 2500], [np.mean(m0_c2),np.mean(m0_c2)], 'r-', lw=1)
plt.savefig('kineticenergy_vs_restmass.png')

print("Rest energy of electron = {0:.4}".format(np.mean(m0_c2)),"± {0:.3}".format(np.mean(m0_c2_err)), "keV") 
