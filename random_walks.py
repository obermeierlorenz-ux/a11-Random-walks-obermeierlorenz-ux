import numpy as np


#validation check
def validate_positive_integer(value, name):

    if not isinstance(value, (int, np.integer)) or value <= 0:
        raise ValueError(f'{name} must be a positive integer.')


def validate_probability(p):

    if not 0 <= p <= 1:
        raise ValueError('p must satisfy 0 <= p <= 1.')

    
def random_walks(N, M_values, rng):

    validate_positive_integer(N, 'N')

    for M in M_values:
        validate_positive_integer(M, 'M')
    #empty lists to store the arrays of each simulation
    simulations = []


    for M in M_values:

    #create a array with M[i] zeros
        steps = rng.choice([-1, 1], size=(N, M))

        final_postion = np.sum(steps, axis=1)

        simulations.append(final_postion)


    return simulations

def two_dimensional_walks(M, rng):

    validate_positive_integer(M, 'M')

    #empty lists to store the arrays of each simulation
    postion = np.array([0.0, 0.0])

    for i in range(M):

    #random vector
        step = rng.normal(0.0, 1.0, size=2)
        step = step / np.linalg.norm(step)

        postion = postion + step


    return postion


def three_dimensional_walks(M, rng):

    validate_positive_integer(M, 'M')


    #empty lists to store the arrays of each simulation
    postion = np.array([0.0, 0.0, 0.0])

    for i in range(M):

    #random vector
        step = rng.normal(0.0, 1.0, size=3)
        step = step / np.linalg.norm(step)

        postion = postion + step


    return postion

def boundary(boundary, N, M, rng):

    validate_positive_integer(N, 'N')
    validate_positive_integer(M, 'M')

    positions = np.zeros(N, dtype=int)

    for step_number in range(M):

    #create a array with M[i] zeros
        steps = rng.choice([-1, 1], size=N)

        attempted_crossing = (positions == boundary) & (steps ==1)

        positions+= steps
        positions[attempted_crossing] -=2


    return positions


def absorbing_survivors(boundary, N, M, rng):


    validate_positive_integer(N, 'N')
    validate_positive_integer(M, 'M')

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




def absorbing_stopped(boundary, N, M, rng):


    validate_positive_integer(N, 'N')
    validate_positive_integer(M, 'M')

    positions = np.zeros(N, dtype=int)
    active = np.ones(N, dtype=bool)
    absorbed = np.zeros(N, dtype=bool)

    for step_number in range(M):

        steps = rng.choice([-1, 1], size=N)

        # active walker tries to move from b to b + 1
        attempted_crossing = (active& (positions == boundary)& (steps == 1))

        # Stop these walkers at the boundary
        absorbed[attempted_crossing] = True
        active[attempted_crossing] = False

        # Only walkers that are still active move
        positions[active] += steps[active]
    absorbed_fraction = np.mean(absorbed)


    return positions, absorbed_fraction

def cliff_no_return(boundary, N, M, rng):


    validate_positive_integer(N, 'N')
    validate_positive_integer(M, 'M')

    positions = np.zeros(N, dtype=int)

    for step_number in range(M):

        steps = rng.choice([-1,1], size=N)

        attempted_return = ((positions == boundary + 1)&(steps == -1))

        # reflect the return step  b+1 -> b becomes b+1 -> b + 2
        steps[attempted_return] = 1
        positions += steps

    return positions


def tunneling_wall(boundary, N, M, p, rng):


    validate_positive_integer(N, 'N')
    validate_positive_integer(M, 'M')
    validate_probability(p)

    positions = np.zeros(N, dtype=int)

    for step_number in range(M):

        steps = rng.choice([-1, 1], size=N)

        # crossing from left to right
        cross_left_to_right = ((positions == boundary)& (steps == 1))

        # right to left
        cross_right_to_left = ((positions == boundary + 1)& (steps == -1))

        #connects the two bool arrays
        attempted_crossing = cross_left_to_right | cross_right_to_left

        #give every attempted crossing a transmission decision
        crossing_indices = np.where(attempted_crossing)[0]
        random_values = rng.random(len(crossing_indices))

        #reflection of the  walkers that dont transmit
        reflected_indices = crossing_indices[random_values >= p]
        steps[reflected_indices] *= -1

        positions += steps

    return positions