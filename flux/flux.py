import numpy as np
import math as math
from numpy import linalg as lg
import matplotlib.pyplot as plot
from classes import reflectivity as reflectivity
from classes.photons import Photons
import periodictable as periodictable
from classes.maestro import maestro as SR

incidentAngle = SR().incidentAngle
material = "Au"
density = periodictable.Au.density
maxeV = 30000.

# flux = Photons(None, maxeV)
photon = Photons(SR(), maxeV)
photonFlux =  photon.getPhotonFlux(0.,0.)
print("on axis power density without material reflectivity = " + str(photonFlux) + " w/mrad^2")
photon.setReflectivity(material, density, incidentAngle)
photonFlux = photon.getPhotonFlux(0.,0.)
print("photon flux reflectivity " + str(photonFlux) + " w/mrad^2")
photon.setAbsorption(material, density, incidentAngle)
photonFlux = photon.getPhotonFlux(0.,0.)
print("photon flux absorption " + str(photonFlux) + " w/mrad^2")
