class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n + 1):
            b = bin(i)
            ans.append(b.count('1'))
        return ans