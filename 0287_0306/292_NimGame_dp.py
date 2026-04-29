class Solution:
    def canWinNim(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            for take in range(1, 4):
                print(i, take, dp)
                if i - take >= 0 and not dp[i - take]:
                    dp[i] = True
                    break

        return dp[n]

s = Solution()
print(s.canWinNim(4))  # False
print(s.canWinNim(1))  # True
print(s.canWinNim(13))  # True
