class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        for n in range(1, 5001):
            cnt = 0
            ok = False
            for c in citations:
                if c >= n:
                    cnt += 1
                    if cnt >= n:
                        ok = True
                        break
            if not ok:
                return n - 1

s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))
print(s.hIndex([1, 3, 1]))
