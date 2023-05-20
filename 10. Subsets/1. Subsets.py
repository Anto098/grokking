def find_subsets(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            s_c = subsets[i].copy()
            s_c.append(num)
            subsets.append(s_c)

    return subsets


if __name__ == "__main__":
    print(f"Here is the list of subsets {find_subsets([1, 3])}")
    print(f"Here is the list of subsets {find_subsets([1, 5, 3])}")
