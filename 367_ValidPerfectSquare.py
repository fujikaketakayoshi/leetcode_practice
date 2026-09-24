class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        sq = 0
        while sq < num:
            sq = n * n
            if sq == num:
                return True
            n += 1
        return False