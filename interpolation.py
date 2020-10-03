"""
Module for interpolating the potential
"""

import os.path
from scipy import interpolate
import numpy as np


def interpolating(basedata, path):

    """
    Interpolates the given potentialpoints while considering the given plotsize
    and the given number of potentialpoints

    Returns: the x- and y-values for the potential (xnew, ynew)
    """

    plotsize1 = int(basedata[1])
    plotsize2 = int(basedata[2])
    plotsize3 = int(basedata[3])
    potp = basedata[8:]
    interpol = basedata[6]

    xnew = np.linspace(plotsize1, plotsize2, num=plotsize3)

    if interpol == "polynomial":
        xx = potp[::2]
        yy = potp[1::2]
        pot = interpolate.BarycentricInterpolator(xx, yy)

        ynew = pot(xnew)

    elif interpol == "linear":
        xx = potp[::2]
        yy = potp[1::2]
        pot = interpolate.interp1d(xx, yy)

        ynew = pot(xnew)

    elif interpol == "cspline":
        xx = potp[::2]
        yy = potp[1::2]
        pot = interpolate.CubicSpline(xx, yy, bc_type='natural')

        ynew = pot(xnew)

    potnew = np.array([xnew[0], ynew[0]])
    for i in range(1, len(xnew)):
        potnew = np.vstack((potnew, np.array([xnew[i], ynew[i]])))
    np.savetxt(os.path.join(path, "potential.dat"), potnew)
