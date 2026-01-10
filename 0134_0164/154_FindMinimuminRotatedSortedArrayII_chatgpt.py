class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                # nums[mid] == nums[right]
                right -= 1

        return nums[left]

solution = Solution()
print(solution.findMin([3,4,5,1,2]))  # Output: 1
print(solution.findMin([4,5,6,7,0,1,2]))  # Output: 0
print(solution.findMin([11,13,15,17]))  # Output: 11
print(solution.findMin([3,3,1,3]))  # Output: 1