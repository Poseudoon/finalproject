# -*- coding: utf-8 -*-
from scipy import interpolate
import numpy as np
import os.path


def interpol(plotsize, potp, interpol, path):

    xnew = np.linspace(plotsize[0], plotsize[1], num=plotsize[2])

    if interpol == "polynomial":
        x = potp[:, 0]
        y = potp[:, 1]
        pot = interpolate.BarycentricInterpolator(x, y)

        ynew = pot(xnew)

    elif interpol == "linear":
        x = potp[:, 0]
        y = potp[:, 1]
        pot = interpolate.interp1d(x, y)

        ynew = pot(xnew)

    potnew = np.array([xnew[0], ynew[0]])
    for i in range(1, len(xnew)):
        potnew = np.vstack((potnew, np.array([xnew[i], ynew[i]])))
    np.savetxt(os.path.join(path, "potenial.dat"), potnew)

    return xnew, ynew
