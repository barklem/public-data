import numpy as np
import sys, os

# Usage: eg for all tested cases, at 1000K, for all MN channels from inital ionic ground states
# cases = ["C+H", "Ca+H", "Fe+H", "K+H", "Mn+H", "N+H", "O+H", "Rb+H", "Ti+H"]
# for c in cases:
#     get_rates(c, 1000, bf_cut = 0.1, mn_groundstate_only = True)

# Works for:
# C+H Ca+H Fe+H K+H Mn+H N+H O+H Rb+H Ti+H

# Not yet (non-standard data format)
# Li+H - single file
# Mg+H - single file
# Na+H - single file
# Si+H - multiple files, but states included in each

def get_rates(case, temp, bf_cut = 0.0, mn_groundstate_only=False):
    """
        get_rates(case, temp, bf_cut = 0.0, mn_groundstate_only = False)

        Function to get rates and branching fractions for a certain pair of reactants at a given temperature.

        case                [str]     : case name, e.g. 'Ti+H'
        temp                [int]     : temperature in Kelvin, e.g. 1000
        bf_cut              [float]   : branching fraction cut in percent (optional, default 0.0)
        mn_groundstate_only [boolean] : include only the mutual neutralization channel from ground state (optional, default False)

        returns a table printed to screen
    """

    # first, check special cases (these are not implemented yet, just defining the file)
    if case == "Si+H":
        file_rates  = "../inelastic-"+case+'/rt_'+str(temp)+".dat"
        file_states = ""
        sys.exit(' case not implemented yet!')
    elif case == "Li+H":
        file_rates  = "../inelastic-"+case+'/lih_rates.txt'
        file_states = ""
        sys.exit(' case not implemented yet!')
    elif case == "Mg+H":
        file_rates  = "../inelastic-"+case+'/MgH_rates.txt'
        file_states = ""
        sys.exit(' case not implemented yet!')
    elif case == "Na+H":
        file_rates  = "../inelastic-"+case+'/NaH_rates.txt'
        file_states = ""
        sys.exit(' case not implemented yet!')
    else:
        # standard file structure
        file_states = "../inelastic-"+case+'/states.dat'
        file_rates = "../inelastic-"+case+'/'+str(temp)+"_K.rates"
        if not os.path.isfile(file_states):
            print(" Error: missing states file {}!".format(file_states))

        if not os.path.isfile(file_rates):
            file_rates = "../inelastic-"+case+'/rates/'+str(temp)+"_K.rates"
            if not os.path.isfile(file_rates):
                print(" Error: missing rates file {}!".format(file_rates))

        if (not os.path.isfile(file_states)) or (not os.path.isfile(file_rates)):
            return ' File(s) missing.'

    states = np.loadtxt(file_states, dtype='str')
    rates = np.loadtxt(file_rates)

    # inital states (rates columns)
    for i in range(len(states)):
        if mn_groundstate_only and '+' in states[i, -2]:
            # final states (rates rows)
            sum_rates = np.sum(rates[:, i])
            print("  {:20}".format(states[i, -2]))
            for j in range(len(states)):
                if 100*rates[j, i]/sum_rates >= bf_cut:
                    print("  ----->  {:20} {:10} {:8.2f}".format(
                        states[j, -2], rates[j, i], 100*rates[j, i]/sum_rates))
            break

        elif not mn_groundstate_only:
            # final states (rates rows)
            sum_rates = np.sum(rates[:, i])
            print("  {:20}".format(states[i, -2]))
            for j in range(len(states)):
                if 100*rates[j, i]/sum_rates >= bf_cut:
                    print("  ----->  {:20} {:10} {:8.2f}".format(
                        states[j, -2], rates[j, i], 100*rates[j, i]/sum_rates))
        else:
            continue

