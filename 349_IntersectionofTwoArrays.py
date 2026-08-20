class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nset = set()
        for n1 in nums1:
            nset.add(n1)
        # print(nset)
        ans = set()
        for n2 in nums2:
            if n2 in nset:
                ans.add(n2)
        return list(ans)

s = Solution()
s.intersection([1,2,2,1], [2,2])
