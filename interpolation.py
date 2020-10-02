"""
Module for interpolating the potential
"""

import os.path
from scipy import interpolate
import numpy as np


def interpolating(plotsize, potp, interpol, path):

    """
    Interpolates the given potentialpoints while considering the given plotsize
    and the given number of potentialpoints

    Returns: the x- and y-values for the potential (xnew, ynew)
    """

    xnew = np.linspace(plotsize[0], plotsize[1], num=plotsize[2])

    if interpol == "polynomial":
        xx = potp[8::2]
        yy = potp[9::2]
        pot = interpolate.BarycentricInterpolator(xx, yy)

        ynew = pot(xnew)

    elif interpol == "linear":
        xx = potp[8::2]
        yy = potp[9::2]
        pot = interpolate.interp1d(xx, yy)

        ynew = pot(xnew)

    potnew = np.array([xnew[0], ynew[0]])
    for i in range(1, len(xnew)):
        potnew = np.vstack((potnew, np.array([xnew[i], ynew[i]])))
    np.savetxt(os.path.join(path, "potenial.dat"), potnew)
