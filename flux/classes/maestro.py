import math as math
import numpy as np
from numpy import linalg as lg

class maestro(object):
    def __init__(self):

        # incident angle (degreee)
        self.incidentAngle = np.array(2.25)

        #electron energy (GeV)
        self.GeV = 2.

        #current (mA)
        self.beamCurrent = 500

        # period length lambda [cm]
        self.lambda0 = 7

        # number of period N
        self.N = 25

        # By magnet field T [tesla)
        #self.magnetBy = 1.12659
        self.magnetBy = 0.145347

        # Bx magnet field T (tesla)
        self.magnetBx = 0.0

        # total length of ID (m)
        self.totalLength = self.lambda0*self.N/100.

        # deflection parameter Ky
        self.Ky = 0.934 * self.lambda0 * self.magnetBy

        # deflection parameter Kx
        self.Kx = 0.934 * self.lambda0 * self.magnetBx

        # gamma 1/mrad
        self.gamma = 1957.*self.GeV/1000.

        # electron volt

        #get 1st harmonic energy in eV
        self.eV1 = 9.498*np.power(self.GeV,2)/(self.lambda0/100.*(1 + np.power(self.Kx,2)/2. + np.power(self.Ky,2)/2.))
