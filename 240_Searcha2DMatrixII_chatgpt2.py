class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                if target in row:
                    return True
        return False

solution = Solution()
print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))  # 出力: True
print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))  # 出力: False   
