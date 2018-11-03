#author: Ruairí Brady (ruairi.brady@ucdconnect.ie)

#importing packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
%matplotlib inline

#loading data
data = np.loadtxt("comptscat-data.txt")
t = (data[:,2])
c = (data[:,3])
c_err = (data[:,4])
r = 0.009
r2 = 0.26
years = 41.25
m_rod = 79.3

#experimental calculations
IPS = 0.1522*(energy)**(-1.1325)
sum_gamma = c/t*IPS
A_det = (np.pi)*(0.009)**2
sumgamma = c/(t*IPS)
nume = ((m_rod*13*6.0221E23)/(27))
delta = A_det/(r2)**2
I = (1.013E6)*(np.exp(-41.25/43.48))
nume*delta*I
cs_real = sumgamma/(nume*delta*I) 

#theoreitcal calculations
r0 = 2.82E-13
alpha = 1.29
theta = np.deg2rad(angle)
diffCS1 = (r0**2)/2
diffCS2 = ((1+(np.cos(theta))**2))/((1+(alpha)*(1-np.cos(theta))**2))
diffCS3 = (1+(1-np.cos(theta))**2*(alpha)**2)/((1+(np.cos(theta))**2)*(1+(alpha)*(1-np.cos(theta))))
theoretical_diffCS = diffCS1*diffCS2*diffCS3

#plotting the experimental and theoretical data
def func2(x, a, b, c, d):
    return a*x*x*x +b*x*x +c*x +d
popt2, pcov2 = curve_fit(func2,angle, cs_real)
best2 = func2(angle, popt2[0],popt2[1],popt2[2],popt2[3])
plt.plot(angle,theoretical_diffCS, 'r-', label='Theoretical Prediction')
plt.plot(angle,cs_real,'b.',markersize=5)
plt.plot(angle,best2,'b-',linewidth=1,label='Experimental Results')
plt.title('Differential Scattering Cross-Section for the\n Compton Interaction at a given Angle\n')
plt.ylabel(r'Differential Scattering Cross-Section')
plt.xlabel(r'Angle ($^\circ$)')
plt.grid(True)
plt.legend(bbox_to_anchor=(0.52, 0.95), loc=2, borderaxespad=0.)
plt.savefig('diff_scattering_CS.png')
