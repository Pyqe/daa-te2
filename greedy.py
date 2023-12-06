def set_cover_greedy(universe, subsets, costs):
    present_elements = set()
    for subset in subsets:
        present_elements = present_elements | set(subset)
    if present_elements != set(universe):
        return
    
    total_cost = 0
    best_subsets = []
    cur_elements = set()
    while cur_elements != set(universe):
        best_ratio = 0.0
        best_subset = []
        best_cost = []
        for subset, cost in zip(subsets, costs):
            cnt_new = len(set(subset) - cur_elements)
            ratio = cnt_new / cost
            if ratio > best_ratio:
                best_ratio = ratio
                best_subset = subset
                best_cost = cost
        
        total_cost += best_cost
        best_subsets.append(best_subset)
        cur_elements |= set(best_subset)
    
    return total_cost, best_subsets
    
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
    print(set_cover_greedy(universe, sets, costs))

    universe = list(range(1, 4))
    sets = [
        [1, 2],
        [1],
        [2, 3],
    ]
    costs = [5, 4, 6]
    print(set_cover_greedy(universe, sets, costs))

    universe = list(range(1, 5))
    sets = [
        [1, 2, 4],
        [2, 4, 5],
        [1, 5],
    ]
    costs = [9, 8, 6]
    print(set_cover_greedy(universe, sets, costs))