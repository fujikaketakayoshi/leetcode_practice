from collections import defaultdict
import bisect
class Solution:
    def countBits(self, n: int) -> list[int]:
        MAX = 10 ** 5
        ans = [0]
        beki2 = []
        x = 1
        while x <= MAX:
            beki2.append(x)
            x *= 2
        
        for i in range(1, n + 1):
            if i in beki2:
                ans.append(1)
            else:
                bitcnt = 0
                x = i
                while x > 0:
                    idx = bisect.bisect_right(beki2, x) - 1
                    # print(x, idx, beki2[idx])
                    bitcnt += 1
                    x -= beki2[idx]
                ans.append(bitcnt)
        return ans