# -*- coding: utf-8 -*-

import os.path
import numpy as np
import pytest
import interpolation

potentials = ["asymmetric", "double_well_lin", "double_well_spl", "fin_well", "harmonic", "inf_well"]


@pytest.mark.parametrize("potname", potentials)
def test_interpolation(potentials):
    path = "./testing/inf_well"
    newpath = "./testing/inf_well_test"
    fp = open(os.path.join(path, "schrodinger.inp"), "r")
    basedata = fp.read().split()
    fp.close()
    for i in range(len(basedata)):
        try:
            basedata[i] = float(basedata[i])
        except ValueError:
            continue

    interpolation.interpolating(basedata, newpath)
    newpot = np.loadtxt(os.path.join(newpath, "potential.dat"))
    originalpot = np.loadtxt(os.path.join(path, "potential.dat"))

    assert np.allclose(originalpot, newpot, rtol=1e-10, atol=1e10)
