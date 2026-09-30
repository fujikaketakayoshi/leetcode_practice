class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)

        dp = [1] * n
        prev = [-1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        print(dp, prev)
        idx = max(range(n), key=lambda i: dp[i])
        print(idx)

        ans = []
        while idx != -1:
            ans.append(nums[idx])
            idx = prev[idx]

        return ans
