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

# #2D walk'
# N = 10_000
# M = 1_000

# final_positions = []

# for tiral in range(N):
#     final_postion = two_dimensional_walks(M, rng)
#     final_positions.append(final_postion)

# final_positions = np.array(final_positions)

# x_final = final_positions[:, 0]
# y_final = final_positions[:, 1]

# r_final = np.sqrt(x_final**2 + y_final**2)

# #plots
# x_final = final_positions[:, 0]
# y_final = final_positions[:, 1]
# plt.figure()

# plt.hist2d(
#     x_final,
#     y_final,
#     bins=50,
#     cmap='viridis'
# )

# plt.xlabel('Final x position')
# plt.ylabel('Final y position')
# plt.title('2D Random-Walk Final Position Density')
# plt.colorbar(label='Count')
# plt.gca().set_aspect('equal')

# plt.tight_layout()
# plt.show()
# # Histogram of final x values
# plt.figure()

# plt.hist(
#     x_final,
#     bins=50,
#     density=True,
#     alpha=0.7
# )

# plt.xlabel('Final x position')
# plt.ylabel('Probability density')
# plt.title('Distribution of Final x Values')
# plt.grid()

# plt.tight_layout()
# plt.show()

# # Histogram of final y values
# plt.figure()

# plt.hist(
#     y_final,
#     bins=50,
#     density=True,
#     alpha=0.7
# )

# plt.xlabel('Final y position')
# plt.ylabel('Probability density')
# plt.title('Distribution of Final y Values')
# plt.grid()

# plt.tight_layout()
# plt.show()

# # Histogram of final distance from the origin
# plt.figure()

# plt.hist(
#     r_final,
#     bins=50,
#     density=True,
#     alpha=0.7
# )

# plt.xlabel('Final distance r')
# plt.ylabel('Probability density')
# plt.title('Distribution of Final Distance from Origin')
# plt.grid()

# plt.tight_layout()
# plt.show()

#3D walks

N = 10_000
M = 1_000

final_positions_3d = []

for tiral in range(N):
    final_postion_3d = three_dimensional_walks(M, rng)
    final_positions.append(final_postion_3d)

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
plt.title('Distribution of Final y Values')
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
plt.title('Distribution of Final Distance from Origin')
plt.grid()

plt.tight_layout()
plt.show()



