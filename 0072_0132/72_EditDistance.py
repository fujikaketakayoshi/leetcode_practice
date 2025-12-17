class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初期化
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # DPループ
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # delete
                        dp[i][j - 1],     # insert
                        dp[i - 1][j - 1]  # replace
                    )

        return dp[m][n]

solution = Solution()
word1 = "intention"
word2 = "execution"
print(solution.minDistance(word1, word2))  # 出力: 5
word1 = "horse"
word2 = "ros"
print(solution.minDistance(word1, word2))  # 出力: 3
word1 = "intention"
word2 = "ntentiona"
print(solution.minDistance(word1, word2))  # 出力: 2
