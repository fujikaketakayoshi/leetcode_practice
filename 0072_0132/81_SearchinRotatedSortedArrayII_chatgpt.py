class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 見つかった
            if nums[mid] == target:
                return True

            # 重複で判断不能 → 1個縮める
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # 左側がソートされている場合
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # 右側がソートされている場合
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

solution = Solution()
print(solution.search([2,5,6,0,0,1,2], 0))  # Output: True
print(solution.search([2,5,6,0,0,1,2], 3))  # Output: False
print(solution.search([1,0,1,1,1], 0))        # Output: True
print(solution.search([1,1,3,1], 3))        # Output: True