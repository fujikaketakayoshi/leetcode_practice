class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            j = i
            while j < n and nums[j] == 0:
                j += 1
            if j >= n:
                break
            # print(i, j)
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        print(nums)

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
print(s.moveZeroes([0,0,1]))