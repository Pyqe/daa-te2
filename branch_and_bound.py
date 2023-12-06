def bypass_branch(subset, i):
    for j in range(i - 1, -1, -1):
        if subset[j] == 0:
            subset[j] = 1
            return subset, j + 1

    return subset, 0

def next_vertex(subset, i, m):
    if i < m:
        subset[i] = 0
        return subset, i + 1
    else:
        for j in range(m - 1, -1, -1):
            if subset[j] == 0:
                subset[j] = 1
                return subset, j + 1
                
    return subset, 0

def set_cover_branch_and_bound(universe,sets,costs):
    subset = [1] * len(sets)
    subset[0] = 0
    bestCost = sum(costs)
    bestSubset = []
    i = 1

    while i > 0:

        if i < len(sets):
            cost, tSet = 0, set()
            for k in range(i):
                cost += subset[k] * costs[k]
                if subset[k] == 1:
                    tSet.update(set(sets[k]))

            if cost > bestCost:
                subset, i = bypass_branch(subset, i)
                continue
            for k in range(i, len(sets)):
                tSet.update(set(sets[k]))
            if tSet != universe:
                subset, i = bypass_branch(subset, i)
            else:
                subset, i = next_vertex(subset, i, len(sets))
                
        else:
            cost, fSet = 0, set()
            for k in range(i):
                cost += subset[k] * costs[k]
                if subset[k] == 1:
                    fSet.update(set(sets[k]))

            if cost < bestCost and fSet == universe:
                bestCost = cost
                bestSubset = subset[:]
            subset, i = next_vertex(subset, i , len(sets))

    return bestCost, bestSubset

if __name__ == "__main__":
    universe = list(range(1, 10))
    sets = [
        [1, 5, 6, 7],
        [2, 6, 8, 9],
        [1, 2, 4, 7, 9],
        [3, 4, 6],
        [3, 5, 6, 8],
        [1, 3, 4, 7, 8],
    ]
    costs = [14, 13, 17, 9, 12, 18]
    print(set_cover_branch_and_bound(universe, sets, costs))

    universe = list(range(1, 4))
    sets = [
        [1, 2],
        [1],
        [2, 3],
    ]
    costs = [5, 4, 6]
    print(set_cover_branch_and_bound(universe, sets, costs))

    universe = list(range(1, 5))
    sets = [
        [1, 2, 4],
        [2, 4, 5],
        [1, 5],
    ]
    costs = [9, 8, 6]
    print(set_cover_branch_and_bound(universe, sets, costs))

if __name__ == "__main__":
    universe = list(range(1, 10))
    sets = [
        [1, 5, 6, 7],
        [2, 6, 8, 9],
        [1, 2, 4, 7, 9],
        [3, 4, 6],
        [3, 5, 6, 8],
        [1, 3, 4, 7, 8],
    ]
    costs = [14, 13, 17, 9, 12, 18]
    print(BB(universe, sets, costs))

    universe = list(range(1, 4))
    sets = [
        [1, 2],
        [1],
        [2, 3],
    ]
    costs = [5, 4, 6]
    print(BB(universe, sets, costs))

    universe = list(range(1, 5))
    sets = [
        [1, 2, 4],
        [2, 4, 5],
        [1, 5],
    ]
    costs = [9, 8, 6]
    print(BB(universe, sets, costs))