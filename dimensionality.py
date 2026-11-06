import numpy as np
import matplotlib.pyplot as plt
from random_walks import random_walks , two_dimensional_walks

#initial conditions

N = 10_000
M_values = [100, 1000, 4000, 7000, 10000]

rng = np.random.default_rng(44)

simulations = random_walks(N, M_values, rng)

for M, final_positions in zip(M_values, simulations):

    plt.figure()
    plt.hist(
        final_positions,
        bins=50,
        density=True,
        alpha=0.7
    )
    plt.hist(final_positions, bins=50, density=True)
    plt.xlabel('Final position x')
    plt.ylabel('Probability density')
    plt.title(f'Random-walk final positions for M = {M}')
    plt.grid()

    plt.show()


#calculate and print sigma
sigma_values = []

for final_positions in simulations:

    sigma = np.std(final_positions)

    sigma_values.append(sigma)

plt.figure()

plt.plot(M_values,sigma_values,marker='o',label=r'Measured standard deviation $\sigma$')

plt.axhline(np.sqrt(N),color='black',linestyle='--',label=r'Expected value $\sqrt{N}$')

plt.xlabel('Number of walks M')
plt.ylabel(r'Standard deviation $\sigma$')
plt.title('Standard Deviation of Final Positions')
plt.grid()
plt.legend()

plt.show()

#Part 2 higher dimensions
M_hd = 1000

#2D walk
N = 10_000
M = 1_000

final_positions = []

for tiral in range(N):
    final_postion = two_dimensional_walks(M, rng)
    final_positions.append(final_postion)

final_positions = np.array(final_positions)

#plots
y = 0.7 * final_positions + np.random.normal(size = 5000)

plt.hist2d(final_positions, y, bins = 40)
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Count')
plt.show()