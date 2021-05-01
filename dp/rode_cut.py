def find_max_amount(cost):
    new_cost = [0] + cost
    dp = [0] * len(new_cost)
    for i in range(2, len(dp)):
        dp[i] = new_cost[i]
        l = 1
        r = i - 1
        while r >= l:
            dp[i] = max(dp[i], dp[l] + dp[r])
            r -= 1
            l += 1

    return dp[-1]


arr = [1, 5, 8, 9, 10, 17, 17, 20]
print(find_max_amount(arr))