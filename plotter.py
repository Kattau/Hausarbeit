"""importing all necessary packages and modules"""
import matplotlib.pyplot as plt
import numpy as np


def _unpacker(file_path: str, scalar: float):
    x_value= np.loadtxt(file_path + "/potential.dat")[:,0]
    vx_potential = np.loadtxt(file_path + "/potential.dat")[:,1]
    eigen = np.loadtxt(file_path + "/energies.dat")
    v_potent = np.loadtxt(file_path + "/wavefuncs.dat")
    x_explist = np.loadtxt(file_path + "/expvalues.dat")[:,0]
    uncertainty = np.loadtxt(file_path + "/expvalues.dat")[:,1]
    return(eigen, vx_potential, x_value, v_potent, x_explist, uncertainty)

def visualizer(file_path: str, scalar: float):
    """funtion to visualize"""
    eigen, vx_potential, x_value, v_potent, x_explist, uncertainty = _unpacker(file_path, scalar)
    fig,(ax1, ax2) = plt.subplots(1, 2)

    ax1.set_ylim(min(vx_potential)-0.25,max(eigen)+0.25)
    ax1.plot(x_value, vx_potential)
    for i in range(len(eigen)):
        ax1.set_title("Potential, eigenstates, <x>")
        ax1.set_xlabel("x [Bohr]")
        ax1.set_ylabel("Energy [Hartree]")
        ax2.set_title("σ")
        ax2.set_xlabel("x [Bohr]")
        ax2.set_ylabel("Energy [Hartree]")
        ax1.plot(x_value, v_potent[:,i+1 ]*scalar+eigen[i], color = 'blue')
        ax1.axhline(y = eigen[i], color = 'grey', linestyle = '-')
        ax1.plot(x_explist[i], eigen[i], marker = "x")
        ax2.axhline(y = eigen[i], color = 'grey', linestyle = '-')
        ax2.plot(uncertainty, eigen, marker = "x", color = 'blue', linestyle = ' ')
    ax2.set_ylim(min(vx_potential)-0.25, max(eigen)+0.25)
    plt.show()
