class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # (index, height)
        max_area = 0

        for i, h in enumerate(heights + [0]):  # 最後に番兵0
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
            print(stack)

        return max_area


solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
print(solution.largestRectangleArea([2,4]))          # Output: 4
print(solution.largestRectangleArea([0,9]))          # Output: 9
print(solution.largestRectangleArea([4,2,0,3,2,5]))  # Output: 6
