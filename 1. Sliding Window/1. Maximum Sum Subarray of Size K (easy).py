def max_sub_array_of_size_k(k, arr):
    _max = -1
    _sum = 0
    start_idx = 0
    for end in range(len(arr)):
        _sum += arr[end]
        if end >= k - 1:
            if _sum > _max:
                _max = _sum
            _sum -= arr[start_idx]
            start_idx += 1

    return _max


if __name__ == "__main__":
    print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
