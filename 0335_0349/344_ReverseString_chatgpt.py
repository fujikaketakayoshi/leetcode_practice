class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            r = -1 * (i + 1)
            s[i], s[r] = s[r], s[i]
        print(s)

so = Solution()
so.reverseString(["h", "e", "l", "l", "o"])
