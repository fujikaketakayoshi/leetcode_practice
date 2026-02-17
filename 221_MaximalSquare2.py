class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ly = len(matrix)
        lx = len(matrix[0])
        stack = [0] * lx

        max_square = 0
        for y in range(ly):
            max_success = 0
            max_stack = 0
            success = 0
            for x in range(lx):
                v = int(matrix[y][x])
                if v == 1:
                    stack[x] += 1
                    max_stack = max(max_stack, stack[x])
                    success += 1
                    max_success = max(max_success, success)
                else:
                    stack[x] = 0
                    success = 0
            max_square = max(max_square, min(max_stack, max_success))
        
        return max_square ** 2
