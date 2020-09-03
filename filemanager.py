# -*- coding: utf-8 -*-
"""Importing the informations about the plot and potential"""
import os.path
import numpy as np


def fileinp(path):
    input = np.loadtxt(os.path.join(path, "schrodinger.inp"))

    mass = input[0, 0]

    graphsize = input[1]

    ew = input[2, 1] - input[2, 0]

    interpol = input[3, 0]

    potpoints = input[5:, 0:1]

    return mass, graphsize, ew, interpol, potpoints
