def find_missing_number(nums):
    for i in range(len(nums)):
        unique_nums = set()
        while nums[i] != i:
            idx = nums[i] if nums[i] < len(nums) else -1
            if nums[idx] in unique_nums:
                return i
            else:
                unique_nums.add(nums[idx])
            nums[i], nums[idx] = nums[idx], nums[i]

    return nums


def find_missing_number_2(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != i:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n


if __name__ == "__main__":
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
    print("============================")
    print(find_missing_number_2([4, 0, 3, 1]))
    print(find_missing_number_2([8, 3, 5, 2, 4, 6, 0, 1]))
