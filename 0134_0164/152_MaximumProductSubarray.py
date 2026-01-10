class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        ans = max(nums)

        for i in range(0, n):
            now = nums[i]
            for j in range(i + 1, n):
                now *= nums[j]
                ans = max(ans, now)

        return ans

solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))  # Output: 6
print(solution.maxProduct([-2, 0, -1]))    # Output: 0
print(solution.maxProduct([-2, 3, -4]))    # Output: 24
