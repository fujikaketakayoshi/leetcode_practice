class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        min_num = float('INF')
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            min_num = min(min_num, nums[mid])
            if nums[left] < nums[mid] < nums[right]:
                min_num = min(min_num, nums[left])
                break
            elif nums[right] < nums[left] < nums[mid]:
                left = mid + 1
            elif nums[mid] < nums[right] < nums[left]:
                right = mid - 1
            elif nums[left] == nums[mid] > nums[right]:
                min_num = min(min_num, nums[right])
                break
            else:
                left += 1
                right -= 1
        return min_num

solution = Solution()
print(solution.findMin([3,4,5,1,2]))  # Output: 1
print(solution.findMin([4,5,6,7,0,1,2]))  # Output: 0
print(solution.findMin([11,13,15,17]))  # Output: 11
