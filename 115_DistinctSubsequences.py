class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)
        cnt = 0
        for S in range(1 << ns):
            idx = []
            for i in range(ns):
                if (S >> i) & 1:
                    idx.append(i)
            if len(idx) == nt:
                cand = ''
                for j in idx:
                    cand += s[j]
                if cand == t:
                    cnt += 1

        return cnt

print(Solution().numDistinct("rabbbit", "rabbit"))
print(Solution().numDistinct("babgbag", "bag"))
print(Solution().numDistinct("a", "a"))
print(Solution().numDistinct("a", "b"))
print(Solution().numDistinct("ccc", "c"))
print(Solution().numDistinct("abcd", "abcd"))
