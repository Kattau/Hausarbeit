import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import os
def _unpacker(file_path):
    """Takes a FIle as Input and outputs seperated variables for further use
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
    E=np.array(Data[2].split()[0:2])
    xstring=Data[1].split()
    x=np.linspace(float(xstring[0]),float(xstring[1]),int(xstring[2]))
    xx=[]
    yy=[]
    for ii in range(len(Data)-5):
        xx.append(float(Data[ii+5].split()[0]))
        yy.append(float(Data[ii+5].split()[1]))
    V=interp1d(xx,yy,Data[3].split()[0])
    Vx=V(x)
    np.savetxt('potential.txt',np.c_[x, Vx])
    print(np.c_[x, Vx])
    return(V,M,x,E)
file_path = input('Enter a file path: ')
_unpacker(file_path)