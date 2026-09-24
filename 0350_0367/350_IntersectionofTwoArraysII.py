from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        for k, v in cnt1.items():
            if k in cnt2:
                cnt = min(v, cnt2[k])
                ans += [k] * cnt
        return ans

s = Solution()
print(s.intersect([1,2,2,1], [2,2]))
