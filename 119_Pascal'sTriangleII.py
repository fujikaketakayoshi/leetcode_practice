class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = [[0] * (i + 1) for i in range(rowIndex + 1)]
        dp[0][0] = 1
        for i in range(rowIndex + 1):
            dp[i][0] = 1
            dp[i][-1] = 1
            for j in range(rowIndex + 1):
                if 0 < i and 0 < j < len(dp[i - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp[rowIndex]

print(Solution().getRow(3))
print(Solution().getRow(0))
print(Solution().getRow(1))
