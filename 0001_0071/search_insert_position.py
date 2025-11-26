class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
#            print(left, right, mid)
            if nums[mid] == target:
                return mid
            elif mid - 1 >= 0 and mid + 1 < len(nums) and nums[mid - 1] < target < nums[mid]:
                return mid
            elif len(nums) == 1 and target < nums[0]:
                return 0
            elif len(nums) == 1 and nums[0] < target:
                return len(nums)
            elif mid == 0 and target < nums[mid + 1] and not (nums[mid] < target):
                return 0
            elif mid == len(nums) - 1 and nums[mid] < target:
                return len(nums)
            elif mid == len(nums) - 1 and nums[mid] > target:
                return len(nums) - 1
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

Solution = Solution()
print(Solution.searchInsert([1,3,5,6], 5))
print(Solution.searchInsert([1,3,5,6], 2))
print(Solution.searchInsert([1,3,5,6], 7))
print(Solution.searchInsert([1,3,5,6], 0))
print(Solution.searchInsert([1], 0))