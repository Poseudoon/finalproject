"""
Tests if the potsolver module is working properly, using six
different test potentials

"""

import numpy as np
import os.path
import pytest
import execute
import interpolation
import potsolver

# Reading the testsolutions for comparison


# Testing interpolation


def test_interpol(potpoint):
    potx =
    poty =



def test_potsolver():

    xx_expected = np.array([0.666666666666667, 0.416666666666667, -0.5])
    xx_gauss = solvers.gaussian_eliminate(aa, bb)
    assert np.allclose(xx_gauss, xx_expected, 1e-10, 1e-10)
