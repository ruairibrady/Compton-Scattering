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

#Figure: EGamma as a funciton of Kinetic Energy - Quadratic Plot
def func(x, a):
    return (2*x*x)/(2*x + a)

popt, pcov = curve_fit(func,Egam, T)
best = func(Egam, popt[0])
plt.plot(Egam,T,'bo',markersize=5)
plt.plot(Egam, best, 'r-',linewidth=1,)
plt.errorbar(Egam,T,xerr=Egam_err,yerr=T_err,fmt='.')
plt.xlabel('$E_{\gamma}$ (keV)')
plt.ylabel('T (keV)')
plt.title("The Electron Kinetic Energy as a Function of \nthe $\gamma$ Ray Energy")
plt.grid(True)
plt.axis([0,2700, 0, 2500])
plt.savefig('energy_vs_kineticenergy.png')
print("The rest mass of the electron is: {0:.4}".format(popt[0]), "± {0:.2}".format(pcov[0,0]), "keV")
