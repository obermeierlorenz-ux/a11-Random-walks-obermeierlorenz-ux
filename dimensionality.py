import numpy as np
import matplotlib.pyplot as plt
from random_walks import random_walks , two_dimensional_walks, three_dimensional_walks

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

expected_sigma = np.sqrt(M_values)

plt.plot(
    M_values,
    expected_sigma,
    color='black',
    linestyle='--',
    label=r'Expected $\sqrt{M}$'
)

plt.xlabel('Number of steps M')
plt.ylabel(r'Standard deviation $\sigma$')
plt.title('Standard Deviation of Final Positions')
plt.grid()
plt.legend()

plt.show()

#Part 2 higher dimensions
M_hd = 1000

# #2D walk'
N = 10_000
M = 1_000

final_positions = []
for tiral in range(N):
    final_postion = two_dimensional_walks(M, rng)
    final_positions.append(final_postion)

final_positions = np.array(final_positions)

x_final = final_positions[:, 0]
y_final = final_positions[:, 1]

r_final = np.sqrt(x_final**2 + y_final**2)

#plots
x_final = final_positions[:, 0]
y_final = final_positions[:, 1]
plt.figure()

plt.hist2d(
    x_final,
    y_final,
    bins=50,
    cmap='viridis'
)

plt.xlabel('Final x position')
plt.ylabel('Final y position')
plt.title('2D Random-Walk Final Position Density')
plt.colorbar(label='Count')
plt.gca().set_aspect('equal')

plt.tight_layout()
plt.show()
#Histogram of final x values
plt.figure()

plt.hist(
    x_final,
    bins=50,
    density=True,
    alpha=0.7
)

plt.xlabel('Final x position')
plt.ylabel('Probability density')
plt.title('Distribution of Final x Values')
plt.grid()

plt.tight_layout()
plt.show()

# # Histogram of final y values
plt.figure()

plt.hist(
    y_final,
    bins=50,
    density=True,
    alpha=0.7
)

plt.xlabel('Final y position')
plt.ylabel('Probability density')
plt.title('Distribution of Final y Values')
plt.grid()

plt.tight_layout()
plt.show()

# Histogram of final distance from the origin
plt.figure()

plt.hist(
    r_final,
    bins=50,
    density=True,
    alpha=0.7
)

plt.xlabel('Final distance r')
plt.ylabel('Probability density')
plt.title('Distribution of Final Distance from Origin 2D')
plt.grid()

plt.tight_layout()
plt.show()

#3D walks

N = 10_000
M = 1_000

final_positions_3d = []

for tiral in range(N):
    final_postion_3d = three_dimensional_walks(M, rng)
    final_positions_3d.append(final_postion_3d)

final_positions_3d = np.array(final_positions_3d)

#plots
x_3d_final = final_positions_3d[:, 0]
y_3d_final = final_positions_3d[:, 1]
z_3d_final = final_positions_3d[:, 2]


r_3d_final = np.sqrt(x_3d_final**2 + y_3d_final**2 + z_3d_final**2)

plt.figure()

plt.hist2d(
    x_3d_final,
    y_3d_final,
    bins=50,
    cmap='viridis'
)

plt.xlabel('Final x position')
plt.ylabel('Final y position')
plt.title('3D Random Walk: Final x-y Projection')
plt.colorbar(label='Count')
plt.gca().set_aspect('equal')

plt.tight_layout()
plt.show()
# Histogram of final x values
plt.figure()

plt.hist(
    x_3d_final,
    bins=50,
    density=True,
    alpha=0.7
)

plt.xlabel('Final x position')
plt.ylabel('Probability density')
plt.title('Distribution of Final x Values')
plt.grid()

plt.tight_layout()
plt.show()

# Histogram of final y values
plt.figure()

plt.hist(
    y_3d_final,
    bins=50,
    density=True,
    alpha=0.7
)

plt.xlabel('Final y position')
plt.ylabel('Probability density')
plt.title('Distribution of Final y Values')
plt.grid()

plt.tight_layout()
plt.show()

#z histogram
plt.figure()
plt.hist(
    z_3d_final,
    bins=50,
    density=True,
    alpha=0.7
)

plt.xlabel('Final z position')
plt.ylabel('Probability density')
plt.title('Distribution of Final z Values')
plt.grid()

plt.tight_layout()
plt.show()

# Histogram of final distance from the origin
plt.figure()

plt.hist(
    r_3d_final,
    bins=50,
    density=True,
    alpha=0.7
)

plt.xlabel('Final distance r')
plt.ylabel('Probability density')
plt.title('Distribution of Final Distance from Origin 3D')
plt.grid()

plt.tight_layout()
plt.show()


# 1D, 2D, and 3D comparison

# Same number of independent trials for every dimension
# Use 1000 first because the 2D and 3D functions use Python loops
N_trend = 1000

sigma_1d = []
sigma_2d = []
sigma_3d = []

mean_r_1d = []
mean_r_2d = []
mean_r_3d = []


#for 1D
simulations_1d = random_walks(N_trend, M_values, rng)

for final_positions_1d in simulations_1d:

    sigma_1d.append(np.std(final_positions_1d))
    mean_r_1d.append(np.mean(np.abs(final_positions_1d)))


#2d and 3D
for M in M_values:

    positions_2d = []
    positions_3d = []

    for trial in range(N_trend):

        final_position_2d = two_dimensional_walks(M, rng)
        final_position_3d = three_dimensional_walks(M, rng)

        positions_2d.append(final_position_2d)
        positions_3d.append(final_position_3d)

    positions_2d = np.array(positions_2d)
    positions_3d = np.array(positions_3d)

    sigma_2d.append(np.std(positions_2d[:, 0]))
    sigma_3d.append(np.std(positions_3d[:, 0]))

    r_2d = np.linalg.norm(positions_2d, axis=1)
    r_3d = np.linalg.norm(positions_3d, axis=1)

    mean_r_2d.append(np.mean(r_2d))
    mean_r_3d.append(np.mean(r_3d))


# Plot 1
#  standard deviation of x versus M
plt.figure()

plt.plot(M_values, sigma_1d, marker='o', label='1D')
plt.plot(M_values, sigma_2d, marker='o', label='2D')
plt.plot(M_values, sigma_3d, marker='o', label='3D')

plt.xlabel('Number of steps M')
plt.ylabel(r'Standard deviation of x, $\sigma_x$')
plt.title('Coordinate Spread for 1D, 2D, and 3D Random Walks')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()


#  mean distance from origin versus M
plt.figure()

plt.plot(M_values, mean_r_1d, marker='o', label='1D')
plt.plot(M_values, mean_r_2d, marker='o', label='2D')
plt.plot(M_values, mean_r_3d, marker='o', label='3D')

plt.xlabel('Number of steps M')
plt.ylabel(r'Mean distance from origin $\langle r \rangle$')
plt.title('Mean Distance from Origin for 1D, 2D, and 3D Random Walks')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
