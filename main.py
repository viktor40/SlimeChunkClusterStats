"""
The MIT License (MIT)

Copyright (c) 2020 Viktor40

The source code can be found at:
https://github.com/viktor40/SlimeChunkClusterStats

This program calculate the statistical probability of finding a slime cluster of a given size within a world.
It also calculates to probability of finding one in any seed. If the probability is bigger than 1 it means you're
expecting to find more than 1 of that size of cluster.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from matplotlib import rcParams


"""----Constants----"""
n = 200
p = 0.1

"""----Config----"""
rcParams.update({'font.size': 11, 'interactive': False})
WORLD = True
SEED = True


def main():
    number_of_chunks = np.arange(200, dtype=int)
    world_probability = binom.pmf(number_of_chunks, n, p) * ((29999984 * (2/16)) ** 2)
    np.append(world_probability, [200, (1 / 10) ** 200 * (29999984 * (2 / 16)) ** 2]), np.append(number_of_chunks, [200])
    data_world = np.array([number_of_chunks, world_probability]).T
    np.savetxt('world_probability.txt', data_world, fmt=['%d', '%e'])

    if WORLD:
        print('---World---')
        print('n', 'P(x)')
        for i, j in data_world:
            print(int(i), j)

        plt.plot(number_of_chunks, world_probability)
        plt.yscale('log')
        plt.title('amount of slime chunks clusters per amount of slime chunks \n on avg in a given world')
        plt.xlabel('number of chunks in cluster'), plt.ylabel('amount on avg in world')
        plt.savefig('slime_clusters.png')
        plt.show()

    if SEED:
        number_of_seeds = 18446744073709551616
        seed_probability = world_probability * number_of_seeds
        data_seed = np.array([number_of_chunks, seed_probability]).T
        np.savetxt('seed_probability.txt', data_seed, fmt=['%d', '%e'])

        print('---Seed---')
        print('n', 'P(x)')
        for i, j in data_seed:
            print(int(i), j)


if __name__ == '__main__':
    main()
