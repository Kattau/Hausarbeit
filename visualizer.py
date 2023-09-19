"""importing all necessary packages and modules"""
import matplotlib.pyplot as plt
from solvers import schrodinger


def visualizer(file_path):
    """funtion to visualize"""
    eigen, vx_potential, x_value, v_potent, x_explist, uncertainty = schrodinger(file_path)
    fig,(ax1, ax2) = plt.subplots(1, 2)

    ax1.set_ylim(min(vx_potential)-0.25,max(eigen)+0.25)
    ax1.plot(x_value, vx_potential)
    for i in range(len(eigen)):
        #plt.plot(x,abs(v_potent[:,i ])**2+eigen[i])
        ax1.set_title("Potential, eigenstates, <x>")
        ax1.set_xlabel("x [Bohr]")
        ax1.set_ylabel("Energy [Hartree]")
        ax2.set_title("σ")
        ax2.set_xlabel("x [Bohr]")
        ax2.set_ylabel("Energy [Hartree]")
        ax1.plot(x_value, v_potent[:,i ]*0.2+eigen[i], color = 'blue')
        ax1.axhline(y_value = eigen[i], color = 'grey', linestyle = '-')
        ax1.plot(x_explist[i], eigen[i], marker = "x")
        ax2.axhline(y_value = eigen[i], color = 'grey', linestyle = '-')
        ax2.plot(uncertainty, eigen, marker = "x", color = 'blue', linestyle = ' ')
    ax2.set_ylim(min(vx_potential)-0.25, max(eigen)+0.25)
    plt.show()
    