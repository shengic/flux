import numpy as np
import periodictable as periodictable
from periodictable import xsf
# https://periodictable.readthedocs.io/en/latest/api/xsf.html 

class reflectivity(object):
    def __init__(self, material, density):
#        print(periodictable.core.iselement(material))
#        if(periodictable.core.isatom(material)):
#            self.material = material
#            self.density = getattr(periodictable,material).density
#            self.roughness = 0.
#        else:
#            print("i dont know the element " + material)
        self.material = material
        self.density = density
        self.roughness = 0.

    def setMaterial(self,material):
        if(p.core.iselement(material)):
            self.material = material
            self.density = getattr(periodictable,material).density

    def setRoughness(self, roughness):
        self.roughness = roughness

    def setMaterial(self, material):
        self.material = material

# give only one reflectivity for given photon energy
    def getOneReflectivity(self, incidentAngle, eV):
        self.incidentAngle = [incidentAngle]
        self.keV = [eV]/1000.
        self.oneReflectivity = xsf.mirror_reflectivity(compound = self.material, density = self.density ,\
            energy = self.keV, roughness = self.roughness, angle = self.incidentAngle)
        return reflectivity[0][0]

# return list of reflectivity for given list of photon energy
    def getReflectivityList(self, incidentAngle, evList):
        self.incidentAngle = incidentAngle
        self.keVList = evList/1000.
        self.reflectivity = xsf.mirror_reflectivity(compound = self.material, density = self.density ,\
            energy = self.keVList, roughness = self.roughness, angle = self.incidentAngle)
        return self.reflectivity[0]
