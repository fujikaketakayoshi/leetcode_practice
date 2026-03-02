class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        for i in range(n + 1):
            d = i
            while d > 0:
                digit = d % 10
                if digit == 1:
                    cnt += 1
                d //= 10
        return cnt

solution = Solution()
print(solution.countDigitOne(13))  # 出力: 6
print(solution.countDigitOne(824883294))