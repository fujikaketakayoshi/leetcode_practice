class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)

        masks = []
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            masks.append(mask)

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
