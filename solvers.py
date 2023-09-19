"""Importing all necessary packages and modules"""
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d

def _unpacker(file_path: str):
    """Takes a File as Input and outputs seperated variables for further use
    Input: Txt File in the given Format;

    Output:
    v_potential: Array, Potential from the given Interpolation
    mass: Variable, Mass of the Object
    x_value: Array, x-Values for the Solver
    eigenv: Array, Eigenvalues to find
    """
    with open(file_path, encoding = "utf-8") as file:
        data = file.readlines()
    mass=float(data[0].split()[0])
    eigenv=[int(data[2].split()[0])-1]
    eigenv.append(int(data[2].split()[1])-1)
    xstring=data[1].split()
    x_value=np.linspace(float(xstring[0]),float(xstring[1]),int(xstring[2]))
    xx_value=[]
    yy_value=[]
    for variable in range(int(data[4].split()[0])):
        xx_value.append(float(data[variable+5].split()[0]))
        yy_value.append(float(data[variable+5].split()[1]))

    if data[3].split()[0] =='cspline':
        v_potential=interp1d(xx_value,yy_value,'cubic')
        vx_potential=v_potential(x_value)
    if data[3].split()[0] =='polynomial':
        v_potential=np.polyfit(xx_value,yy_value,2)
        vx_potential=v_potential[0]*x_value**2+v_potential[1]*x_value+v_potential[2]
    if data[3].split()[0] =='linear':
        v_potential=interp1d(xx_value,yy_value,'linear')
        vx_potential=v_potential(x_value)

    delta= (float(xstring[1]) - float(xstring[0]))/int(xstring[2])
    np.savetxt('potential.dat',np.c_[x_value, vx_potential])
    return( vx_potential , mass , x_value , eigenv , delta)

def schrodinger(file_path: str):
    """Solves the Schrodinger Equation for given Parameters and Potential and saves the Output in seperat files.
    Input: Txt File

    Output:
    eigen: Array, Eigenvalues in the given Interval
    """
    vx_potential,mass,x_value,eigenv,delta =_unpacker(file_path)
    diag= 1/(mass*delta**2)+vx_potential
    ndiag= [-1/2*1/(mass*delta**2)]*(len(x_value)-1)
    eigen,v_potent=sp.linalg.eigh_tridiagonal(diag,ndiag,select='i',select_range=eigenv)

    for i in range((eigenv[1]-eigenv[0])+1):
        norm = 0
        for num in range(len(v_potent)):
            norm = norm + delta*(v_potent[num][i])**2
        for num in range(len(v_potent)):
            v_potent[num][i]=v_potent[num][i]/(np.sqrt(norm))

    x_explist=[]
    for i in range((eigenv[1]-eigenv[0])+1):
        x_exp = 0
        for num in range(len(v_potent)-1):
            x_exp = x_exp + delta*(v_potent[num+1][i])*x_value[num+1]*(v_potent[num+1][i])
        x_explist.append(x_exp)

    x_sqlist=[]
    for i in range((eigenv[1]-eigenv[0])+1):
        x_sq = 0
        for num in range(len(v_potent)-1):
            x_sq = x_sq + delta*(v_potent[num+1][i])*x_value[num+1]**2*(v_potent[num+1][i])
        x_sqlist.append(x_sq)

    uncertainty=[]
    for num in range(len(x_explist)):
        uncertainty.append(np.sqrt(x_sqlist[num]-(x_explist[num])**2))

    path=" "
    if len(file_path)>15:
        path=file_path[0:-15]


    np.savetxt(str(path) +'wavefuncs.dat',np.c_[x_value, v_potent])
    np.savetxt(str(path) +'energies.dat',eigen)
    np.savetxt(str(path) +'expvalues.dat',np.c_[x_explist, uncertainty])

    return(eigen, vx_potential, x_value, v_potent, x_explist,uncertainty)
