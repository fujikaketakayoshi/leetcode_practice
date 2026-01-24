class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        print(bin(n >> 1))
        while n > 0:
            # print(bin(n))
            cnt += n & 1   # 右端のビットが1なら+1
            n >>= 1       # 右に1ビットシフト
        return cnt

solution = Solution()
print(solution.hammingWeight(11))  # 出力: 3
print(solution.hammingWeight(128))  # 出力: 1
print(solution.hammingWeight(4294967293))  # 出力: 31
