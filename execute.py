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

    interpolation.interpolating(basedata, newpath)

    potsolver.solve_pot(basedata, newpath)

    visualizer.visualise(newpath)


if __name__ == "__main__":
    main()
