class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break

        return h

s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))
print(s.hIndex([1, 3, 1]))
