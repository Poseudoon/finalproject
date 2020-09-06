from scipy import interpolate
import numpy as np


def interpol(plotsize, potp, interpol):

    """
    Interpolates the given potentialpoints while considering the given plotsize
    and the given number of potentialpoints

    Returns: the x- and y-values for the potential (xnew, ynew)
    """

    xnew = np.linspace(plotsize[0], plotsize[1], num=plotsize[2])

    if interpol == "polynomial":
        x = potp[:, 0]
        y = potp[:, 1]
        pot = interpolate.interp1d(x, y)

        ynew = pot(xnew)

    elif interpol == "linear":

        ynew = []
        n = 1

        for i in range(0, len(xnew)):

            if xnew[i] > potp[n, 0]:
                n += 1
                if potp[n-1, 0] == potp[n, 0]:
                    n += 1

            x = potp[n-1:n+1, 0]

            y = potp[n-1:n+1, 1]

            pot = interpolate.interp1d(x, y)

            ynew.append(pot(xnew[i]))

    return xnew, ynew
