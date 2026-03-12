class Solution:
    def isPowerOfTwo(self, n: int) -> bool:        
        if n < 0:
            return False
        x = 0
        while True:
            num = 2 ** x
            if num == n:
                return True
            elif num > n:
                return False
            x += 1

solution = Solution()
print(solution.isPowerOfTwo(1))  # True
print(solution.isPowerOfTwo(16)) # True
print(solution.isPowerOfTwo(3))  # False
