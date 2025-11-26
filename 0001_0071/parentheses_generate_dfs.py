class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results = []

        def backtrack(cur: str, open_count: int, close_count: int):
            # n 個ずつ使ったら完成
            if open_count == n and close_count == n:
                results.append(cur)
                return

            # '(' を追加できるなら追加
            if open_count < n:
                backtrack(cur + "(", open_count + 1, close_count)

            # ')' を追加できるなら追加
            if close_count < open_count:
                backtrack(cur + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return results

solution = Solution()
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(4))
print(solution.generateParenthesis(5))
