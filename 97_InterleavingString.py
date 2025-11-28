class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 == 0 or l2 == 0:
            if s1 == s2 and s1 == s3:
                return True
            else:
                return False
        
        def dfs(i1, i2):
            # print(i1, i2, i1 + i2, s1[i1], s2[i2], s3[i1 + i2])
            if i1 == l1 and i2 == l2:
                return True
            if i1 < l1 and s1[i1] == s3[i1 + i2]:
                if dfs(i1 + 1, i2):
                    return True
            if i2 < l2 and s2[i2] == s3[i1 + i2]:
                if dfs(i1, i2 + 1):
                    return True
            if i1 < l1 and i2 < l2 and s1[i1] != s3[i1 + i2] and s2[i2] != s3[i1 + i2]:
                return False

        return dfs(0, 0)

Solution = Solution()
print(Solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
print(Solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # False
print(Solution.isInterleave("", "", ""))                          # True
print(Solution.isInterleave("a", "", "c"))                          # False
print(Solution.isInterleave("abc", "def", "adbcef"))                    # True
print(Solution.isInterleave("abc", "def", "abdecf"))                    # False
print(Solution.isInterleave("aaaa", "bbbb", "aaaabbbb"))                # True
