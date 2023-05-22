def pair_with_targetsum(arr, target_sum):
    p1, p2 = 0, len(arr) - 1
    while p2 >= p1:
        _s = arr[p1] + arr[p2]
        if _s == target_sum:
            return [p1, p2]
        elif target_sum < _s:
            p2 -= 1
        elif target_sum > _s:
            p1 += 1

    return [-1, -1]


if __name__ == "__main__":
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
