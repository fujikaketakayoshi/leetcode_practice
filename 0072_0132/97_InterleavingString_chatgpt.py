class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)

        # 長さ不一致は即False
        if l1 + l2 != l3:
            return False

        # 空文字対策（これがあなたが詰んだ原因）
        if l1 == 0:
            return s2 == s3
        if l2 == 0:
            return s1 == s3

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i1, i2):
            if i1 == l1 and i2 == l2:
                return True

            k = i1 + i2  # s3側のインデックス

            # s1から取れる場合
            if i1 < l1 and s1[i1] == s3[k]:
                if dfs(i1 + 1, i2):
                    return True

            # s2から取れる場合
            if i2 < l2 and s2[i2] == s3[k]:
                if dfs(i1, i2 + 1):
                    return True

            return False  # ← これが必須

        return dfs(0, 0)

Solution = Solution()
print(Solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
print(Solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # False
print(Solution.isInterleave("", "", ""))                          # True
print(Solution.isInterleave("a", "", "c"))                          # False
print(Solution.isInterleave("abc", "def", "adbcef"))                # True
print(Solution.isInterleave("aaaa", "bbbb", "aaaabbbb"))            # True
