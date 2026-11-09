import numpy as np



def random_walks(N, M_values, rng):

    #empty lists to store the arrays of each simulation
    simulations = []


    for M in M_values:

    #create a array with M[i] zeros
        steps = rng.choice([-1, 1], size=(M, N))

        final_postion = np.sum(steps, axis=1)

        simulations.append(final_postion)


    return simulations

def two_dimensional_walks(M, rng):

        #empty lists to store the arrays of each simulation
    postion = np.array([0.0, 0.0])

    for i in range(M):

    #random vector
        step = rng.normal(0.0, 1.0, size=2)
        step = step / np.linalg.norm(step)

        postion = postion + step


    return postion


def three_dimensional_walks(M, rng):

        #empty lists to store the arrays of each simulation
    postion = np.array([0.0, 0.0, 0.0])

    for i in range(M):

    #random vector
        step = rng.normal(0.0, 1.0, size=3)
        step = step / np.linalg.norm(step)

        postion = postion + step


    return postion