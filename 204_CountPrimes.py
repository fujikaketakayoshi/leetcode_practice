class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1): 
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    print(i, j)
                    is_prime[j] = False

        return len([i for i in range(2, n + 1) if is_prime[i]])

solution = Solution()
print(solution.countPrimes(10))  # 出力: 4
print(solution.countPrimes(0))  # 出力: 0
print(solution.countPrimes(1))  # 出力: 0
print(solution.countPrimes(2))  # 出力: 1
print(solution.countPrimes(3))  # 出力: 2
print(solution.countPrimes(100))  # 出力: 25
print(solution.countPrimes(150))  # 出力: 35
