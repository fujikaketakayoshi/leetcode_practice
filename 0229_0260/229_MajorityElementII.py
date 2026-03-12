from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        print(cnt)
        sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        print(sorted_cnt)
        lnums = len(nums)
        results = []
        for (k, v) in sorted_cnt:
            print((k, v), v/lnums, 1/3)
            if v / lnums > 1 / 3:
                results.append(k)
        return results
