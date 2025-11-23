class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < l1 and j < l2:
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
            elif nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
            i += 1
        nums1.sort()
        print(nums1)

Solution = Solution()
Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)  # [1,2,2,3,5,6]
Solution.merge([1], 1, [], 0)                  # [1]
Solution.merge([0], 0, [1], 1)                  # [1]
Solution.merge([4,5,6,0,0,0], 3, [1,2,3], 3)  # [1,2,3,4,5,6]
Solution.merge([2,0], 1, [1], 1)               # [1,2]
Solution.merge([0,0,3,0,0,0], 3, [-1,1,1], 3) # [-1,0,0,0,1,1]
Solution.merge([1,2,4,5,6,0], 5, [3], 1)      # [1,2,3,4,5,6]