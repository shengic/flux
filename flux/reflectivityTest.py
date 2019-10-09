import numpy as np
import math as math
from numpy import linalg as lg
import matplotlib.pyplot as plot
#from classes import constants
#from classes import SR as SR
from classes import reflectivity as reflectivity
from classes import photons as photons
import periodictable as periodictable
from classes import SRconstants as undulator

incidentAngle = np.array(2)
material = "Cu"
density = periodictable.Cu.density
mineV = 30.
maxeV = 30000.

energyList = np.arange(mineV, maxeV, (maxeV - mineV)/1000)

ref = reflectivity(material, density)
rList = ref.getReflectivityList(incidentAngle, energyList)
plot.plot(energyList, rList, 'ro')
plot.show()
