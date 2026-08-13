class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        vowels = set("aeiouAEIOU")

        l = 0
        r = len(ss) - 1

        while l < r:
            while l < r and ss[l] not in vowels:
                l += 1

            while l < r and ss[r] not in vowels:
                r -= 1

            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1

        return ''.join(ss)