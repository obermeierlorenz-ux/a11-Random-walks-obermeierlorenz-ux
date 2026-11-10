import numpy as np



def random_walks(N, M_values, rng):

    #empty lists to store the arrays of each simulation
    simulations = []


    for M in M_values:

    #create a array with M[i] zeros
        steps = rng.choice([-1, 1], size=(N, M))

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

def boundary(boundary, N, M, rng):


    positions = np.zeros(N, dtype=int)

    for step_number in range(M):

    #create a array with M[i] zeros
        steps = rng.choice([-1, 1], size=N)

        attempted_crossing = (positions == boundary) & (steps ==1)

        positions+= steps
        positions[attempted_crossing] -=2


    return positions


def absorbing_survivors(boundary, N, M, rng):

    final_positions = []

    # keep starting new trials until N walkers survived
    while len(final_positions) < N:

        #  simulate as many new walkers as are still needed
        number_new_walkers = N - len(final_positions)

        positions = np.zeros(number_new_walkers, dtype=int)
        alive = np.ones(number_new_walkers, dtype=bool)

        for step_number in range(M):

            steps = rng.choice([-1, 1], size=number_new_walkers)

            # A walker at b attempts to move to b + 1
            attempted_crossing = (alive & (positions == boundary)& (steps == 1))

            #remove walker
            alive[attempted_crossing] = False

            #only surviving walkers
            positions[alive] += steps[alive]

        
        final_positions.extend(positions[alive])

    return np.array(final_positions[:N])