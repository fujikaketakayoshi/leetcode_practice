class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        s2 = ''.join(chars)
        return s2 == s2[::-1]

Solution = Solution()
print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
print(Solution.isPalindrome("race a car"))
print(Solution.isPalindrome(" "))
print(Solution.isPalindrome("0P"))
print(Solution.isPalindrome("ab_a"))
print(Solution.isPalindrome("a."))
print(Solution.isPalindrome("a b a"))
print(Solution.isPalindrome("Able was I ere I saw Elba"))