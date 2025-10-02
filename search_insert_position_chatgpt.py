class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 探索が終わったとき、left が挿入位置
        return left

Solution = Solution()
print(Solution.searchInsert([1,3,5,6], 0))