"""
    Executing the programm.
"""
import os.path
import interpolation
import visualizer
import potsolver


def main():
    """
        Managing the files of the programm.
    """
    path = input("Please enter the to your schrodinger.inp-file: ")
    fp = open(os.path.join(path, "schrodinger.inp"), "r")
    basedata = fp.read().split()
    fp.close()
    newpath = input("Please enter the path where to save the results: ")

    for i in range(len(basedata)):
        try:
            float(basedata[i])
        except ValueError:
            continue

    potx, poty = interpolation.interpolating(basedata[1:4], basedata[8:], basedata[6], newpath)

    eigvals, eigvecs, uncertainty_and_expected = potsolver.solve_pot(basedata[0], basedata[1:4], potx, poty, basedata[4:6], newpath)

    visualizer.visualise(potx, poty, newpath)


if __name__ == "__main__":
    main()
