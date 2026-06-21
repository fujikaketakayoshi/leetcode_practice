import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:

        heap = [1]
        visited = {1}

        for _ in range(n):
            x = heapq.heappop(heap)

            for p in primes:
                nxt = x * p

                if nxt not in visited:
                    visited.add(nxt)
                    heapq.heappush(heap, nxt)

        return x

s = Solution()
print(s.nthSuperUglyNumber(12, [2,7,13,19])) # 32
