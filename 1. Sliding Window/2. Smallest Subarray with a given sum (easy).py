import math


def smallest_subarray_with_given_sum(s, arr):
    _min = math.inf
    p1, p2 = 0, 0
    _sum = 0
    n = len(arr)
    while p1 <= p2 and p2 < n:
        _sum += arr[p2]
        while _sum >= s:
            _min = min((p2 - p1) + 1, _min)
            _sum -= arr[p1]
            p1 += 1

        p2 += 1

    return _min


if __name__ == "__main__":
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
    print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))
    print(smallest_subarray_with_given_sum(8, [1, 1, 1]))
