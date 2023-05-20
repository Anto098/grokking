def memoization_solve_knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights))]
    return recursive_solve_knapsack(dp, profits, weights, capacity, index=0)


def recursive_solve_knapsack(dp, profits, weights, capacity, index):
    if index == len(profits) or capacity <= 0:
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    profits1 = 0
    if weights[index] <= capacity:
        profits1 = profits[index] + recursive_solve_knapsack(dp, profits, weights, capacity - weights[index], index + 1)

    profits2 = recursive_solve_knapsack(dp, profits, weights, capacity, index + 1)

    dp[index][capacity] = max(profits1, profits2)
    return dp[index][capacity]


def bottom_up_solve_knapsack(p, w, c):
    # p = profits
    # w = weights
    # c = capacity
    dp = [[0 for _ in range(c + 1)] for _ in range(len(w))]
    for i in range(len(w)):
        dp[i][0] = 0
    for c in range(c + 1):
        dp[0][c] = p[0] if w[0] <= c else 0

    for i in range(1, len(w)):
        for c in range(1, c + 1):
            new_p = p[i] + dp[i - 1][c - w[i]] if c - w[i] >= 0 else 0
            dp[i][c] = max(dp[i - 1][c], new_p)

    print_selected_elements(p, w, c, dp)

    return dp[-1][-1]


def print_selected_elements(p, w, capacity, dp):
    i = len(w) - 1
    c = capacity
    elem = dp[-1][-1]
    selected_elems = set()
    while elem != 0:
        if i > 0 and dp[i - 1][c] == elem:
            i -= 1
            continue
        else:
            elem -= p[i]
            c -= w[i]
            selected_elems.add(p[i])

    print(selected_elems)


if __name__ == "__main__":
    # print(memoization_solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    # print(memoization_solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

    print(bottom_up_solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(bottom_up_solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
