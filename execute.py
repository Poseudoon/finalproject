# -*- coding: utf-8 -*-
import os.path
import numpy as np
import interpolation


def main():
    basedata = np.loadtxt(os.path.join(input("Please enter the to your schrodinger.inp-file: "), "schrodinger.inp"))

    xnew, ynew = interpolation.interpol(basedata[1, ], basedata[5:, ], basedata[3, ])


if __name__ == "__main__":
    main()
