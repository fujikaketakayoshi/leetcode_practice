from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        H = len(matrix)
        W = len(matrix[0])

        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        max_p = 1
        for h in range(H):
            for w in range(W):
                # print(h, w)
                q = deque()
                q.append((h, w, 1))
                while q:
                    y, x, p = q.popleft()
                    # print(y,x,p)
                    max_p = max(max_p, p)
                    for dy, dx in DIRS:
                        ny = dy + y
                        nx = dx + x
                        if not (0 <= ny < H and 0 <= nx < W):
                            continue
                        if matrix[ny][nx] <= matrix[y][x]:
                            continue
                        q.append((ny, nx, p + 1))
                    # print(q)
        return max_p
