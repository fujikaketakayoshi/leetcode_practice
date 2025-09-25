class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            print(nums[left], nums[right])
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left

solution = Solution()
#print(solution.removeElement([3,2,2,3], 3))
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))