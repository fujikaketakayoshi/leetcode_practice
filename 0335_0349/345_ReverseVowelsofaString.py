class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        n = len(s)
        l = 0
        r = n - 1
        vs = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        while l < r:
            while l < n and not ss[l] in vs:
                l += 1
            while 0 < r and not ss[r] in vs:
                r -= 1
            if l > r:
                break
            # print(l, r, ss[l], ss[r])
            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1
        return ''.join(ss)

s = Solution()
print(s.reverseVowels("hello"))
