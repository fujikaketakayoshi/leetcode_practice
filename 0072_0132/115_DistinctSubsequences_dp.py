class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [0] * (m + 1)
        dp[0] = 1  # 空文字は常に1通り

        for i in range(n):
            # 後ろから更新しないと上書きされる
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        
        return dp[m]

print(Solution().numDistinct("rabbbit", "rabbit"))
print(Solution().numDistinct("babgbag", "bag"))
print(Solution().numDistinct("a", "a"))
print(Solution().numDistinct("a", "b"))
print(Solution().numDistinct("ccc", "c"))
print(Solution().numDistinct("abcd", "abcd"))
