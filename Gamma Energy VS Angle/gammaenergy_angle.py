#author: Ruairí Brady (ruairi.brady@ucdconnect.ie)

#importing packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
%matplotlib inline

#loading data
data = np.loadtxt("comptscat-data.txt")
angle = data[:,0]
energy = (data[:,1])/1000
energy_err = (data[0:,5])
x = (1-np.cos(np.deg2rad(angle)))
y = (1/energy)
y_theoretical = 1.51 + 1.956*(x)

#loading errors on data
xerror = 1-np.cos(np.deg2rad(0.25))
yerror = ((data[:,5])/1000)/energy**2

#defining our linear fit function
def func(x, m, c):
    return m*x+c

#experimental fitting
popt, pcov = curve_fit(func, x, y)
best = func(x, popt[0], popt[1])
uncert_slope = np.sqrt(pcov[0,0])
uncert_intercept = np.sqrt(pcov[1,1])

#theoretical fitting
popt2, pcov2 = curve_fit(func, x, y_theoretical)
best2 = func(x, popt2[0], popt2[1])

#plotting with error bars
plt.plot(x,best,'b-', label="Experimental Results")
plt.plot(x,y,'b.')
plt.errorbar(x,y,xerr=xerror,yerr=yerror,fmt='.')
plt.plot(x,y_theoretical,'r-', label="Theoretical Prediction")
plt.title("Dependence of Energy on Angle \nfor a Compton Scattered $\gamma$ Ray")
plt.ylabel(r'$\frac{1}{E_\gamma}$ ' r'($\frac{1}{MeV}$)')
plt.xlabel(r'$1 - cos(\theta)$')
plt.grid(True)
plt.legend(bbox_to_anchor=(0.05, 0.95), loc=2, borderaxespad=0.)
plt.savefig('energy_vs_angle.png')

slope_difference = 100*(popt2[0]-popt[0])/popt2[0]

print("The experimental slope: {0:.4}".format(popt[0]),"± {0:.2}".format(uncert_slope))
print("The experimental y-intercept: {0:.3}".format(popt[1]),"± {0:.1}\n".format(uncert_intercept))

print("The theoretical slope: {0:.4}".format(popt2[0]))
print("The theoretical y-intercept: {0:.3}\n".format(popt2[1]))

print("The percentage error between the theoretical and experimental slope values: {0:.2}".format(100*(popt2[0]-popt[0])/popt2[0]),"%")
print("The percentage error between the theoreitcal and experimental y-intercept values: {0:.2}".format(100*(popt2[1]-popt[1])/popt2[1]),"%\n")
