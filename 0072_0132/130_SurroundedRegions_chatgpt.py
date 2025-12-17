class Solution:
    def solve(self, board: list[list[str]]) -> None:
        from collections import deque

        m, n = len(board), len(board[0])
        q = deque()

        # 外周の O をキューに入れる
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    q.append((i, j))
        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == 'O':
                    q.append((i, j))

        # 外周から到達可能な O をマーク
        while q:
            y, x = q.popleft()
            if board[y][x] != 'O':
                continue
            board[y][x] = '#'
            for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == 'O':
                    q.append((ny, nx))

        # 仕上げ
        for y in range(m):
            for x in range(n):
                if board[y][x] == 'O':
                    board[y][x] = 'X'
                elif board[y][x] == '#':
                    board[y][x] = 'O'


solution = Solution()
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
solution.solve(board)
print(board)  # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
