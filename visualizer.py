"""importing all necessary packages and modules"""
import numpy as np
import matplotlib.pyplot as plt
from solvers import schrodinger


def visualizer(file_path):
    """funtion to visualize"""
    w_sol_dp = schrodinger(file_path)
    Vx = w_sol_dp[1]
    w = w_sol_dp[0]
    x = w_sol_dp[2]
    v = w_sol_dp[3]

    plt.ylim(min(Vx)-1,max(w)+1)
    plt.plot(x,Vx)
    for i in range(len(w)):
        plt.plot(x,abs(v[:,i ])**2+w[i])
        plt.plot(x,v[:,i ]/3+w[i])
    plt.show()
    