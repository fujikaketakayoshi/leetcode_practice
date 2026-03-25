import bisect
class Solution:
    def numSquares(self, n: int) -> int:
        i = 0
        sqs = []
        while i <= 10 ** 2:
            sqs.append(i ** 2)
            i += 1
        # print(sqs)
        min_cnt = float('INF')
        idx = bisect.bisect_left(sqs, n)
        results = [[] for _ in range(idx)]
        while idx > 0:
            cnt = n // sqs[idx]
            tmp_n = n % sqs[idx]
            i = 1
            while idx - i > 0:
                cnt += tmp_n // sqs[idx - i]
                tmp_n %= sqs[idx - i]
                i += 1
            min_cnt = min(min_cnt, cnt)
            idx -= 1
        return min_cnt

s = Solution()
print(s.numSquares(12)) # 3
print(s.numSquares(13)) # 2
print(s.numSquares(1)) # 1
print(s.numSquares(43)) # 3