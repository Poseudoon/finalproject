# -*- coding: utf-8 -*-
from scipy import interpolate
import numpy as np


def interpol(plotsize, potp, interpol):

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

    return xnew, ynew
