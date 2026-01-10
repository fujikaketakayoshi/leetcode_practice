class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] > nums[(mid + 1) % n]:
                return mid
            if nums[-1] < nums[0] > nums[1 % n]:
                return 0
            if nums[-2] < nums[-1] > nums[0]:
                return n - 1

            if nums[mid - 1] < nums[mid] < nums[right]:
                left = mid + 1
            elif nums[left] > nums[mid] > nums[mid + 1]:
                right = mid
            else:
                right -= 1

solution = Solution()
print(solution.findPeakElement([1,2,3,1]))  # Output: 2
print(solution.findPeakElement([1,2,1,3,5,6,4]))  # Output: 5
print(solution.findPeakElement([1]))  # Output: 0
print(solution.findPeakElement([2,1]))  # Output: 0
print(solution.findPeakElement([1,2]))  # Output: 1
print(solution.findPeakElement([3,2,1]))  # Output: 0
