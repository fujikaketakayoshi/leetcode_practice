class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

s = Solution()
print(s.canWinNim(4))  # False
print(s.canWinNim(1))  # True
print(s.canWinNim(2))  # True
print(s.canWinNim(3))  # True
