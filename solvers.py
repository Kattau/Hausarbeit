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
<<<<<<< HEAD
    E: Array, number of Eigenvalues to find
=======
    E: Array, Eigenvalues to find
>>>>>>> 28778fd24e582cdbe891ec5498bbc0e1783761a1
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
<<<<<<< HEAD
    V=interp1d(xx,yy,Data[3].split()[0])
    Vx=V(x)
    Delta= (float(xstring[1]) - float(xstring[0]))/int(xstring[2])
    np.savetxt('potential.txt',np.c_[x, Vx])
=======

    if Data[3].split()[0] =='cspline':
        V=interp1d(xx,yy,'cubic')
        Vx=V(x)
    if Data[3].split()[0] =='polynomial':
        V=np.polyfit(xx,yy,2)    
        Vx=V[0]*x**2+V[1]*x+V[2] 
    if Data[3].split()[0] =='linear':
        V=interp1d(xx,yy,'linear')
        Vx=V(x)

    Delta= (float(xstring[1]) - float(xstring[0]))/int(xstring[2])
    np.savetxt('potential.dat',np.c_[x, Vx])
>>>>>>> 28778fd24e582cdbe891ec5498bbc0e1783761a1
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
<<<<<<< HEAD
    np.savetxt('Eigenstates.txt',np.c_[x, v])
    np.savetxt('Eigenvalues.txt',w)
    #plt.ylim(min(Vx)-1,max(w)+1)
    #plt.plot(x,Vx)
    #for i in range(len(w)):
    #    plt.plot(x,v[:,i ]+w[i])
    #plt.show()
    result = (w, Vx)
    return(result)
=======

    for i in range((E[1]-E[0])+1):
        norm = 0
        for n in range(len(v)):
            norm = norm + Delta*(v[n][i])**2
        for n in range(len(v)):
            v[n][i]=v[n][i]/(np.sqrt(norm))

    x_explist=[]
    for i in range((E[1]-E[0])+1):
        x_exp = 0
        for n in range(len(v)):
            x_exp = x_exp + Delta*(v[n][i])*(v[n][0])*(v[n][i])
        x_explist.append(x_exp)
    
    x_sqlist=[]
    for i in range((E[1]-E[0])+1):
        x_sq = 0
        for n in range(len(v)):
            x_sq = x_sq + Delta*(v[n][i])*(v[n][0])**2*(v[n][i])
        x_sqlist.append(x_sq)

    unschärfe=[]
    for n in range(len(x_explist)):
        unschärfe.append(np.sqrt(x_sqlist[n]-(x_explist[n])**2))
    
    np.savetxt('wavefuncs.dat',np.c_[x, v])
    np.savetxt('energies.dat',w)
    np.savetxt('expvalues.dat',np.c_[x_explist, unschärfe])

    plt.ylim(min(Vx)-1,max(w)+1)
    plt.plot(x,Vx)
    for i in range(len(w)):
        #plt.plot(x,abs(v[:,i ])**2+w[i])
        plt.plot(x,v[:,i ]/3+w[i])
    plt.show()
    return(w)
>>>>>>> 28778fd24e582cdbe891ec5498bbc0e1783761a1
