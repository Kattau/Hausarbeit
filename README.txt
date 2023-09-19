**********************************
Solver of the schrodinger equation
**********************************

***********
Description
***********
This application uses an imputfile in a given Format to solve the schrodinger equation under the given Conditions.
The solutions are saved as multiple .dat files. THe application also presents the user with a grafic containing the processed data.
To solve the schrodinger equation a method of representing the problem as a matrix is used to find the eigenvalues. 
For the simplicity, the solver uses atomic units and the solutions are presented in the units Hartree for energy and Bohr for the distance.
The results of this application are the values for the used potential, the eigenvalues and wavefunctions, the expected values for x and x squared, as well as their uncertainty.

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
The results will be located in the same directory as the input file. 