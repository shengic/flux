import math as math
import numpy as np
from numpy import linalg as lg
from classes import reflectivity as reflectivity
from classes import SRconstants as undulator
from classes.tender import tender
import scipy.constants as constants
import scipy.special as special

class photons(object):
    def __init__(self, undulator, maxeV):
        self.undulator = undulator
#reflectivity/absorption percentage list
        self.ntotal = int(maxeV/(this.undulator.eV1))+1
#create evlist per n
        self.evList = np.arange(1, self.ntotal, 2) * self.undulator.ev1
        self.evHash = {key : value for key, value in zip(np.arange(1, self.ntotal, 2), self.evList)}
        self.refList = np.repeat(1., len(self.evList))
        self.refHash = {key : value for key, value in zip(np.arange(1, self.ntotal, 2), self.refList)}
# get list of each harmonic energy
        self.LfunList = self.getLfunList()

    def setReflectivity(self, material, density, incidentAngle):
        self.reflectivity = reflectivity(material, density)
        reflist = self.reflectivity.getReflectivityList(incidentAngle, self.evList)
        self.refHash = {key : value for key, value in zip(np.arange(1, self.ntotal, 2), reflist)}

    def getPhotonFlux(self, thetax, thetay):
        self.thetax = thetax
        self.thetay = thetay

        self.photonFlux = np.power(constants.e*self.undulator.gamma*self.undulator.N,2)/constants.e* \
            2.*math.pi/constants.Planck/(4.*constants.pi*constants.epepsilon_0*constants.c)
        self.photonFlux *= self.undulator.ev1*1000./self.undulator.N*np.sum(self.LfunList())


    def getLfunList(self):
        self.LfunList = np.array()
# make sure each element is only odd number energy
        for n in np.arange(1, self.ntotal, 2):
            self.LfunList.append(Fn(n)*n*self.refHash(n))
        return self.LfunList

    def Fn(self,n):
        k = self.undulator.ky
        z = n*np.power(kaiser,2)/(2.*(1.+ np.power(kaiser,2)/2))
        self.Fn = np.power(n*k,2)/np.power((1.+ np.power(k,2)/2.) ,2) * \
                   np.power(special.jv((n+1)/2,z)-special.jv((n-1)/2,z),2)
        return self.Fn