class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)

        # 長さが合わなければ不可能
        if l1 + l2 != l3:
            return False

        # dp[i][j] = s1のi文字 + s2のj文字 → s3のi+j文字を作れるか
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                if j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[l1][l2]
