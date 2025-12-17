class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque
        m, n = len(board), len(board[0])
        Oset = set()
        Os = []
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        for y in range(1, m - 1):
            for x in range(1, n - 1):
                if board[y][x] == 'O' and not (y, x) in Oset:
                    Oset.add((y, x))
                    tmpOset = set()
                    tmpOset.add((y, x))
                    queue = deque()
                    queue.append((y, x))
                    while queue:
                        y, x = queue.popleft()
                        for d in range(4):
                            ny = y + dy[d]
                            nx = x + dx[d]
                            if 0 < ny < m - 1 and 0 < nx < n - 1 and board[ny][nx] == 'O' and not (ny, nx) in Oset:
                                Oset.add((ny, nx))
                                tmpOset.add((ny, nx))
                                queue.append((ny, nx))
                    Os.append(tmpOset.copy())
        
        index_Os_X = []
        for i, O in enumerate(Os):
            tmpBool = True
            for y, x in O:
                if tmpBool:
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if board[ny][nx] == 'O' and not(0 < ny < m - 1 and 0 < nx < n - 1):
                            tmpBool = False
                            break
            if tmpBool:
                index_Os_X.append(i)

        for i in index_Os_X:
            for y, x in Os[i]:
                board[y][x] = 'X'

solution = Solution()
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
solution.solve(board)
print(board)  # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
