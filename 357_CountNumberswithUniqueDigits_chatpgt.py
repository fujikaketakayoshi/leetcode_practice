class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 10

        cur = 9
        choices = 9

        for digits in range(2, n + 1):
            cur *= choices
            ans += cur
            choices -= 1

        return ans