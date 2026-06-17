class Solution:
    def coinChange(self, coins, amount):
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], dp[a-c] + 1)

        return dp[amount] if dp[amount] != INF else -1

s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([233, 408, 101, 448, 235, 339, 40, 211], 7392))
