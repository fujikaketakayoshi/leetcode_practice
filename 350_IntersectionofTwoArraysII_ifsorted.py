from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        ans = []
        while i < n1 and j < n2:
            while i < n1 and j < n2 and nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            while i < n1 and j < n2 and nums1[i] > nums2[j]:
                j += 1
            while i < n1 and j < n2 and nums1[i] < nums2[j]:
                i += 1
        return ans