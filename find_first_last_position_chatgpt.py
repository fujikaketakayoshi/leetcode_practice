class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findLeft():
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                print(mid)
                if nums[mid] >= target:
                    hi = mid - 1
                else:
                    lo = mid + 1
                if nums[mid] == target:
                    ans = mid
            return ans

        def findRight():
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                print(mid)
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
                if nums[mid] == target:
                    ans = mid
            return ans

        return [findLeft(), findRight()]

solution = Solution()
print(solution.searchRange([8,8,8,8,8,8], 8))