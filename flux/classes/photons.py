import math as math
import numpy as np
from numpy import linalg as lg
from classes import reflectivity as reflectivity
import scipy.constants as constants
import scipy.special as special

class Photons(object):
    def __init__(self, undulator, maxeV):
        self.undulator = undulator
#reflectivity/absorption percentage list 1,2,3,4,...
        self.ntotal = math.floor(maxeV/self.undulator.eV1)
#create evlist per n
# all require ev list to determine reflectivity/absorption
        self.evList = np.arange(1, self.ntotal) * self.undulator.eV1
# give a hash table key = n, value = ev
        self.evHash = {key : value for key, value in zip(np.arange(1, self.ntotal), self.evList)}
# give ref list all reflectivity = 1
        self.refList = np.repeat(1., len(self.evList))
# give hash table by default, all reflectivity = 1
        self.refHash = {key : value for key, value in zip(np.arange(1, self.ntotal), np.repeat(1., len(self.evList)))}
# get list of each harmonic energy
        self.LfunList = self.getLfunList(self.refHash)

    def setReflectivity(self, material, density, incidentAngle):
        self.reflectivity = reflectivity(material, density)
        reflist = self.reflectivity.getReflectivityList(incidentAngle, self.evList)
        self.refHash = {key : value for key, value in zip(np.arange(1, self.ntotal), reflist[0::1])}
        self.LfunList = self.getLfunList(self.refHash)
#        print(self.refHash)

    def setAbsorption(self, material, density, incidentAngle):
        self.reflectivity = reflectivity(material, density)
        reflist = self.reflectivity.getReflectivityList(incidentAngle, self.evList)
        self.refHash = {key : value for key, value in zip(np.arange(1, self.ntotal), reflist[0::1])}
        self.absHash = {key : value for key, value in zip(np.arange(1, self.ntotal), 1- reflist[0::1])}
        self.LfunList = self.getLfunList(self.absHash)
#        print(self.refHash)

    def getPhotonFlux(self, thetax, thetay):
        self.thetax = thetax
        self.thetay = thetay

        self.photonFlux = np.power(constants.e*self.undulator.gamma*self.undulator.N,2)/constants.e* \
            (2.*math.pi/constants.Planck)/(4.*math.pi*constants.epsilon_0*constants.c)
        self.photonFlux *= constants.e*self.undulator.beamCurrent/1000.
        self.photonFlux *= self.undulator.eV1/self.undulator.N*np.sum(self.LfunList)
#       print(self.undulator.eV1/self.undulator.N*np.sum(self.LfunList))
        return self.photonFlux


    def getLfunList(self, percentage):
        self.LfunList = []
# make sure each element is only odd number energy
        for n in np.arange(1, self.ntotal,2):
            self.LfunList.append(self.Fn(n)*percentage[n])
        return self.LfunList

    def Fn(self,n):
        k = self.undulator.Ky
        z = n*np.power(k,2)/(4.*(1.+ np.power(k,2)/2))
        fn = np.power(n*k,2)/np.power((1.+ np.power(k,2)/2.) ,2) * \
                   np.power(special.jv((n+ 1)/2,z)-special.jv((n-1)/2,z),2)
        return fn