from solvers import schrodinger
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import pytest
from solvers import _unpacker


"""Test for infinitely deep potential pot""" 
w_sol_infP = schrodinger('/Users/marenbackes/Hausarbeit/schrodinger_uePT.inp')
print(w_sol_infP)
w_ref_infP = [0.61623307, 1.38652299, 2.46492621, 3.854407, 5.54606116]
assert np.all(w_sol_infP - w_ref_infP < 0.01)
assert np.all(w_ref_infP - w_sol_infP < 0.01)
    

"""Test for potential pot"""    
w_sol_P = schrodinger('/Users/marenbackes/Hausarbeit/schrodinger_ePT.inp')
print(w_sol_P)
w_ref_P = [-4.61321566, 0.17345711, 1.05563221]
#assert np.all(w_sol_P - w_ref_P < 0.01)
#assert np.all(w_ref_P - w_sol_P < 0.01)    
    
"""Test for harmonic oszillator"""
#w_sol_HO = schrodinger('/Users/marenbackes/Hausarbeit/schrodinger_HO.inp')
#print(w_sol_HO)
#w_ref_HO = [0.61623307, 1.38652299, 2.46492621, 3.854407, 5.54606116]
#assert np.all(w_sol_HO - w_ref_HO < 0.01)
#assert np.all(w_ref_HO - w_sol_HO < 0.01)


"""Test for double potential pot (linear)"""
w_sol_dP = schrodinger('/Users/marenbackes/Hausarbeit/schrodinger_dPT.inp')
print(w_sol_dP)
w_ref_dP = [-1.14450859, -0.49765423, -0.49765423, 0.04366327, 0.04366332, 0.53122844, 0.53123715, 0.98144827, 0.98192219, 1.39689457, 1.40720664, 1.74911269, 1.83146143, 2.09096569, 2.29555329, 2.55231647]
#assert np.all(w_sol_dP - w_ref_dP < 0.01)
#assert np.all(w_ref_dP - w_sol_dP < 0.01)


"""Test for double potential pot (natural cubic spline)"""
#w_sol_dP_cubic = schrodinger('/Users/marenbackes/Hausarbeit/schrodinger_dPT(kubisch).inp')
#print(w_sol_dP_cubic)
#w_ref_dP_cubic = [0.61623307, 1.38652299, 2.46492621, 3.854407, 5.54606116]
#assert np.all(w_sol_dP_cubic - w_ref_dP_cubic < 0.01)
#assert np.all(w_ref_dP_cubic - w_sol_dP_cubic < 0.01)


"""asymmetrical potential pot"""
#w_sol_aP = schrodinger('/Users/marenbackes/Hausarbeit/schrodinger_aPT.inp')
#print(w_sol_aP)
#w_ref_aP = [0.61623307, 1.38652299, 2.46492621, 3.854407, 5.54606116]
#assert np.all(w_sol_aP - w_ref_aP < 0.01)
#assert np.all(w_ref_aP - w_sol_aP < 0.01)