from test_generator import *
from greedy import *
from branch_and_bound import *

import os
import time

def compare_algs(sz):
    universe, subsets, costs = gen_rand_test(sz)
    print("-" * 32)
    print("Size", sz)

    start_time = time.time()
    set_cover_greedy(universe, subsets, costs)
    end_time = time.time()
    print("Greedy:", end_time - start_time)

    start_time = time.time()
    set_cover_branch_and_bound(universe, subsets, costs)
    end_time = time.time()
    print("Branch and Bound:", end_time - start_time)

if __name__ == "__main__":
    for sz in [20, 200, 2000]:
        compare_algs(sz)