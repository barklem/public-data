import numpy as np
import sys, os

# Usage: eg for all tested cases, at 1000K, for all MN channels from inital ionic ground states
# cases = ["C+H", "Ca+H", "Fe+H", "K+H", "Mn+H", "N+H", "O+H", "Rb+H", "Ti+H"]
# for c in cases:
#     get_rates(c, 1000, bf_cut = 0.1, mn_groundstate_only = True)

# Works for: C+H,Ca+H, Fe+H, K+H, Mn+H, N+H, O+H, Rb+H, Ti+H, Li+H, Mg+H, Na+H, Si+H

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

    print("\n\n  {:10} T = {:8d} K         E[cm-1]    Rate[-1]     BF[%]".format(c, int(temp)))

    # inital states (columns)
    for i in range(len(states)):
        if mn_groundstate_only and '+' in states[i, -2]:
            # final states (rows)
            sum_rates = np.sum(rates[:, i])
            print("\n  {:28} {:12.1f}".format(states[i, -2], float(states[i,-1])))
            for j in range(len(states)):
                if sum_rates > 1e-40:
                    if 100*rates[j, i]/sum_rates >= bf_cut:
                        print("  ----->  {:20} {:12.1f} {:12.3e} {:8.2f}".format(
                            states[j, -2], float(states[j, -1]), rates[j, i], 100*rates[j, i]/sum_rates))
            break

        elif not mn_groundstate_only:
            # final states (rates rows)
            sum_rates = np.sum(rates[:, i])
            print("\n  {:28} {:12.1f}".format(states[i, -2], float(states[i,-1])))
            for j in range(len(states)):
                if sum_rates > 1e-40:
                    if 100*rates[j, i]/sum_rates >= bf_cut:
                        print("  ----->  {:20} {:12.1f} {:12.3e} {:8.2f}".format(
                            states[j, -2], float(states[j, -1]), rates[j, i], 100*rates[j, i]/sum_rates))
        else:
            continue

# Test
cases = ["Li+H", "C+H", "N+H", "O+H", "Na+H", "Mg+H", "Si+H", "K+H", "Ca+H", "Ti+H", "Mn+H", "Fe+H", "Rb+H"]
temps = [1000, 3000, 7000]

for T in temps:
    for c in cases:
        get_rates(c, T, bf_cut = 0.00, mn_groundstate_only = True)
