class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        
        if n == 0:
            return 1.0
        elif n < 0:
            x = 1 / x
            n = -n
        
        for _ in range(n):
            res *= x
        return res

solution = Solution()
print(solution.myPow(2.00000, 10))
print(solution.myPow(2.10000, 3))
print(solution.myPow(2.00000, -2))
print(solution.myPow(2.00000, 0))
print(solution.myPow(2.00000, -2147483648))
print(solution.myPow(1.00000, -2147483648))
print(solution.myPow(0.44528, 0))