def find_all_duplicates(nums):
    i, n = 0, len(nums)
    dup_nums = []
    while i < n:
        j = nums[i] - 1
        if nums[i] != i + 1:
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                dup_nums.append(nums[i])
                i += 1
        else:
            i += 1

    return dup_nums


if __name__ == "__main__":
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
