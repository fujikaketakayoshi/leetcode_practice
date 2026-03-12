class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

solution = Solution()
print(solution.isPowerOfTwo(1))  # True
print(solution.isPowerOfTwo(16)) # True
print(solution.isPowerOfTwo(3))  # False
