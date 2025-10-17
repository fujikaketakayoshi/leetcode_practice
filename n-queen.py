class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # r + c
        diag2 = set()  # r - c

        def dfs(r: int):
            # n 行すべてにクイーンを置けたら解答
            if r == n:
                results.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in diag1 or (r - c) in diag2:
                    continue  # 攻撃範囲なのでスキップ

                # 置く
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r + c)
                diag2.add(r - c)

                dfs(r + 1)  # 次の行へ

                # 戻す（バックトラック）
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)

        dfs(0)
        return results


# Example usage:
solution = Solution()
print(solution.solveNQueens(1))
print(solution.solveNQueens(2))
print(solution.solveNQueens(3))
print(solution.solveNQueens(4))
print(solution.solveNQueens(5))