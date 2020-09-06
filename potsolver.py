import scipy as sc
import numpy as np


def evectorcalc(mass, plotsize, potx, poty):

    """
    Calculates the number of desired eigenvectors

    Returns: y-values of desired eigenvectors
    """
# defining constants
    interval = (plotsize[1] - plotsize[0])/plotsize[3]
    a = 1/(mass*interval**2)

# calculating hamiltonmatrix
    hamiltonmatrix = np.zeros((len(poty), len(poty)), dtype=float)

    for col in range(0, len(poty)):

        for row in range(0, len(poty)):

            if col == row:
                hamiltonmatrix[row, col] = a + poty[row]

                if col == len(poty) - 1:
                    break

                hamiltonmatrix[row + 1, col] = -1/2*a
                hamiltonmatrix[row, col + 1] = -1/2*a
