from solvers import schrodinger
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import pytest
 
w_sol_infP = schrodinger('/Users/marenbackes/Hausarbeit/schrodinger_uePT.inp')
print(w_sol_infP)
w_ref_infP = [0.61623307, 1.38652299, 2.46492621, 3.854407, 5.54606116]
assert np.all(w_sol_infP - w_ref_infP < 0.01)
assert np.all(w_ref_infP - w_sol_infP < 0.01)
    
    
