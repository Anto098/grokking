def can_partition(nums):
    s = sum(nums)
    half_s = int(s/2)
    n = len(nums)
    if s % 2 != 0:
        return False

    dp = [[False for _ in range(half_s + 1)] for _ in range(n)]
    dp[0][1] = True  # special case
    for i in range(n):
        dp[i][0] = True
        if i >= 2:
            dp[0][i] = False

    for i in range(1, n):
        for _s in range(1, half_s + 1):
            if dp[i - 1][_s] == True:
                dp[i][_s] = True
            else:
                dp[i][_s] = dp[i - 1][_s - nums[i]] if nums[i] <= half_s else False

    return dp[-1][-1]


if __name__ == "__main__":
    print(can_partition([1, 2, 3, 4]))
    print(can_partition([1, 1, 3, 4, 7]))
    print(can_partition([2, 3, 4, 6]))
