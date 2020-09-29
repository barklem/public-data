import numpy as np
import sys, os

# Usage: eg for all tested cases, at 1000K, for all MN channels from inital ionic ground states
# cases = ["C+H", "Ca+H", "Fe+H", "K+H", "Mn+H", "N+H", "O+H", "Rb+H", "Ti+H"]
# for c in cases:
#     get_rates(c, 1000, bf_cut = 0.1, mn_groundstate_only = True)

# Cases so far: C+H, Ca+H, Fe+H, K+H, Mn+H, N+H, O+H, Rb+H, Ti+H, Li+H, Mg+H, Na+H, Si+H

# Hydrogen electron affinity: 6082.99±0.15 cm-1 (Lykke et al. PRA, 1991, 43, 11, 6104, https://doi.org/10.1103/PhysRevA.43.6104)
# --------------------------------------------------------------------------------------------------------------------------
# At. num | Sp. Name  | Ground Shells (a) | Ground Level | Ionized Level     | Ionization Energy (1/cm) | References
# --------|-----------|-------------------|--------------|-------------------|--------------------------|-------------------
#       3 | Li I      | 1s2.2s            | 2S<1/2>      | 1s2 1S<0>         |         43487.11420      |            L12261
#       6 | C I       | 1s2.2s2.2p2       | 3P0          | 2s2.2p 2P*<1/2>   |         90820.348        |            L20057
#       7 | N I       | 1s2.2s2.2p3       | 4S*<3/2>     | 2p2 3P<0>         |        117225.7          |             L1411
#       8 | O I       | 1s2.2s2.2p4       | 3P<2>        | 2p3 4S*<3/2>      |        109837.02         |         L74,L3760
#      11 | Na I      | [Ne].3s           | 2S<1/2>      | 2p6 1S<0>         |         41449.451        |      L10921,L9648
#      12 | Mg I      | [Ne].3s2          | 1S0          | 3s 2S<1/2>        |         61671.05         |      L10635,L6969
#      14 | Si I      | [Ne].3s2.3p2      | 3P0          | 3p 2P*<1/2>       |         65747.76         |             L5815
#      19 | K I       | [Ar].4s           | 2S<1/2>      | 3p6 1S<0>         |         35009.8140       | L5451,L5783,L7185
#      20 | Ca I      | [Ar].4s2          | 1S0          | 4s 2S<1/2>        |         49305.9240       |             L8900
#      22 | Ti I      | [Ar].3d2.4s2      | 3F<2>        | 3d2.4s 4F<3/2>    |         55072.5          |            L17996
#      25 | Mn I      | [Ar].3d5.4s2      | 6S<5/2>      | 3d5.4s 7S<3>      |         59959.560        |            L19057
#      26 | Fe I      | [Ar].3d6.4s2      | 5D<4>        | 3d6.4s 6D<9/2>    |         63737.704        |         L7743c109
#      37 | Rb I      | [Kr].5s           | 2S<1/2>      | 4p6 1S<0>         |         33690.81         |       L4740,L5783
# --------------------------------------------------------------------------------------------------------------------------

def get_rates(case, temp, bf_cut = 0.0, mn_groundstate_only=False):
    """
        get_bfs_rates(case, temp, bf_cut = 0.0, mn_groundstate_only = False)

        Function to get branching fractions from rate coeffs for a certain pair of
        reactants at a given temperature.

        case                [str]     : case name, as corresp directory: 'public-data/<case>'
        temp                [int]     : temperature in Kelvin, e.g. 1000
        bf_cut              [float]   : branching fraction cut in percent (optional, default 0.0)
        mn_groundstate_only [boolean] : include only the mutual neutralization channel from ground state (optional, default False)

        returns a table printed to screen
    """
    # conversion factors
    eVtocm = 8065.54429

    # hydrogen electron affinity
    EA_H = 6082.99   # 6082.99±0.15 (Lykke et al. PRA, 1991, 43, 11, 6104, https://doi.org/10.1103/PhysRevA.43.6104)

    # cases and corresponding ionization energies (NIST ASD 2020)
    IE_dict = {"Li+H":43487.11420, "C+H":90820.348, "N+H":117225.7, "O+H":109837.02, "Na+H":41449.451, "Mg+H":61671.05, "Si+H":65747.76, "K+H":35009.814, "Ca+H":49305.924, "Ti+H":55072.5, "Mn+H":59959.56, "Fe+H":63737.704, "Rb+H":33690.81}
    if case in IE_dict:
        IE = IE_dict[case]
    else:
        return ' selected case {} not recognized!'.format(case)

    # define (merged) states and rates files
    file_states = "../inelastic-"+case+'/states.dat'
    file_rates  = "../inelastic-"+case+'/'+str(temp)+"_K.rates"

    # test file name definitions and update if needed
    if not os.path.isfile(file_states):
        # if states file doesn't exist - there's probably a separate folder with LCAO data
        file_states = "../inelastic-"+case+'/LCAOdata/merged_states.txt'
        file_rates  = "../inelastic-"+case+'/LCAOdata/'+str(temp)+"_K.rates"
        if not os.path.isfile(file_states):
            print(" Error: missing rates file {}!".format(file_states))
    if not os.path.isfile(file_rates):
        # if rate file isn't found then they are probaly in a separate rates folder
        file_rates = "../inelastic-"+case+'/rates/'+str(temp)+"_K.rates"
        if not os.path.isfile(file_rates):
            print(" Error: missing rates file {}!".format(file_rates))
    if (not os.path.isfile(file_states)) or (not os.path.isfile(file_rates)):
        return ' File(s) missing.'

    # load data for selected case and temperature
    states = np.loadtxt(file_states, dtype='str')
    rates  = np.loadtxt(file_rates)

    print("\n\n  {:10} T = {:8d} K           E[eV]      KER[eV]     Rate[-1]    BF[%]".format(c, int(temp)))

    # inital states (columns)
    for i in range(len(states)):
        if mn_groundstate_only and '+' in states[i, -2]:
            # final states (rows)
            sum_rates = np.sum(rates[:, i])
            print("  {:28} {:12.6f}".format(states[i, -2], float(states[i,-1])/eVtocm))
            for j in range(len(states)):
                if sum_rates > 1e-40 and states[i, -2] != states[j, -2] and not '+' in states[j, -2]:
                    if 100*rates[j, i]/sum_rates >= bf_cut:
                        E_LS = float(states[j, -1])/eVtocm                   # LS-averaged energy
                        KER  = (IE - EA_H - float(states[j, -1]))/eVtocm     # kinetic energy release
                        print("  ----->  {:20} {:12.6f} {:12.6f} {:12.3e} {:8.2f}".format(
                            states[j, -2], E_LS, KER, rates[j, i], 100*rates[j, i]/sum_rates))
            break

        elif not mn_groundstate_only:
            # final states (rates rows)
            sum_rates = np.sum(rates[:, i])
            print("  {:28} {:12.6f}".format(states[i, -2], float(states[i,-1])/eVtocm))
            for j in range(len(states)):
                if sum_rates > 1e-40:
                    if 100*rates[j, i]/sum_rates >= bf_cut and states[i, -2] != states[j, -2]:
                        E_LS = float(states[j, -1])/eVtocm                   # LS-averaged energy
                        KER  = (IE - EA_H - float(states[j, -1]))/eVtocm     # kinetic energy release
                        print("  ----->  {:20} {:12.6f} {:12.6f} {:12.3e} {:8.2f}".format(
                            states[j, -2], E_LS, KER, rates[j, i], 100*rates[j, i]/sum_rates))
            print()
        else:
            continue

# Test
cases   = ["Li+H", "C+H", "N+H", "O+H", "Na+H", "Mg+H", "Si+H", "K+H", "Ca+H", "Ti+H", "Mn+H", "Fe+H", "Rb+H"]
temps = [1000, 3000, 5000, 7000, 9000]

for T in temps:
    for c in cases:
        get_rates(c, T, bf_cut = 1.0e-10, mn_groundstate_only = True)
