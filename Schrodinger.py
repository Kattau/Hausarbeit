from solvers import schrodinger
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

#file_path = input('Enter a file path: ')
#schrodinger(file_path)

w_sol_dp = schrodinger('/Users/marenbackes/Hausarbeit/schrodinger_dPT.inp')
print(w_sol_dp)