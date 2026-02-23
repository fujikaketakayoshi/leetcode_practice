class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        t = s + "#" + rev

        lps = [0] * len(t)

        j = 0
        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]:
                j = lps[j - 1]
            if t[i] == t[j]:
                j += 1
            lps[i] = j
            print(i,j, t[i], t[j - 1],  t[j])
        print(lps)

        # lps[-1] = 最長回文prefixの長さ
        add = rev[:len(s) - lps[-1]]
        return add + s

solution = Solution()
print(solution.shortestPalindrome("aacecaaa"))
print(solution.shortestPalindrome("abcd"))
print(solution.shortestPalindrome("abb"))