"""
Executing the programm.
"""
import os.path
import interpolation
import visualizer
import potsolver


def main():
    """
    Determines the inputpath where the schrodinger.inp is located,
    as well as where the ouputdata will be saved.

    Runs the modules to solve the given Problem.
    """
    path = input("Please enter the path to your schrodinger.inp-file: ")
    fp = open(os.path.join(path, "schrodinger.inp"), "r")
    basedata = fp.read().split()
    fp.close()
    newpath = input("Please enter the path where to save the results: ")

    for i in range(len(basedata)):
        try:
            basedata[i] = float(basedata[i])
        except ValueError:
            continue

    interpolation._interpolating(basedata, newpath)

    potsolver._solve_pot(basedata, newpath)

    visualizer._visualise(newpath)


if __name__ == "__main__":
    main()
