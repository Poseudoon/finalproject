"""
Tests if the potsolver and interpolation module is working properly,
using six different test potentials given in the ../testing folder
"""

import os.path
import numpy as np
import pytest
import solver.interpolation
import solver.potsolver


pot_names = ["asymmetric", "double_well_lin", "double_well_spl",
             "fin_well", "harmonic", "inf_well"]

# Testing the interpoloation module


@pytest.mark.parametrize("pot_name", pot_names)
def test_interpolation(pot_name):
    """
    Tests the interpolation module with the six test potentials

    Args:
        pot_name (string): is the name of the potential that is being
        currently tested
    """

    path = "./testing/{0}".format(pot_name)
    newpath = "./testing/{0}_test".format(pot_name)
    fp = open(os.path.join(path, "schrodinger.inp"), "r")

    basedata = fp.read().split()
    fp.close()
    for i in range(len(basedata)):
        try:
            basedata[i] = float(basedata[i])
        except ValueError:
            continue

    solver.interpolation._interpolating(basedata, newpath)
    test_pot = np.loadtxt(os.path.join(newpath, "potential.dat"))
    original_pot = np.loadtxt(os.path.join(path, "potential.dat"))

    assert np.allclose(original_pot, test_pot, rtol=1e-10, atol=1e10)

# Testing the potsolver module


@pytest.mark.parametrize("pot_name", pot_names)
def test_potsolver(pot_name):
    """
    Tests the potsolver module with the six test potentials

    Args:
        pot_name (string): is the name of the potential that is
        being currently tested
    """

    path = "./testing/{0}".format(pot_name)
    newpath = "./testing/{0}_test".format(pot_name)
    fp = open(os.path.join(path, "schrodinger.inp"), "r")

    basedata = fp.read().split()
    fp.close()
    for i in range(len(basedata)):
        try:
            basedata[i] = float(basedata[i])
        except ValueError:
            continue

    solver.potsolver._solve_pot(basedata, newpath)
    test_wavefuncs = np.loadtxt(os.path.join(newpath, "wavefuncs.dat"))
    original_wavefuncs = np.loadtxt(os.path.join(path, "wavefuncs.dat"))
    test_expvalues = np.loadtxt(os.path.join(newpath, "expvalues.dat"))
    original_expvalues = np.loadtxt(os.path.join(path, "expvalues.dat"))
    test_energies = np.loadtxt(os.path.join(newpath, "energies.dat"))
    original_energies = np.loadtxt(os.path.join(path, "energies.dat"))

    assert np.allclose(original_wavefuncs, test_wavefuncs,
                       rtol=1e-10, atol=1e10)
    assert np.allclose(original_expvalues, test_expvalues,
                       rtol=1e-10, atol=1e10)
    assert np.allclose(original_energies, test_energies, rtol=1e-10, atol=1e10)
