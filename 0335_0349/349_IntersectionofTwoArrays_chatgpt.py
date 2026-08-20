class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

s = Solution()
print(s.intersection([1,2,2,1], [2,2]))
