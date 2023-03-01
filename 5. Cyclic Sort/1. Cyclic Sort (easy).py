def cyclic_sort(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            idx = nums[i] - 1
            nums[i], nums[idx] = nums[idx], nums[i]

    return nums


def cyclic_sort_2(nums):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] != i+1:
            idx = nums[i]-1
            nums[i], nums[idx] = nums[idx], nums[i]
        else:
            i += 1

    return nums


if __name__ == "__main__":
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))
    print("=======================")
    print(cyclic_sort_2([3, 1, 5, 4, 2]))
    print(cyclic_sort_2([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort_2([1, 5, 6, 4, 3, 2]))
