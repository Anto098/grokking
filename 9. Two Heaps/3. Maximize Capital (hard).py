from heapq import *


def find_maximum_capital(capital, profits, nb_of_projects, initial_capital):
    min_heap = []
    max_heap = []
    current_capital = initial_capital

    for i in range(len(capital)):
        heappush(min_heap, (capital[i], profits[i], i))

    for i in range(nb_of_projects):
        while min_heap and min_heap[0][0] <= current_capital:
            _, p, j = heappop(min_heap)
            heappush(max_heap, (-p, j))

        if len(max_heap) == 0:
            break

        current_capital += -heappop(max_heap)[0]

    return current_capital


if __name__ == "__main__":
    print(f"Maximum capital: {find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)}")
    print(f"Maximum capital: {find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)}")
