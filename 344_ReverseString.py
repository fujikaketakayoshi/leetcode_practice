class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
        for i in range(n):
            r = -1 * (i + 1)
            s[i], s[r] = s[r], s[i]
