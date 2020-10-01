# -*- coding: utf-8 -*-

import numpy as np
import filemanager


def test_1():

    xx_expected = np.array([0.666666666666667, 0.416666666666667, -0.5])
    xx_gauss = solvers.gaussian_eliminate(aa, bb)
    assert np.allclose(xx_gauss, xx_expected, 1e-10, 1e-10)
