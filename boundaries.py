import numpy as np
import matplotlib.pyplot as plt
from random_walks import  boundary, absorbing_survivors

M = 1000
N = 10_000
#case A, B1 and C
#list with boundarys 
boundarys = [5, 20, 50]
rng = np.random.default_rng(44)
#for loop for every boundary 
x_5 = boundary(boundarys[0], N, M, rng)
x_20 = boundary(boundarys[1], N, M, rng)
x_50 = boundary(boundarys[2], N, M, rng)


#unbiased walk
unbiased_steps = rng.choice([-1, 1], size=(N, M))
x_unbiased = np.sum(unbiased_steps, axis=1)
#case B2 only x = 20


#case D x= 5 with transmission probability

#plot try

# Separate unbiased ensemble: no boundary



# Use identical integer-centered bins for every histogram
all_positions = np.concatenate((x_unbiased, x_5, x_20, x_50))

bins = np.arange(
    np.min(all_positions) - 0.5,
    np.max(all_positions) + 1.5,
    1
)


# Plot all four final-position distributions
plt.figure(figsize=(9, 5))

plt.hist(
    x_unbiased,
    bins=bins,
    density=True,
    histtype='step',
    linewidth=2,
    label='Unbiased'
)

plt.hist(
    x_5,
    bins=bins,
    density=True,
    histtype='step',
    linewidth=2,
    label='Reflecting wall: x = 5'
)

plt.hist(
    x_20,
    bins=bins,
    density=True,
    histtype='step',
    linewidth=2,
    label='Reflecting wall: x = 20'
)

plt.hist(
    x_50,
    bins=bins,
    density=True,
    histtype='step',
    linewidth=2,
    label='Reflecting wall: x = 50'
)

plt.xlabel('Final position x')
plt.ylabel('Probability density')
plt.title('Case A: Reflecting Walls')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()


#B1
x_5_survivors = absorbing_survivors(5, N, M, rng)
x_20_survivors = absorbing_survivors(20, N, M, rng)
x_50_survivors = absorbing_survivors(50, N, M, rng)

#plot für B1

#new unbiased
unbiased_steps_B1 = rng.choice([-1, 1], size=(N, M))
x_unbiased_B1 = np.sum(unbiased_steps_B1, axis=1)



all_positions_B1 = np.concatenate((
    x_unbiased_B1,
    x_5_survivors,
    x_20_survivors,
    x_50_survivors
))

bins_B1 = np.arange(
    np.min(all_positions_B1) - 0.5,
    np.max(all_positions_B1) + 1.5,
    1
)


plt.figure()

plt.hist(x_unbiased_B1, bins=bins_B1, density=True,
         histtype='step', label='Unbiased')

plt.hist(x_5_survivors, bins=bins_B1, density=True,
         histtype='step', label='Absorbing boundary: x = 5')

plt.hist(x_20_survivors, bins=bins_B1, density=True,
         histtype='step', label='Absorbing boundary: x = 20')

plt.hist(x_50_survivors, bins=bins_B1, density=True,
         histtype='step', label='Absorbing boundary: x = 50')

plt.xlabel('Final position x')
plt.ylabel('Probability density')
plt.title('Case B1: Absorbing Boundaries, Survivors Only')
plt.grid()
plt.legend()
plt.show()

