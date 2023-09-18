"""importing all necessary packages and modules"""
import numpy as np
import matplotlib.pyplot as plt
from solvers import schrodinger


def visualizer(file_path):
    """funtion to visualize"""
    w, Vx, x, v, x_explist,unschärfe = schrodinger(file_path)
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.set_ylim(min(Vx)-0.25,max(w)+0.25)
    ax1.plot(x,Vx)
    for i in range(len(w)):
        #plt.plot(x,abs(v[:,i ])**2+w[i])
        ax1.set_title("Potential, eigenstates, <x>")
        ax1.set_xlabel("x [Bohr]")
        ax1.set_ylabel("Energy [Hartree]")
        ax2.set_title("σ")
        ax2.set_xlabel("x [Bohr]")
        ax2.set_ylabel("Energy [Hartree]")
        ax1.plot(x,v[:,i ]*0.2+w[i], color = 'blue')
        ax1.axhline(y = w[i], color = 'grey', linestyle = '-')
        ax1.plot(x_explist[i],w[i],marker = "x")
        ax2.axhline(y = w[i], color = 'grey', linestyle = '-')
        ax2.plot(unschärfe,w,marker = "x", color = 'blue', linestyle = ' ')
    ax2.set_ylim(min(Vx)-0.25,max(w)+0.25)
    plt.show()
    