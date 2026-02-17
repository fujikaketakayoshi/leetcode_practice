class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ly = len(matrix)
        lx = len(matrix[0])
        
        def square(y, x, l):
            for ny in range(y, y + l):
                for nx in range(x, x + l):
                    # print(ny, nx)
                    if 0 <= ny <= ly - 1 and 0 <= nx <= lx - 1 and matrix[ny][nx] == '1':
                        continue
                    else:
                        return False
            return True
        
        l = 1
        for y in range(ly):
            for x in range(lx):
                while True:
                    # print(square(y, x, l))
                    if square(y, x, l):
                        l += 1
                    else:
                        break
        return (l - 1) ** 2
