"""
Module for Visualising the results from potsolver
"""
import os.path
import numpy as np
import matplotlib.pyplot as plt


def visualise(xpot, ypot, path):
    """
    Reading in the results of potsolver, enters the size for the plot
    and plotting the results
    """
    try:
        energies = np.loadtxt(os.path.join(path, "energies.dat"))
        wavefuncs = np.loadtxt(os.path.join(path, "wavefuncs.dat"))
        expval = np.loadtxt(os.path.join(path, "expvalues.dat"))
    except OSError:
        path = input("Please enter path where the potential, energies and wavefunctions exist: ")
        energies = np.loadtxt(os.path.join(path, "energies.dat"))
        wavefuncs = np.loadtxt(os.path.join(path, "wavefuncs.dat"))
        expval = np.loadtxt(os.path.join(path, "expvalues.dat"))

    try:
        factor = float(input("Please enter the factor of the wavefunctions for a better visualisation: "))
    except ValueError:
        factor = 1

    try:
        xmin = float(input("Please enter the x-range: \nx-minimum: "))
    except ValueError:
        xmin = xpot[0]

    try:
        xmax = float(input("x-maximum: "))
    except ValueError:
        xmax = xpot[-1]

    try:
        ymin = float(input("Please enter the y-range: \ny-minimum: "))
    except ValueError:
        ymin = energies[0]-1

    try:
        ymax = float(input("y-maximum: "))
    except ValueError:
        ymax = energies[-1]+1

    for i in range(0, len(energies)):
        wfunc = wavefuncs[:, i+1]
        energ = energies[i]

        plt.subplot(1, 2, 1)
        plt.title("Wavefunctions", fontsize=18)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.plot(xpot, ypot, linewidth=1.5, linestyle="-", color="black")
        plt.plot([-10, 10], [energ, energ], linewidth=1, linestyle="-", color="grey")
        if i == 0:
            plt.scatter(expval[i, 0], energ, 100, marker='x', color='green', label='expected value')
        else:
            plt.scatter(expval[i, 0], energ, 100, marker='x', color='green')
        if i % 2:
            color = 'blue'
        else:
            color = 'red'
        plt.plot(xpot, energ + factor * wfunc, linewidth=1, linestyle="-", color=color, label='wavefunction')
        plt.legend(loc='lower right', fontsize='xx-small')
        plt.xlabel("x [Bohr]", fontsize=11)
        plt.ylabel("Energy [Hartree]", fontsize=11)

        plt.subplot(1, 2, 2)
        plt.title("UUncertainty", fontsize=18)
        plt.xlim(0, 1.1)
        plt.ylim(ymin, ymax)
        plt.plot([0, 1.1], [energ, energ], linewidth=1, linestyle="-", color="grey", label='energy')
        if i == 0:
            plt.scatter(expval[i, 1], energ, 100, marker='x', color='green', label='uncertainty')
        else:
            plt.scatter(expval[i, 1], energ, 100, marker='x', color='green')
        plt.legend(loc='upper left', fontsize='xx-small')
        plt.xlabel("[Bohr]", fontsize=11)
        plt.ylabel("Energy [Hartree]", fontsize=11)
        plt.savefig(os.path.join(path, "wavefunctions.pdf"), format='pdf')
        plt.show()
