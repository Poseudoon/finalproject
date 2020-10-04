"""
Executing the programm.
"""
import os.path
import argparse
import interpolation
import visualizer
import potsolver


def main():
    """
    Determines the inputpath where the schrodinger.inp is located,
    as well as where the ouputdata will be saved.

    Runs the modules to solve the given Problem.
    """

# adding arguments
    _description = """Script solves Schoedinger-equation for a given potential from path
    and saves the solution in newpath."""
    parser = argparse.ArgumentParser(description=_description)

    msg = "path (default: .)"
    parser.add_argument("-i", "--inputpath", default=".", help=msg)

    msg = "newpath (default: .)"
    parser.add_argument("-o", "--outputpath", default=".", help=msg)

# reading the input-file
    args = parser.parse_args()
    path = args.inputpath
    newpath = args.outputpath
    fp = open(os.path.join(path, "schrodinger.inp"), "r")
    basedata = fp.read().split()
    fp.close()

# changing data-types of the numbers
    for i in range(len(basedata)):
        try:
            basedata[i] = float(basedata[i])
        except ValueError:
            continue

# generating results
    interpolation.interpolating(basedata, newpath)

    potsolver._solve_pot(basedata, newpath)

    visualizer._visualise(newpath)


if __name__ == "__main__":
    main()
