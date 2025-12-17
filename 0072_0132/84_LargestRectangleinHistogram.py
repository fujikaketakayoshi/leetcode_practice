class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        lh = len(heights)
        max_rect = 0
        for i in range(lh):
            target = heights[i]
            left = i - 1
            right = i + 1
            while left >= 0:
                if target > heights[left]:
                    break
                left -= 1
            while right < lh :
                if target > heights[right]:
                    break
                right += 1
            width = right - left - 1
            rect = width * target
            max_rect = max(max_rect, rect)
        return max_rect

solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
print(solution.largestRectangleArea([2,4]))          # Output: 4
print(solution.largestRectangleArea([0,9]))          # Output: 9
print(solution.largestRectangleArea([4,2,0,3,2,5]))  # Output: 6
