def find_subsets(nums):
    subsets = [[]]
    prev = []
    l = None
    for i in range(len(nums)):
        temp = []

        if i > 0 and nums[i] == nums[i - 1]:
            l = prev
        else:
            l = subsets
            prev = []

        for s in l:
            s_c = s.copy()
            s_c.append(nums[i])
            temp.append(s_c)

        prev = temp
        subsets.extend(temp)

    return subsets


if __name__ == "__main__":
    print(f"Here is the list of subsets {find_subsets([1, 3, 3])}")
    print(f"Here is the list of subsets {find_subsets([1, 5, 3, 3])}")
