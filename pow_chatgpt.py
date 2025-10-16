class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(x, n):
            if n == 0:
                return 1.0
            half = fast_pow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)

solution = Solution()
print(solution.myPow(2.00000, 10))
print(solution.myPow(2.10000, 3))
print(solution.myPow(2.00000, -2))
print(solution.myPow(2.00000, 0))
print(solution.myPow(2.00000, -2147483648))
print(solution.myPow(1.00000, -2147483648))
print(solution.myPow(0.44528, 0))