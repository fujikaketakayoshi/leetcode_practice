class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        m = len(primes)

        ugly = [1] * n
        idx = [0] * m
        cand = primes[:]

        for i in range(1, n):
            nxt = min(cand)
            ugly[i] = nxt

            for j in range(m):
                if cand[j] == nxt:
                    idx[j] += 1
                    cand[j] = ugly[idx[j]] * primes[j]
            print(cand)
        return ugly[-1]

s = Solution()
print(s.nthSuperUglyNumber(12, [2,7,13,19])) # 32
