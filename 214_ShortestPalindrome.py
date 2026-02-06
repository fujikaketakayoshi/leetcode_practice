class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        s2 = ''
        pre = ''
        for i in range(0, n):
            s2 += s[i]
            if s2 == s2[::-1]:
                pre = s[i + 1:]
        ans = pre[::-1] + s 
        return ans

solution = Solution()
print(solution.shortestPalindrome("aacecaaa"))
print(solution.shortestPalindrome("abcd"))
print(solution.shortestPalindrome("abb"))