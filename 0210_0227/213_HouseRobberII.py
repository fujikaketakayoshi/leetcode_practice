class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob(nums):
            print(nums)
            n = len(nums)
            dp = [0] * (n + 1)
            for i in range(1, n + 1):
                if i >= 2:
                    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
                else:
                    dp[i] = max(dp[i - 1], nums[i - 1])
            return max(dp)
        
        if len(nums) == 1:
            return nums[0]
        return max(rob(nums[1:]), rob(nums[:-1]))

solution = Solution()
print(solution.rob([2,3,2]))
print(solution.rob([1,2,3,1]))
print(solution.rob([1,2,3]))
print(solution.rob([200,3,140,20,10]))
print(solution.rob([1,3,1,3,100]))
