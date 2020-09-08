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
        expvalues = np.loadtxt(os.path.join(path, "expvalues.dat"))
    except OSError:
        path = input("Please enter path where the potential, energies and wavefunctions exist: ")
        energies = np.loadtxt(os.path.join(path, "energies.dat"))
        wavefuncs = np.loadtxt(os.path.join(path, "wavefuncs.dat"))
        expvalues = np.loadtxt(os.path.join(path, "expvalues.dat"))

    factor = float(input("Please enter the factor of the wavefunctions for a better visualisation: "))
    xmin = float(input("Please enter the x-range: \nx-minimum: "))
    xmax = float(input("x-maximum: "))
    ymin = float(input("Please enter the y-range: \ny-minimum: "))
    ymax = float(input("y-maximum: "))

    for i in range(0, len(energies)):
        wfunc = wavefuncs[:, i+1]
        energy = energies[i]

        plt.subplot(1, 2, 1)
        plt.title("Wavefunctions", fontsize=16)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.plot(xpot, ypot, linewidth=1.5, linestyle="-", color="black")
        plt.plot([-10, 10], [energy, energy], linewidth=1, linestyle="-", color="grey")
        plt.scatter(expvalues[i, 0], energies[i], 100, marker='x', color='green')
        if i % 2:
            color = 'blue'
        else:
            color = 'red'
        plt.plot(xpot, energy + factor * wfunc, linewidth=1, linestyle="-", color=color)

        plt.subplot(1, 2, 2)
        plt.title("Unsharpness", fontsize=16)
        plt.xlim(0, 1.1)
        plt.ylim(ymin, ymax)
        plt.plot([0, 1.1], [energy, energy], linewidth=1, linestyle="-", color="grey")
        plt.scatter(expvalues[i, 1], energies[i], 100, marker='x', color='green')
    plt.show()
