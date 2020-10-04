# POTSOLVER (finalproject)

## Introduction

 With this program you can solve the schrodinger-equation from variety of  
 1-dimensional potentials. 

## Tabele of contents
* [Technologies]
* [Input format]
* [Execution details]
* [Testing]

## Technologies
   python3

### Input format
  Choose the directory where you save the inputdata (schrodinger.inp(.dat)) with the  
  following format:
  
  mass  
  xMin xMax nPoint  
  first and last eigenvalues to calculate  
  interpolarion type  
  nr. of interpolation points  
  x1 y1  
  x2 y2  
  .  .  
  .  .  
  xn yn  
  
  The mass 1 is considered to be equal to the mass of an electron. 
  The length unit is Bor (1 unit = 0,529177 * 10 ** -10 m)  
  The energy unit is hartree (1 unit = 27,211385 eV)  
  Wich eingevalues to choose should be self-explanatory  
  As interpolation type you can choose 'linear', 'polynomial' or 'cspline'  
  (cspline meaning the natural cubic spline interpolation)  
  nr. of interp. points is the number of basepoints that will be passed in the  
  following lines (n)  
  x1, y1 - xn, yn the potential basepoints for the interpolation  
  (for examples see any schodinger.inp in ./testing/potential)  

### Execution details
   To execute the program run python3 execute.py inputpath outputpath  
   in the shell.  
   inputpath is the path where the schrodinger.inp is located.  
   outputpath is the path where the output files will be saved  
   The options scale-factor as well as x- and y-range are optional.  
   The scale factor scales the visualized wavefunction and  
   the x- and y-range determines the visualized x- and y-intervals.  
  
   After execution the program will show 2 plots with the interplated potential.  
   One shows the nr. of desired wavefunctions, raised by their energy, and the  
   x-expectancy.  
   The second plot shows the x-uncertainty for the respective energies  
   In the passed outputpath the plots will be saved as .pdf. The potential,  
   energies, wavefunctions, x-expectancy und -uncertainty will also be saved there  
   with the following formats:  
  
   potential.dat  
     
   x1 V(x1)  
   x2 V(x2)  
   .  .  
   .  .  
   xn V(xn)  

   energies.dat  
 
   Ea  
   Ea + 1  
   .  
   .  
   Eb  

   wavefuncs.dat  
  
   x1 wfa(x1) wf(a+1)(x1) ... wfb(x1)  
   x2 wfa(x2) wf(a+1)(x2) ... wfb(x2)  
   .  
   .  
   xn wfa(xn) wf(a+1)(xn) ... wfb(xn)  
  
   expvalues.dat  
  
   expval(Ea)     uncertainty(Ea)  
   expval(E(a+1)) uncertainty (E(a+1))  
   .   
   .   
   expval(Eb)     uncertainty(Eb)  
  
## Testing
   To test, if the program is working properly you can run python3 -m pyteset.  
   The Programm will then be tested with six potentials.
