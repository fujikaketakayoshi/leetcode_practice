from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False

        return target % gcd(x, y) == 0

s = Solution()
print(s.canMeasureWater(3, 5, 4))
print(s.canMeasureWater(13, 11, 1))