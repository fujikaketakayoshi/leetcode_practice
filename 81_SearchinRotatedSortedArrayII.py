class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                return True
            elif nums[mid] < target and nums[right] < target:
                right = mid - 1
            elif nums[mid] > target and nums[left] > target:
                left = mid + 1
            elif nums[mid] < target and nums[right] > target:
                left = mid + 1
            elif nums[mid] > target and nums[left] < target:
                right = mid - 1
        return False

solution = Solution()
print(solution.search([2,5,6,0,0,1,2], 0))  # Output: True
print(solution.search([2,5,6,0,0,1,2], 3))  # Output: False
print(solution.search([1,0,1,1,1], 0))        # Output: TrueだがFalseが出てコードが正しくない