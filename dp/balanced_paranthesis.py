
def balanced_paranthesis(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        j = i-1
        k = 0
        val = 0
        while j >= 0:
            val += dp[j]*dp[k]
            j -= 1
            k += 1
        dp[i] = val

    return dp[n]


print(balanced_paranthesis(3))