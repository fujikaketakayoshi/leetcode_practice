class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (
            n > 0 and
            # 2の冪乗を判定する条件
            (n & (n - 1)) == 0 and 
            # そのうち4の冪乗を判定する条件
            n % 3 == 1
        )