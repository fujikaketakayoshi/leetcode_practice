class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        nboard = [[None] * n for _ in range(m)]

        dy = [-1, -1, 0, 1, 1, 1, 0, -1]
        dx = [0, 1, 1, 1, 0, -1, -1, -1]

        for y in range(m):
            for x in range(n):
                live, dead = 0, 0
                yx = board[y][x]
                for d in range(8):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if not (0 <= ny < m and 0 <= nx < n):
                        continue
                    if board[ny][nx] == 1:
                        live += 1
                    else:
                        dead += 1
                if yx == 1:
                    if 0 <= live <= 1 or live >= 4:
                        nboard[y][x] = 0
                    else:
                        nboard[y][x] = 1
                else:
                    if live == 3:
                        nboard[y][x] = 1
                    else:
                        nboard[y][x] = 0
        for y in range(m):
            for x in range(n):
                board[y][x] = nboard[y][x]

s = Solution()
b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(b)
print(b)  # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
