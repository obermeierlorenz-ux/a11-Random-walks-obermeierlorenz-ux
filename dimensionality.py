import numpy as np
import matplotlib.pyplot as plt


#initial conditions

N = 10_000
M_values = [100, 1000, 4000, 7000, 10000]

rng = np.random.default_rng(44)


def random_walks(N, M_values, rng):

    #empty lists to store the arrays of each simulation
    simulations = []


    for M in M_values:

    #create a array with M[i] zeros
        steps = rng.choice([-1, 1], size=(M, N))

        final_postion = np.sum(steps, axis=1)

        simulations.append(final_postion)


    return simulations

simulations = random_walks(N, M_values, rng)

for i in range(len(simulations)):
    plt.hist(simulations[i], bins=100, density=True)#
    plt.xlabel('x')
    plt.ylabel('Probability density')
    plt.show()


