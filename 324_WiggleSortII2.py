class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
        elif len(nums) > 2:
            i = 0
            while i < len(nums):
                j = i + 1
                if i % 2 == 0:
                    while j < len(nums) and nums[i] >= nums[j]:
                        j += 1
                    if j < len(nums) and nums[i] < nums[j]:
                        nums[i + 1], nums[j] = nums[j], nums[i + 1]
                else:
                    while j < len(nums) and nums[i] <= nums[j]:
                        j += 1
                    if j < len(nums) and nums[i] > nums[j]:
                        nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1

            print(nums)

            if len(nums) % 2 == 0 and nums[-2] >= nums[-1]:
                if nums[-3] > nums[-1]:
                    nums[-1], nums[-2] = nums[-2], nums[-1]
                i = len(nums) - 4
                while i > 0 and nums[i - 1] > nums[-1] and nums[-1] < nums[i + 1] and nums[i] > nums[-2]:
                    nums[-1], nums[i] = nums[i], nums[-1]
                    i -= 2
                if nums[0] > nums[-1] and nums[1] > nums[-1]:
                    nums[-1], nums[0] = nums[0], nums[-1]
            elif len(nums) % 2 == 1 and nums[-2] <= nums[-1]:
                i = len(nums) - 3
                while i > 0 and nums[i - 1] > nums[-1] and nums[-1] < nums[i + 1] and nums[i] < nums[-2]:
                    nums[-1], nums[i] = nums[i], nums[-1]
                    i -= 2
                if nums[0] < nums[-1] and nums[1] > nums[-1]:
                    nums[-1], nums[0] = nums[0], nums[-1]
            return nums

s = Solution()
print(s.wiggleSort([1, 5, 1, 1, 6, 4]))
print(s.wiggleSort([1,4,3,4,1,2,1,3,1,3,2,3,3]))
print(s.wiggleSort([5,5,5,4,4,4,4]))

