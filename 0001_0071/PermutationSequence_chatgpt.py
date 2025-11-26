import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        k -= 1  # 0-indexにする（計算が楽）
        res = ""

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            res += str(nums.pop(index))
            k %= fact

        return res

solution = Solution()
print(solution.getPermutation(3, 3))  # Output: "213"
print(solution.getPermutation(4, 9))  # Output: "2314"
print(solution.getPermutation(3, 1))  # Output: "123"
print(solution.getPermutation(3, 6))  # Output: "321"
print(solution.getPermutation(1, 1))  # Output: "1"
print(solution.getPermutation(4, 1))  # Output: "1234"
print(solution.getPermutation(4, 24))  # Output: "4321"
print(solution.getPermutation(5, 16))  # Output: "25314"
print(solution.getPermutation(5, 1))  # Output: "12345"
print(solution.getPermutation(5, 120))  # Output: "54321"
print(solution.getPermutation(6, 400))  # Output: "154326"
print(solution.getPermutation(6, 1))  # Output: "123456"
print(solution.getPermutation(6, 720))  # Output: "654321"
print(solution.getPermutation(7, 1000))  # Output: "1234756"
print(solution.getPermutation(7, 1))  # Output: "1234567"
print(solution.getPermutation(7, 5040))  # Output: "7654321"
print(solution.getPermutation(8, 20000))  # Output: "12348765"
print(solution.getPermutation(8, 1))  # Output: "12345678"
print(solution.getPermutation(8, 40320))  # Output: "87654321"
print(solution.getPermutation(9, 100000))  # Output: "123496875"
print(solution.getPermutation(9, 1))  # Output: "123456789"
print(solution.getPermutation(9, 362880))  # Output: "987654321