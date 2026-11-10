import numpy as np
import matplotlib.pyplot as plt
from random_walks import  boundary, absorbing_survivors,absorbing_stopped, cliff_no_return, tunneling_wall
import argparse
from pathlib import Path

#seed
parser = argparse.ArgumentParser()

parser.add_argument(
    '--seed',
    type=int,
    default=44,
    help='Random-number-generator seed'
)

args = parser.parse_args()

M = 1000
N = 10_000
#case A, B1 and C
#list with boundarys 
boundarys = [5, 20, 50]


rng = np.random.default_rng(args.seed)

print('Using seed:', args.seed)
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

plt.savefig(
    'case_A_reflecting.png',
    dpi=300,
    bbox_inches='tight'
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
plt.savefig(
    'case_B1_absorbing.png',
    dpi=300,
    bbox_inches='tight'
)
plt.xlabel('Final position x')
plt.ylabel('Probability density')
plt.title('Case B1: Absorbing Boundaries, Survivors Only')
plt.grid()
plt.legend()
plt.show()

#B2# 
#boundary at 20
x_20_stopped, absorbed_fraction = absorbing_stopped(20, N, M, rng)

print('Case B2 absorbed fraction:', absorbed_fraction)
# same integer-centered bins for B1 and B2
all_positions_B2 = np.concatenate((
    x_20_survivors,
    x_20_stopped
))

bins_B2 = np.arange(
    np.min(all_positions_B2) - 0.5,
    np.max(all_positions_B2) + 1.5,
    1
)

plt.figure()

plt.hist(
    x_20_survivors,
    bins=bins_B2,
    density=True,
    histtype='step',
    label='B1: survivors only'
)

plt.hist(
    x_20_stopped,
    bins=bins_B2,
    density=True,
    histtype='step',
    label='B2: stopped walkers included'
)

plt.savefig(
    'case_B2_comparison.png',
    dpi=300,
    bbox_inches='tight'
)

plt.xlabel('Recorded final position x')
plt.ylabel('Probability density')
plt.title('Absorbing Boundary at x = 20: B1 vs. B2')
plt.grid()
plt.legend()
plt.show()

#C
# Case C: cliff with no return
x_5_cliff = cliff_no_return(5, N, M, rng)
x_20_cliff = cliff_no_return(20, N, M, rng)
x_50_cliff = cliff_no_return(50, N, M, rng)

#separate unbiased for case C
unbiased_steps_C = rng.choice([-1, 1], size=(N, M))
x_unbiased_C = np.sum(unbiased_steps_C, axis=1)

all_positions_C = np.concatenate((
    x_unbiased_C,
    x_5_cliff,
    x_20_cliff,
    x_50_cliff
))

bins_C = np.arange(
    np.min(all_positions_C) - 0.5,
    np.max(all_positions_C) + 1.5,
    1
)

#plot
plt.figure()

plt.hist(x_unbiased_C, bins=bins_C, density=True,
         histtype='step', label='Unbiased')

plt.hist(x_5_cliff, bins=bins_C, density=True,
         histtype='step', label='Cliff at x = 5')

plt.hist(x_20_cliff, bins=bins_C, density=True,
         histtype='step', label='Cliff at x = 20')

plt.hist(x_50_cliff, bins=bins_C, density=True,
         histtype='step', label='Cliff at x = 50')

plt.savefig(
    'case_C_cliff.png',
    dpi=300,
    bbox_inches='tight'
)
plt.xlabel('Final position x')
plt.ylabel('Probability density')
plt.title('Case C: Cliff with No Return')
plt.grid()
plt.legend()
plt.show()

# part D
p_values = [0.0, 0.1, 0.5, 1.0]

tunneling_positions = []

#schleife aufrufe
for p in p_values:

    final_positions = tunneling_wall(boundary=5,N=N,M=M,p=p,rng=rng)
    tunneling_positions.append(final_positions)

all_positions_D = np.concatenate(tunneling_positions)


bins_D = np.arange(
    np.min(all_positions_D) - 0.5,
    np.max(all_positions_D) + 1.5,
    1
)


#plot
plt.figure()
for p, final_positions in zip(p_values, tunneling_positions):

    plt.hist(
        final_positions,
        bins=bins_D,
        density=True,
        histtype='step',
        label=f'p = {p}'
    )
plt.savefig(
    'case_D_tunneling.png',
    dpi=300,
    bbox_inches='tight'
)
plt.xlabel('Final position x')
plt.ylabel('Probability density')
plt.title('Case D: Tunneling Through a Wall at x = 5')
plt.grid()
plt.legend()
plt.show()

#contoroll of the values : 

# unbiased 
unbiased_steps_D = rng.choice([-1, 1], size=(N, M))
x_unbiased_D = np.sum(unbiased_steps_D, axis=1)

#tests
print()
print('Case D limit checks')

print('Reflecting wall x = 5:')
print('mean:', np.mean(x_5))
print('standard deviation:', np.std(x_5))

print('Tunneling p = 0:')
print('mean:', np.mean(tunneling_positions[0]))
print('standard deviation:', np.std(tunneling_positions[0]))

print('Unbiased walk:')
print('mean:', np.mean(x_unbiased_D))
print('standard deviation:', np.std(x_unbiased_D))

print('Tunneling p = 1:')
print('mean:', np.mean(tunneling_positions[-1]))
print('standard deviation:', np.std(tunneling_positions[-1]))