class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            amari = n % 3
            if amari > 0:
                return False
            n //= 3
        return True

s = Solution()
print(s.isPowerOfThree(27))
print(s.isPowerOfThree(0))
print(s.isPowerOfThree(9))