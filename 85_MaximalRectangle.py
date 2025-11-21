class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)  # 番兵として最後に0を追加
        max_area = 0

        for r in range(rows):
            # まずヒストグラムを作成（高さ更新）
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # ヒストグラムの最大長方形（084番と同じ）
            stack = []
            for i in range(cols + 1):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    max_area = max(max_area, h * width)
                stack.append(i)

        return max_area

solution = Solution()
print(solution.maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]))  # Output: 6
print(solution.maximalRectangle([]))  # Output: 0
print(solution.maximalRectangle([["0"]]))  # Output: 0
print(solution.maximalRectangle([["1"]]))  # Output: 1
print(solution.maximalRectangle([["0","0"]]))  # Output: 0
print(solution.maximalRectangle([["1","1"]]))  # Output: 2
print(solution.maximalRectangle([
    ["1","0","1","1","0","1"],
    ["1","1","1","1","1","1"],
    ["0","1","1","0","1","0"],
    ["1","1","1","1","1","1"]
]))  # Output: 8
print(solution.maximalRectangle([
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0"]
]))  # Output: 0
