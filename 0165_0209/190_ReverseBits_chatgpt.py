class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

solution = Solution()
print(solution.reverseBits(43261596))  # 出力: 964176192
print(solution.reverseBits(4294967293))  # 出力: 3221225471
print(solution.reverseBits(0))  # 出力: 0
print(solution.reverseBits(1))  # 出力: 2147483648
print(solution.reverseBits(2))  # 出力: 1073741824