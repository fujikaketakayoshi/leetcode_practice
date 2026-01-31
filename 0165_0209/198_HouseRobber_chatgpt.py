class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        print(dp)
        return dp[n-1]

solution = Solution()
print(solution.rob([1,2,3,1]))  # 出力: 4
print(solution.rob([2,7,9,3,1]))  # 出力: 12
print(solution.rob([2,1,1,2]))  # 出力: 4
print(solution.rob([1,2,3]))  # 出力: 4
print(solution.rob([1,3,1,3,100]))  # 出力: 103