"""
This module calculates the eigenvalues and eigenvectors to the given problem
"""

import os.path
import numpy as np
import scipy.linalg as la


def solve_pot(basedata, newpath):

    """
    Calculates the number of desired eigenvectors, eigenvalues,
    expected values and x-uncertainty

    Returns: y-values of desired eigenvectors, eigenvalues,
    expected values and x-uncertainty
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

        for row in range(0, len(poty)):

            if col == row:
                hamiltonmatrix[row, col] = hamconstant + poty[row]

                if col == len(poty) - 1:
                    break

                hamiltonmatrix[row + 1, col] = -1/2*hamconstant
                hamiltonmatrix[row, col + 1] = -1/2*hamconstant

# Calculate eigenvalues and eigenvectors

    desev = (int(eigvaluesdata[0])-1, int(eigvaluesdata[1])-1)

    main_diag = np.zeros(len(poty))

    for i in range(0, len(poty)):
        main_diag[i] = hamiltonmatrix[i, i]

    minor_diag = hamiltonmatrix[0, 1] * np.ones(len(poty) - 1)

    eigvals, eigvecs = la.eigh_tridiagonal(main_diag, minor_diag, select="i", select_range=desev)

    eigenvecs_withx = np.vstack((potx, np.transpose(eigvecs)))

    np.savetxt(os.path.join(newpath, "energies.dat"), eigvals)
    np.savetxt(os.path.join(newpath, "wavefuncs.dat"), np.transpose(eigenvecs_withx))

# Calculate expected values
    numo_eigenvals = len(eigvals)
    expected_vals_x = []
    expected_vals_xx = []
    uncertainty_x = []

    for i in range(0, numo_eigenvals):
        expected_val_x = interval * np.sum(potx * np.transpose(eigvecs)[i] ** 2)
        expected_val_xx = interval * np.sum(potx ** 2 * np.transpose(eigvecs)[i] ** 2)
        uncertainty = np.sqrt(expected_val_xx - expected_val_x ** 2)

        expected_vals_x.append(expected_val_x)
        expected_vals_xx.append(expected_val_xx)
        uncertainty_x.append(uncertainty)

    uncertainty_and_expected = np.vstack((np.array(expected_vals_x), uncertainty_x))
    np.savetxt(os.path.join(newpath, "expvalues.dat"), np.transpose(uncertainty_and_expected))
