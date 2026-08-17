from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        N = len(nums)
        bucket = [[] for _ in range(N + 1)]
        for n, f in cnt.items():
            bucket[f].append(n)
        # print(bucket)
        ans = []
        for i in range(N, -1, -1):
            if bucket[i]:
                ans += bucket[i]
                if len(ans) >= k:
                    return ans