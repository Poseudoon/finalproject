# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os.path


def visualise(xpot, ypot, path):
    try:
        energies = np.loadtxt(os.path.join(path, "energies.dat"))
        potential = np.loadtxt(os.path.join(path, "potential.dat"))
        wavefuncs = np.loadtxt(os.path.join(path, "wavefuncs.dat"))
        expvalues = np.loadtxt(os.path.join(path, "expvalues.dat"))
    except FileNotFoundError:
        path = input("Please enter path where the potential, energies and wavefunctions exist: ")
        energies = np.loadtxt(os.path.join(path, "energies.dat"))
        potential = np.loadtxt(os.path.join(path, "potential.dat"))
        wavefuncs = np.loadtxt(os.path.join(path, "wavefuncs.dat"))
        expvalues = np.loadtxt(os.path.join(path, "expvalues.dat"))

    factor = input("Please enter the factor of the wavefunctions for a better visualisation: ")
    xmin, xmax = input("Please enter the x-range of the plot in form of *xmin, xmax*: ")
    ymin, ymax = input("Please enter the y-range of the plot in form of *ymin, ymax*: ")

    plt.plot(xpot, ypot, linewidth=1.5, linestyle="-", color="black")
    for i in range(0, len(energies)):
        plt.plot([xmin, xmax], [energies[i], energies[i]], linewidth=1, linestyle="-", color="grey")
        plt.subplot(1, 2, 1)
        plt.title(Wavefunctions, fontsize=16)
        if i % 2:
            plt.plot(wavefuncs[:, 1], wavefuncs[:, 1:], linewidth=1, linestyle="-", color="blue")
        else:
            plt.plot(wavefuncs[:, 1], wavefuncs[:, 1:], linewidth=1, linestyle="-", color="red")
        plt.subplot(1, 2, 2)
        plt.title(Expected value, fontsize=16)
        plt.annotate
