"""importing necessary packages and modules"""
import numpy as np
from solvers import schrodinger

def test_schrodinger_infp():
    """Test for infinitely deep potential pot"""
    e_sol_infp = list(schrodinger('schrodinger_uePT.inp'))
    print(e_sol_infp)
    potentials_sol_infp = e_sol_infp[1]
    e_ref_infp = [[0.15405836, 0.61623307, 1.38652299, 2.46492621, 3.85144007], [0, 0, 0, 0, 0]]
    assert np.all(e_sol_infp[0] - e_ref_infp[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(e_ref_infp[0] - e_sol_infp[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_infp[0:5] - e_ref_infp[1] < 0.01) #testing for potentials
    assert np.all(e_ref_infp[1] - potentials_sol_infp[0:5] < 0.01) #testing for potentials


def test_schrodinger_p():
    """Test for potential pot"""
    e_sol_p = schrodinger('schrodinger_ePT.inp')
    print(e_sol_p)
    potentials_sol_p = e_sol_p[1]
    e_ref_p = [[-8.58964498, -4.61321566, 0.17345711], [0, 0, 0, 0, 0]]
    assert np.all(e_sol_p[0] - e_ref_p[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(e_ref_p[0] - e_sol_p[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_p[0:5] - e_ref_p[1] < 0.01) #testing for potentials
    assert np.all(e_ref_p[1] - potentials_sol_p[0:5] < 0.01) #testing for potentials


def test_schrodinger_ho():
    """Test for harmonic oszillator"""
    eigen_sol_ho = schrodinger('schrodinger_HO.inp')
    print(eigen_sol_ho)
    potentials_sol_ho = eigen_sol_ho[1]
    eigen_ref_ho = [[0.25012434, 0.75037146, 1.25061545, 1.75085631, 2.25109403], [12.5, 12.4749875, 12.45000005, 12.42498755, 12.39997505]]
    assert np.all(eigen_sol_ho[0] - eigen_ref_ho[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(eigen_ref_ho[0] - eigen_sol_ho[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_ho[0:5] - eigen_ref_ho[1] < 0.01) #testing for potentials
    assert np.all(eigen_ref_ho[1] - potentials_sol_ho[0:5] < 0.01) #testing for potentials


def test_schrodinger_dp():
    """Test for double potential pot (linear)"""
    e_sol_dp = schrodinger('schrodinger_dPT.inp')
    print(e_sol_dp)
    potentials_sol_dp = e_sol_dp[1]
    e_ref_dp = [[-1.14450859, -1.14450859, -0.49765423, -0.49765423, 0.04366327, 0.04366332, 0.53122844, 0.53123715, 0.98144827, 0.98192219, 1.39689457, 1.40720664, 1.74911269, 1.83146143, 2.09096569, 2.29555329], [100, 99.830664, 99.66132799, 99.49199199, 99.32265599, 99.15331999, 98.98398398, 98.81464798, 98.64531198, 98.47597598, 98.30663997, 98.13730397, 97.96796797, 97.79863197, 97.62929596, 97.45995996, 97.29062396]]
    assert np.all(e_sol_dp[0] - e_ref_dp[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(e_ref_dp[0] - e_sol_dp[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_dp[0:17] - e_ref_dp[1] < 0.01) #testing for potentials
    assert np.all(e_ref_dp[1] - potentials_sol_dp[0:17] < 0.01) #testing for potentials


def test_schrodinger_dp_cubic():
    """Test for double potential pot (natural cubic spline)"""
    e_sol_dp_cubic = schrodinger('schrodinger_dPT(kubisch).inp')
    print(e_sol_dp_cubic)
    potentials_sol_dp_cubic = e_sol_dp_cubic[1]
    e_ref_dp_cubic = [[ -0.46894129, -0.46894129, -0.22476114, -0.22476114, 0.01577092, 0.01577092, 0.25237151, 0.25237151, 0.48469914, 0.48469914], [ 35, 34.85204916, 34.70449262, 34.55732989, 34.41056046, 34.26418384, 34.11819955, 33.97260709, 33.82740596, 33.68259567]]
    assert np.all(e_sol_dp_cubic[0] - e_ref_dp_cubic[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(e_ref_dp_cubic[0] - e_sol_dp_cubic[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_dp_cubic[0:10] - e_ref_dp_cubic[1] < 0.01) #testing for potentials
    assert np.all(e_ref_dp_cubic[1] - potentials_sol_dp_cubic[0:10] < 0.01) #testing for potentials


def test_schrodinger_ap():
    """asymmetrical potential pot"""
    e_sol_ap = schrodinger('schrodinger_aPT.inp')
    print(e_sol_ap)
    potentials_sol_ap = e_sol_ap[1]
    e_ref_ap = [[0.4533687, 1.1781147, 1.83591724, 2.38919812, 2.85049039, 3.23728701, 3.53887358], [ 30, 29.78564921, 29.57186961, 29.35866364, 29.14603373, 28.93398231, 28.72251181]]
    assert np.all(e_sol_ap[0] - e_ref_ap[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(e_ref_ap[0] - e_sol_ap[0] < 0.01) #testing for eigenvalues, energies
    assert np.all(potentials_sol_ap[0:7] - e_ref_ap[1] < 0.01) #testing for potentials
    assert np.all(e_ref_ap[1] - potentials_sol_ap[0:7] < 0.01) #testing for potentials
