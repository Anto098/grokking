import math


def smallest_subarray_with_given_sum(s, arr):
    _min = math.inf
    _sum = 0
    start = 0
    for end in range(len(arr)):
        _sum += arr[end]
        while _sum >= s:
            curr_len = end - start + 1
            if curr_len < _min:
                _min = curr_len
            _sum -= arr[start]
            start += 1

    return _min if _min != math.inf else 0


if __name__ == "__main__":
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
    print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))
    print(smallest_subarray_with_given_sum(8, [1, 1, 1]))
