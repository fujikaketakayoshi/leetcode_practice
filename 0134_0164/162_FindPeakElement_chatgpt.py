class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # 右側に peak がある
                left = mid + 1
            else:
                # 左側（mid含む）に peak がある
                right = mid

        return left

solution = Solution()
print(solution.findPeakElement([1,2,3,1]))  # Output: 2
print(solution.findPeakElement([1,2,1,3,5,6,4]))  # Output: 5
print(solution.findPeakElement([1]))  # Output: 0
print(solution.findPeakElement([2,1]))  # Output: 0
print(solution.findPeakElement([1,2]))  # Output: 1
print(solution.findPeakElement([3,2,1]))  # Output: 0
print(solution.findPeakElement([2,1,2]))    # Output: 0 or 2