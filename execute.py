# -*- coding: utf-8 -*-
import os.path
import numpy as np
import interpolation
import visualizer


def main():
    path = input("Please enter the to your schrodinger.inp-file: ")
    fp = open(os.path.join(path, "schrodinger.inp"), "r")
    basedata = fp.read().split()
    fp.close()
    newpath = input("Please enter the path where to save the results: ")

    for i in basedata:
        try:
            float(basedata[i])
        except ValueError:
            continue

    xnew, ynew = interpolation.interpolating(basedata[1:4], basedata[8:], basedata[6], newpath)

    visualizer.visualise(xnew, ynew, newpath)


if __name__ == "__main__":
    main()
