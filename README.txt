**********************************
Solver of the schrodinger equation
**********************************

***********
Description
***********

This application uses an inputfile in a given format to solve the schrodinger equation under the given conditions.
The solutions are saved as multiple ".dat" files.
To solve the schrodinger equation a method of representing the problem as a matrix is used to find the eigenvalues. 
For the simplicity, the solver uses atomic units and the solutions are presented in the units Hartree for energy and Bohr for the distance.
The results of this application are the values for the used potential, the eigenvalues and wavefunctions, the expected values for x and x squared, as well as their uncertainty.
The visualizer.py application uses the generated files from schrodinger.py to create a plot showing the results. 

***********
How to Use the Project
***********

To start using the application, the modules numpy, scipy, matplotlib, os and argparse are required.
The inputfile schould use the following format and be called schrodinger.inp:

mass of the object
xMin xMax nomber of points
first and last eigenvalue to print
interpolation type (eg.: linear, polynomial, cspline)
nr. of interpolation points
xy declarations for the interpolation points in the following rows

The schrodinger.inp file is expected to be in the same directory as the application.
Should that not be the case, the directory can be changed by adding -d "directory path" when running the script.
Example: python schrodinger.py -d C:/Users/test
Please use "/" when giving the optional argument. Using "\", the input won't be detected as a file path.
The results will be located in the same directory as the input file. 

The application visualizer.py expects the ".dat" files created using the application schrodinger.py as input to generate an image.
Using the option -d while running the script changes the searched path in the same way as schrodinger.py.
The option -s (eg.: python schrodinger.py -s 0.2) scales the values of the plotted wavefunctions by that factor to increase visibility of the lines