class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        # 区間長
        for length in range(2, n):
            for l in range(n - length):
                r = l + length

                for k in range(l + 1, r):
                    dp[l][r] = max(
                        dp[l][r],
                        dp[l][k]
                        + dp[k][r]
                        + arr[l] * arr[k] * arr[r]
                    )

        return dp[0][n - 1]

s = Solution()
print(s.maxCoins([3,1,5,8]))
print(s.maxCoins([1,5]))
