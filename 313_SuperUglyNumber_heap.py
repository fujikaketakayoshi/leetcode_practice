import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        m = len(primes)
        # heapq.heappush(, 5)
        ugly = [1] * n
        idx = [0] * m
        hp = primes[:]
        for i in range(n):
            minv = heapq.heappop(hp)
            for p in primes:
                heapq.heappush(hp, minv * p)
            print(hp)
        return hp[0]
s = Solution()
print(s.nthSuperUglyNumber(12, [2,7,13,19])) # 32
