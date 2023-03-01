def pair_with_targetsum(arr, target_sum):
    start = 0
    end = len(arr) - 1
    for i in range(len(arr) - 2):
        curr_sum = arr[start] + arr[end]
        if curr_sum > target_sum:
            end -= 1
        elif curr_sum < target_sum:
            start += 1
        else:
            return [start, end]
    return [-1, -1]


if __name__ == "__main__":
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
