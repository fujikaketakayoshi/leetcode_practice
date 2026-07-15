class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        n = len(nums)
        dp = [0] * n
        ans = []
        for i in range(n):
            dp[i] = nums[i]
            if lower <= nums[i] <= upper:
                ans.append(nums[i])
            for j in range(i):
                dp[j] += nums[i]
                if lower <= dp[j] <= upper:
                    ans.append(dp[j])
            # print(dp)
        
        return len(ans)