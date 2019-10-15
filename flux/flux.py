import numpy as np
import math as math
from numpy import linalg as lg
import matplotlib.pyplot as plot
#from classes import constants
#from classes import SR as SR
#from classes.tender import tender as undulator
from classes import reflectivity as reflectivity
from classes.photons import Photons
import periodictable as periodictable
from classes.tender import tender as SR

incidentAngle = np.array(1.25)
material = "Au"
density = periodictable.Au.density
maxeV = 30000.


# flux = Photons(None, maxeV)
photon = Photons(SR(), maxeV)
#photon.setReflectivity(material, density, incidentAngle)
photonFlux = photon.getPhotonFlux(0.,0.)

print("photon flux  " + str(photonFlux) + "w/mrad^2")