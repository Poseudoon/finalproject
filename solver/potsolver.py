"""
This module calculates the eigenvalues and eigenvectors to the given problem
"""

import os.path
import numpy as np
import scipy.linalg as la


def _solve_pot(basedata, newpath):

    """
    Calculates the number of desired eigenvectors, eigenvalues,
    expected values and x-uncertainty

    Args:
        basedata (array): contains all necessary values to calculate the
                          eigenvalues eigenvectors, x-uncertainty and the
                          x-expectation

        newpath (string): is the path where the calculated values will will be
                          saved (energies.dat, wavefuncs.dat and expvalues.dat)
    """

# Reading potential.dat for potx and poty
    potential = np.loadtxt(os.path.join(newpath, "potential.dat"))
    potx = potential[:, 0]
    poty = potential[:, 1]

# Define constants
    mass = basedata[0]
    plotsize = basedata[1:4]
    eigvaluesdata = basedata[4:6]

    interval = (plotsize[1] - plotsize[0])/plotsize[2]
    hamconstant = 1/(mass*interval**2)

# Calculate hamiltonmatrix
    hamiltonmatrix = np.zeros((len(poty), len(poty)), dtype=float)

    for col in range(0, len(poty)):

        hamiltonmatrix[col, col] = hamconstant + poty[col]

        if col == len(poty) - 1:
            break

        hamiltonmatrix[col + 1, col] = -1/2*hamconstant
        hamiltonmatrix[col, col + 1] = -1/2*hamconstant

# Calculate eigenvalues and eigenvectors

    desev = (int(eigvaluesdata[0]) - 1, int(eigvaluesdata[1]) - 1)

    main_diag = np.zeros(len(poty))

    for i in range(0, len(poty)):
        main_diag[i] = hamiltonmatrix[i, i]

    minor_diag = hamiltonmatrix[0, 1] * np.ones(len(poty) - 1)

    eigvals, eigvecs = la.eigh_tridiagonal(main_diag, minor_diag,
                                           select="i", select_range=desev)

    eigenvecs_withx = np.vstack((potx, np.transpose(eigvecs)))

    np.savetxt(os.path.join(newpath, "energies.dat"), eigvals)
    np.savetxt(os.path.join(newpath, "wavefuncs.dat"),
               np.transpose(eigenvecs_withx))

# Calculate expected values
    numo_eigenvals = len(eigvals)
    expected_vals_x = []
    expected_vals_xx = []
    uncertainty_x = []

    for i in range(0, numo_eigenvals):
        norm = np.sqrt(interval * sum(np.transpose(eigvecs)[i] ** 2))
        norm_wfunc = np.transpose(eigvecs)[i] / norm
        expected_val_x = interval * np.sum(potx * norm_wfunc ** 2)
        expected_val_xx = interval * np.sum(potx ** 2 * norm_wfunc ** 2)
        uncertainty = np.sqrt(expected_val_xx - expected_val_x ** 2)

        expected_vals_x.append(expected_val_x)
        expected_vals_xx.append(expected_val_xx)
        uncertainty_x.append(uncertainty)

    uncertainty_and_expected = np.vstack((np.array(expected_vals_x),
                                          uncertainty_x))
    np.savetxt(os.path.join(newpath, "expvalues.dat"),
               np.transpose(uncertainty_and_expected))
