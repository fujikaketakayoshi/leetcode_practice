class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lo_target = -1
        hi_target = -1
        if len(nums) == 0:
            return [-1, -1]
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            #print(lo, hi, mid)
            if nums[mid] == target:
                left = mid
                right = mid
                while (left > 0 and nums[left - 1] == target) or (right < len(nums) - 1 and nums[right + 1]) == target:
                    if left > 0 and nums[left - 1] == target:
                        left -= 1
                    if right < len(nums) - 1 and nums[right + 1] == target:
                        right += 1
                return [left, right]
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            elif nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                return [-1, -1]

solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.searchRange([5,7,7,8,8,10], 6))
print(solution.searchRange([], 1))