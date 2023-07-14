import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
def _unpacker(file_path: str):
    """Takes a File as Input and outputs seperated variables for further use
    Input: Txt File in the given Format;

    Output:
    V: Array, Potential from the given Interpolation
    M: Variable, Mass of the Object
    x: Array, x-Values for the Solver
    E: Array, Eigenvalues to find
    """
    with open(file_path) as f:
        Data = f.readlines()
    M=float(Data[0].split()[0])
    E=[int(Data[2].split()[0])]
    E.append(int(Data[2].split()[1]))
    xstring=Data[1].split()
    x=np.linspace(float(xstring[0]),float(xstring[1]),int(xstring[2]))
    xx=[]
    yy=[]
    for ii in range(len(Data)-5):
        xx.append(float(Data[ii+5].split()[0]))
        yy.append(float(Data[ii+5].split()[1]))
    V=interp1d(xx,yy,Data[3].split()[0])
    Vx=V(x)
    Delta= (float(xstring[1]) - float(xstring[0]))/int(xstring[2])
    np.savetxt('potential.txt',np.c_[x, Vx])
    return( Vx , M , x , E , Delta)

def schrodinger(file_path: str):
    """Solves the Schrodinger Equation for given Parameters and Potential and saves the Output in seperat files.
    Input: Txt File

    Output:
    w: Array, Eigenvalues in the given Interval
    """
    Vx,M,x,E,Delta =_unpacker(file_path)
    diag= 1/(M*Delta**2)+Vx
    ndiag= [-1/2*1/(M*Delta**2)]*(len(x)-1)
    w,v=sp.linalg.eigh_tridiagonal(diag,ndiag,select='i',select_range=E)
    np.savetxt('Eigenstates.txt',np.c_[x, v])
    np.savetxt('Eigenvalues.txt',w)
    plt.ylim(min(Vx)-1,max(w)+1)
    plt.plot(x,Vx)
    for i in range(len(w)):
        plt.plot(x,v[:,i ]+w[i])
    plt.show()
    return(w)
file_path = input('Enter a file path: ')
schrodinger(file_path)