class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] * (amount + 1)
        for c in coins:
            if amount - c >= 0:
                dp[amount - c] += 1
        
        for a in range(amount, -1, -1):
            if dp[a] > 0:
                for c in coins:
                    if a - c >= 0:
                        # print(a, c)
                        if dp[a - c] > 0 and dp[a] + 1 < dp[a - c]:
                            dp[a - c] = dp[a] + 1
                        elif dp[a - c] == 0:
                            dp[a - c] = dp[a] + 1
        return dp[0] if dp[0] != 0 else -1

s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([233, 408, 101, 448, 235, 339, 40, 211], 7392))
