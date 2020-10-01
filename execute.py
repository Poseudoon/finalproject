# -*- coding: utf-8 -*-
import os.path
import numpy as np
import interpolation
import visualizer


def main():
    path = input("Please enter the to your schrodinger.inp-file: ")
    basedata = np.loadtxt(os.path.join(path, "schrodinger.inp"))
    newpath = input("Please enter the path where to save the results: ")

    xnew, ynew = interpolation.interpolating(basedata[1, ], basedata[5:, ], basedata[3, ], newpath)

    visualizer.visualise(xnew, ynew, newpath)


if __name__ == "__main__":
    main()
