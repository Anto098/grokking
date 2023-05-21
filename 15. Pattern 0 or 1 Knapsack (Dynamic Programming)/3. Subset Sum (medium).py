def can_partition(nums, target):
    s = sum(nums)
    n = len(nums)
    if target > s:
        return False

    dp = [[False for _ in range(target + 1)] for _ in range(n)]
    dp[0][1] = True
    for i in range(n):
        dp[i][0] = True
        if i > 2:
            dp[0][i] = True if nums[0] == i else False

    for i in range(1, n):
        for t in range(1, target+1):
            if dp[i-1][t] == True:
                dp[i][t] = True
            else:
                dp[i][t] = dp[i-1][t-nums[i]] if t >= nums[i] else False

    return dp[-1][-1]


if __name__ == "__main__":
    print(can_partition([1, 2, 3, 7], 6))
    print(can_partition([1, 2, 7, 1, 5], 10))
    print(can_partition([1, 3, 4, 8], 6))
