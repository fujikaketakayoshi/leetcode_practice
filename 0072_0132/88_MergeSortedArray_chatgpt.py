class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1        # nums1 の実データの末尾
        j = n - 1        # nums2 の末尾
        k = m + n - 1    # nums1 の末尾（ここへ書き込む）

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        print(nums1)

Solution = Solution()
Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)  # [1,2,2,3,5,6]
Solution.merge([1], 1, [], 0)                  # [1]
Solution.merge([0], 0, [1], 1)                  # [1]
Solution.merge([4,5,6,0,0,0], 3, [1,2,3], 3)  # [1,2,3,4,5,6]
Solution.merge([2,0], 1, [1], 1)               # [1,2]
Solution.merge([0,0,3,0,0,0], 3, [-1,1,1], 3) # [-1,0,0,0,1,1]
Solution.merge([1,2,4,5,6,0], 5, [3], 1)      # [1,2,3,4,5,6]   