class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('INF')] * (amount + 1)
        dp[amount] = 0
        for a in range(amount, -1, -1):
            for c in coins:
                if a - c >= 0:
                    # print(a, c, dp[a - c], dp[a] + 1)
                    dp[a - c] = min(dp[a - c], dp[a] + 1)
        # print(dp)
        return dp[0] if dp[0] != float('INF') else -1

s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([233, 408, 101, 448, 235, 339, 40, 211], 7392))
