class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        row = 0
        col = n - 1   # 右上
        
        while row < m and col >= 0:
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1
        
        return False

solution = Solution()
print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))  # 出力: True
print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))  # 出力: False   
