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

#non-relativistic rest energy of electron using experimental values
mnr_c2 = ((2*Egam-T)**2)/(2*T)
dTmnr_c2 = 0.5+(2*Egam**2)/(T**2)
dEmnr_c2 = (4*Egam/T)-2
mnr_c2_err = np.sqrt((Egam_err)**2*(dEmnr_c2)**2 + (T_err)**2*(dTmnr_c2**2))

#Figure: T as a function of non-relativisitic rest mass energy - linear plot
def func2(x, m, c):
    return m*x+c

popt2, pcov2 = curve_fit(func2, T, mnr_c2)
best2 = func2(T, popt2[0], popt2[1])
plt.plot(T,mnr_c2,'bo', markersize=5)
plt.plot(T,best2, 'r-', linewidth=1)
plt.errorbar(T,mnr_c2,xerr=T_err,yerr=mnr_c2_err,fmt='.')
plt.xlabel('T (keV)')
plt.ylabel('$m_{nr}c^2$ (keV)')
plt.title("The Non-Relativistic Rest Mass Energy of the Electron\nas a Function of its Kinetic Energy")
plt.grid(True)
plt.axis([0,2500, 500, 1800])
plt.savefig('kineticenergy_vs_NRrestmass.png')

uncert_slope = np.sqrt(pcov2[0,0])
uncert_intercept = np.sqrt(pcov2[1,1])

print("The slope: {0:.4}".format(popt2[0]),"± {0:.2}".format(uncert_slope))
print("The y-intercept: {0:.4}".format(popt2[1]),"± {0:.3}".format(uncert_intercept), "keV\n")
