class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1] * n
        lp = len(primes)
        primes_cnt = [0] * lp
        
        for i in range(1, n):
            next = [0] * lp
            for j, p in enumerate(primes):
                next[j] = ugly[primes_cnt[j]] * p
            # print(next)
            nxt = min(next)
            ugly[i] = nxt

            for j, n in enumerate(next):
                if nxt == n:
                    next[j] += 1
                    primes_cnt[j] += 1
            
        return ugly[-1]

s = Solution()
print(s.nthSuperUglyNumber(12, [2,7,13,19])) # 32
