class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1

        for i in range(1, rowIndex + 1):
            # 後ろから更新！
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row

print(Solution().getRow(3))
print(Solution().getRow(0))
print(Solution().getRow(1))
print(Solution().getRow(10))