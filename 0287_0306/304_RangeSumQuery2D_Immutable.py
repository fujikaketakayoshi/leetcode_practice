class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ny, nx = len(matrix), len(matrix[0])
        self.pre_sum = [[0] * (nx + 1) for _ in range(ny + 1)]
        for y in range(1, ny + 1):
            for x in range(1, nx + 1):
                # print(y, x)
                self.pre_sum[y][x] = -self.pre_sum[y - 1][x - 1] + self.pre_sum[y - 1][x] + self.pre_sum[y][x - 1] + matrix[y - 1][x - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row1][col1] - self.pre_sum[row1][col2 + 1] - self.pre_sum[row2 + 1][col1] + self.pre_sum[row2 + 1][col2 + 1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
row1, col1, row2, col2 = 2, 1, 4, 3
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(row1,col1,row2,col2)
print(param_1)