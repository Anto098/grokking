def triplet_with_smaller_sum(l, target):
    nb_triplets = 0
    len_l = len(l)
    for i in range(len_l - 1):
        if i > 0 and l[i] == l[i - 1]:
            continue

        start = i + 1
        end = len_l - 1
        while start < end:
            curr_sum = l[i] + l[start] + l[end]
            if curr_sum < target:
                nb_triplets += end - start
                start += 1
            else:
                end -= 1

    return nb_triplets


def sol_triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += search_pair(arr, target - arr[i], i)
    return count


def search_pair(arr, target_sum, first):
    count = 0
    left, right = first + 1, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    return count


if __name__ == "__main__":
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
