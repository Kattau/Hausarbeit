"""Use data found in a directory to plot the results of the schrodinger equation"""
import matplotlib.pyplot as plt
import numpy as np


def _unpacker(file_path: str, scalar: float):
    """Takes a File as Input and outputs seperated variables for further use
    Input: file path to a .dat file in the given format;

    Output:
    eigen: Array, Eigenvalues in the given Interval
    vx_potential: array, potential used in solving the equation
    x_value: array, x-values for the solver
    wavef: array, wavefunctions as a result of the solver
    x_explist: array, list of the expected values
    uncertainty: array, uncertainty corresponding to a specific energy
    """
    x_value= np.loadtxt(file_path + "/potential.dat")[:,0]
    vx_potent = np.loadtxt(file_path + "/potential.dat")[:,1]
    eigen = np.loadtxt(file_path + "/energies.dat")
    wavef = np.loadtxt(file_path + "/wavefuncs.dat")
    x_explist = np.loadtxt(file_path + "/expvalues.dat")[:,0]
    uncertainty = np.loadtxt(file_path + "/expvalues.dat")[:,1]
    return(eigen, vx_potent, x_value, wavef, x_explist, uncertainty, scalar)

def visualizer(file_path: str, scalar: float):
    """funtion to visualize the imported data"""
    eigen, vx_potent, x_value, wavef, x_explist, uncertainty, scalar = _unpacker(file_path, scalar)
    fig,(ax1, ax2) = plt.subplots(1, 2)

    ax1.set_ylim(min(vx_potent)-0.25,max(eigen)+0.25)
    ax1.plot(x_value, vx_potent)
    for i in range(len(eigen)):
        ax1.set_title("Potential, eigenstates, <x>")
        ax1.set_xlabel("x [Bohr]")
        ax1.set_ylabel("Energy [Hartree]")
        ax2.set_title("σ")
        ax2.set_xlabel("x [Bohr]")
        ax2.set_ylabel("Energy [Hartree]")
        ax1.plot(x_value, wavef[:,i+1 ]*scalar+eigen[i], color = 'blue')
        ax1.axhline(y = eigen[i], color = 'grey', linestyle = '-')
        ax1.plot(x_explist[i], eigen[i], color = 'red', marker = "x")
        ax2.axhline(y = eigen[i], color = 'grey', linestyle = '-')
        ax2.plot(uncertainty, eigen, marker = "x", color = 'red', linestyle = ' ')
    ax2.set_ylim(min(vx_potent)-0.25, max(eigen)+0.25)
    plt.show()
