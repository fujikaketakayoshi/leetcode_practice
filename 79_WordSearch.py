#from collections import deque

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ly = len(board)
        lx = len(board[0])
        
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        goal = False

        def dfs(y, x, result):
            nonlocal goal
            if result == word:
                goal = True
                return
            if y < 0 or y >= ly or x < 0 or x >= lx or cache[y][x]:
                return
            lr = len(result)
            if board[y][x] == word[lr:lr + 1]:
                for dir in range(4):
                    ny = y + dy[dir]
                    nx = x + dx[dir]
                    cache[y][x] = True
                    dfs(ny, nx, result + board[y][x])
                    cache[y][x] = False
        
        for y in range(ly):
            for x in range(lx):
                cache = [[False] * lx for _ in range(ly)]
                dfs(y, x, '')

        return goal

solution = Solution
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(solution.exist(solution, board, word))  # True
word = "SEE"
print(solution.exist(solution, board, word))  # True
word = "ABCB"
print(solution.exist(solution, board, word))  # False
word = "ABFSAD"
print(solution.exist(solution, board, word))  # True
word = "ABCD"
print(solution.exist(solution, board, word))  # False
word = "A"
print(solution.exist(solution, board, word))  # True
word = "E"
print(solution.exist(solution, board, word))  # True
word = "ABCESEEEFS"
print(solution.exist(solution, board, word))  # True