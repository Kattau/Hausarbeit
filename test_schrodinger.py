"""importing necessary packages and modules"""
import numpy as np
from solvers import schrodinger

def test_schrodinger_infp():
    """Test for infinitely deep potential pot"""
    w_sol_infp = list(schrodinger('schrodinger_uePT.inp'))
    print(w_sol_infp)
    potentials_sol_infp = w_sol_infp[1]
    w_ref_infp = [[0.61623307, 1.38652299, 2.46492621, 3.854407, 5.54606116], [0, 0, 0, 0, 0]]
    assert np.all(w_sol_infp[0] - w_ref_infp[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(w_ref_infp[0] - w_sol_infp[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_infp[0:5] - w_ref_infp[1] < 0.01) #testing for potentials
    assert np.all(w_ref_infp[1] - potentials_sol_infp[0:5] < 0.01) #testing for potentials


def test_schrodinger_p():
    """Test for potential pot"""
    w_sol_p = schrodinger('schrodinger_ePT.inp')
    print(w_sol_p)
    potentials_sol_p = w_sol_p[1]
    w_ref_p = [[-4.61321566,  0.17345711,  1.05563221], [0, 0, 0, 0, 0]]
    assert np.all(w_sol_p[0] - w_ref_p[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(w_ref_p[0] - w_sol_p[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_p[0:5] - w_ref_p[1] < 0.01) #testing for potentials
    assert np.all(w_ref_p[1] - potentials_sol_p[0:5] < 0.01) #testing for potentials


def test_schrodinger_ho():
    """Test for harmonic oszillator"""
    w_sol_ho = schrodinger('schrodinger_HO.inp')
    print(w_sol_ho)
    potentials_sol_ho = w_sol_ho[1]
    w_ref_ho = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert np.all(w_sol_ho[0] - w_ref_ho[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(w_ref_ho[0] - w_sol_ho[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_ho[0:5] - w_ref_ho[1] < 0.01) #testing for potentials
    assert np.all(w_ref_ho[1] - potentials_sol_ho[0:5] < 0.01) #testing for potentials


def test_schrodinger_dp():
    """Test for double potential pot (linear)"""
    w_sol_dp = schrodinger('schrodinger_dPT.inp')
    print(w_sol_dp)
    potentials_sol_dp = w_sol_dp[1]
    w_ref_dp = [[-1.14450859, -0.49765423, -0.49765423,  0.04366327,  0.04366332, 0.53122844,  0.53123715,  0.98144827,  0.98192219,  1.39689457, 1.40720664,  1.74911269,  1.83146143,  2.09096569,  2.29555329, 2.55231647], [100, 99.830664, 99.66132799, 99.49199199, 99.32265599, 99.15331999, 98.98398398, 98.81464798, 98.64531198, 98.47597598, 98.30663997, 98.13730397, 97.96796797, 97.79863197, 97.62929596, 97.45995996, 97.29062396]]
    assert np.all(w_sol_dp[0] - w_ref_dp[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(w_ref_dp[0] - w_sol_dp[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_dp[0:5] - w_ref_dp[1] < 0.01) #testing for potentials
    assert np.all(w_ref_dp[1] - potentials_sol_dp[0:5] < 0.01) #testing for potentials


def test_schrodinger_dp_cubic():
    """Test for double potential pot (natural cubic spline)"""
    w_sol_dp_cubic = schrodinger('schrodinger_dPT(kubisch).inp')
    print(w_sol_dp_cubic)
    potentials_sol_dp_cubic = w_sol_dp_cubic[1]
    w_ref_dp_cubic = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert np.all(w_sol_dp_cubic[0] - w_ref_dp_cubic[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(w_ref_dp_cubic[0] - w_sol_dp_cubic[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_dp_cubic[0:10] - w_ref_dp_cubic[1] < 0.01) #testing for potentials
    assert np.all(w_ref_dp_cubic[1] - potentials_sol_dp_cubic[0:10] < 0.01) #testing for potentials


def test_schrodinger_ap():
    """asymmetrical potential pot"""
    w_sol_ap = schrodinger('schrodinger_aPT.inp')
    print(w_sol_ap)
    potentials_sol_ap = w_sol_ap[1]
    w_ref_ap = [[ 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0]]
    assert np.all(w_sol_ap[0] - w_ref_ap[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(w_ref_ap[0] - w_sol_ap[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_ap[0:7] - w_ref_ap[1] < 0.01) #testing for potentials
    assert np.all(w_ref_ap[1] - potentials_sol_ap[0:7] < 0.01) #testing for potentials
