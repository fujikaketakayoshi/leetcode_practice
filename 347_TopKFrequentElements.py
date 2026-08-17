from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        # print(cnt)
        cnt2 = []
        for n, v in cnt.items():
            cnt2.append((v, n))
        cnt2.sort(reverse=True)
        # print(cnt2)
        ans = []
        for i in range(k):
            ans.append(cnt2[i][1])
        
        return ans