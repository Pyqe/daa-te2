import random

def gen_rand_array(sz, lo, hi):
    arr = []
    for i in range(sz):
        arr.append(random.randint(lo, hi))
    return arr

def gen_non_decreasing_array(sz, lo, hi):
    arr = gen_rand_array(sz, lo, hi)
    arr.sort()
    return arr

def gen_increasing_array(sz, lo, hi):
    arr = gen_non_decreasing_array(sz, lo, hi)
    for i in range(sz):
        arr[i] += i
    return arr

def gen_rand_test(sz):
    universe = list(range(1, sz + 1))
    subsets = []
    for i in range(sz):
        cur_sz = random.randint(1, sz)
        subsets.append(gen_increasing_array(cur_sz, 1, sz))
    costs = gen_rand_array(sz, 1, 2 ** 32)
    return universe, subsets, costs