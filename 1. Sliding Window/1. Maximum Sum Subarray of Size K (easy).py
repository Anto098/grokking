def max_sub_array_of_size_k(k, arr):
    _sum = 0
    _max = -1
    for i in range(len(arr)):
        _sum += arr[i]
        if i >= k:
            _sum -= arr[i - k]
            _max = max(_max, _sum)

    return _max


if __name__ == "__main__":
    print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
