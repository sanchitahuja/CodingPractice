class Solution:
    MAX = (5 * 10 ** 6)
    sieve = [1] * (MAX + 1)

    i = 2
    while i * i <= MAX:

        if sieve[i] == 1:
            j = i * i
            while j <= MAX:
                sieve[j] = 0
                j += i

        i += 1

    sieve[0] = 0
    sieve[1] = 0

    for i in range(1, MAX + 1):
        sieve[i] += sieve[i - 1]

    def countPrimes(self, n: int) -> int:
        if n > 1:
            return self.sieve[n - 1]
        else:
            return 0


print(Solution().countPrimes(3))
