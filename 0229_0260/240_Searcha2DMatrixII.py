import bisect
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        cols = []
        for c in range(n):
            col = []
            for r in range(m):
                col.append(matrix[r][c])
            cols.append(col)
        print(cols)

        now = 0
        idx = 0
        visited = set()
        while True:
            if now == 0:
                rowcols = matrix[idx]
                nrowcols = n
            else:
                rowcols = cols[idx]
                nrowcols = m
            if (now, idx) in visited:
                return False
            visited.add((now, idx))
            print(rowcols)
            nrb = n if nrowcols == m else m
            if idx + 1 == nrb:
                tmp_idx = bisect.bisect_right(rowcols, target)
            else:
                tmp_idx = bisect.bisect_left(rowcols, target)
            print(tmp_idx)
            if tmp_idx < nrowcols and rowcols[tmp_idx] == target:
                return True
            nrb = n if nrowcols == m else m
            idx = tmp_idx - 1
            now = 1 if now == 0 else 0

solution = Solution()
print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))  # 出力: True
print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))  # 出力: False   
