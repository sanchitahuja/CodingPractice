

def egg_drop(floors, eggs):
    dp = [[0 for _ in range(floors+1)] for _ in range(eggs+1)]

    for egg in range(1, eggs+1):
        for floor in range(1, floors+1):
            if egg == 1:
                dp[egg][floor] = floor
            elif floor == 1:
                dp[egg][floor] = 1
            else:
                cur = floor-1
                prev = 0
                min_val = float('inf')
                while cur >= 0:
                    max_val = max(dp[egg][cur], dp[egg-1][prev])
                    prev += 1
                    cur -= 1
                    min_val = min(min_val, max_val)

                dp[egg][floor] = min_val + 1

    return dp[eggs][floors]


print(egg_drop(floors=7,eggs =3))

