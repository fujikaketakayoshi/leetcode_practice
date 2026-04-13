class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
print(s.lengthOfLIS([0,1,0,3,2,3]))  # Output: 4
print(s.lengthOfLIS([7,7,7,7,7,7,7]))  # Output: 1
