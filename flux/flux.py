import numpy as np
import math as math
from numpy import linalg as lg
import matplotlib.pyplot as plot
#from classes import constants
#from classes import SR as SR
#from classes.tender import tender as undulator
from classes import reflectivity as reflectivity
from classes import photons as photons
import periodictable as periodictable
from classes import SRconstants

incidentAngle = np.array(1.25)
material = "Au"
density = periodictable.Au.density
maxeV = 30000.

flux = photons(SRconstants, maxeV)
flux.setReflectivity(material, density, incidentAngle)
photonFlux = flux.getPhotonFlux(0.,0.,)

print("photon flux  " + photonFlux)