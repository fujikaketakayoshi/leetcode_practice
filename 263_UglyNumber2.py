class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return True if n == 1 else False

s = Solution()
print(s.isUgly(6))  # True
print(s.isUgly(8))  # True
print(s.isUgly(14)) # False
