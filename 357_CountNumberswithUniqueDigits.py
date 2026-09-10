from collections import defaultdict
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        total = 10 ** n
        exclude = set()
        for i in range(total):
            cnt = defaultdict(int)
            for d in str(i):
                cnt[d] += 1
                if cnt[d] == 2:
                    exclude.add(i)
                    break
        return total - len(exclude)