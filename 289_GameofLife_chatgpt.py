class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # 1回目：中間状態を書き込む
        for y in range(m):
            for x in range(n):
                live = 0

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < m and 0 <= nx < n:
                        if abs(board[ny][nx]) == 1:
                            live += 1

                # 現在 live
                if board[y][x] == 1:
                    if live < 2 or live > 3:
                        board[y][x] = -1   # live -> dead

                # 現在 dead
                else:
                    if live == 3:
                        board[y][x] = 2    # dead -> live

        # 2回目：最終状態に戻す
        for y in range(m):
            for x in range(n):
                if board[y][x] > 0:
                    board[y][x] = 1
                else:
                    board[y][x] = 0

s = Solution()
b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(b)
print(b)  # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]