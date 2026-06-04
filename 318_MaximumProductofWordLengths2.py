class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        max_v = 0
        for i in range(n):
            iw = set(words[i])
            i_cnt = len(words[i])
            for j in range(i + 1, n):
                j_cnt = 0
                if iw.isdisjoint(set(words[j])):
                    j_cnt = len(words[j])
                max_v = max(max_v, i_cnt * j_cnt)
        return max_v

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
