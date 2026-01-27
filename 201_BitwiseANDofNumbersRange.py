class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            i += 1
        
        return left << i

solution = Solution()
print(solution.rangeBitwiseAnd(5, 7))  # 出力: 4
print(solution.rangeBitwiseAnd(0, 1))  # 出力: 0
print(solution.rangeBitwiseAnd(1, 2147483647))  # 出力
print(solution.rangeBitwiseAnd(600000000, 2147483647))  # 出力: 0
print(solution.rangeBitwiseAnd(5, 6))  # 出力: 4