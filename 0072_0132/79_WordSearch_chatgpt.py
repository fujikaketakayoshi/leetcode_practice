class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ly, lx = len(board), len(board[0])
        visited = [[False] * lx for _ in range(ly)]

        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        def dfs(y, x, idx):
            # word をすべて見つけた
            if idx == len(word):
                return True

            # 範囲外 or すでに使用済み or 文字が違う
            if not (0 <= y < ly and 0 <= x < lx):
                return False
            if visited[y][x]:
                return False
            if board[y][x] != word[idx]:
                return False

            visited[y][x] = True

            for d in range(4):
                if dfs(y + dy[d], x + dx[d], idx + 1):
                    return True

            visited[y][x] = False
            return False

        for y in range(ly):
            for x in range(lx):
                if board[y][x] == word[0]:
                    if dfs(y, x, 0):
                        return True

        return False

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