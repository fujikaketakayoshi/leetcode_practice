class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # 左側が英数字になるまで進める
            while l < r and not s[l].isalnum():
                l += 1
            # 右側も同様に
            while l < r and not s[r].isalnum():
                r -= 1

            # 大文字小文字はlowerで揃える
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True

Solution = Solution()
print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
print(Solution.isPalindrome("race a car"))
print(Solution.isPalindrome(" "))
print(Solution.isPalindrome("0P"))
print(Solution.isPalindrome("ab_a"))
print(Solution.isPalindrome("a."))
print(Solution.isPalindrome("a b a"))
print(Solution.isPalindrome("Able was I ere I saw Elba"))