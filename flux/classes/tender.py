import math as math
import numpy as np
from numpy import linalg as lg

class tender(object):
    def __init__(self):
        #electron energy (GeV)
        self.GeV = 2.

        #current (mA)
        self.beamCurrent = 500

        # period length lambda [cm]
        self.lambda0 = 1.9

        # number of period N
        self.N = 208

        # By magnet field T [tesla)
        self.magnetBy = 1.126959

        # Bx magnet field T (tesla)
        self.self.magnetBx = 0.0

        # total length of ID (m)
        self.totalLength = lambda0*N/100.

        # deflection parameter Ky
        self.Ky = 0.934 * lambda0 * magnetBy

        # deflection parameter Kx
        self.Kx = 0.934 * lambda0 * magnetBx

        # gamma 1/mrad
        self.gamma = 1957.*GeV/1000.

        # electron volt

        #get 1st harmonic energy in eV
        self.eV1 = 9.498*np.power(GeV,2)/(lambda0/100.*(1 + np.power(Kx,2)/2. + np.power(Ky,2)/2.))
