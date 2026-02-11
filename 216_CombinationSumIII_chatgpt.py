class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []

        def dfs(start, path, total):
            # 個数がkになった
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return

            # 次に選ぶ数字
            for i in range(start, 10):
                # pruning（これ重要）
                if total + i > n:
                    break

                path.append(i)
                dfs(i + 1, path, total + i)
                path.pop()

        dfs(1, [], 0)
        return ans

solution = Solution()
print(solution.combinationSum3(3, 7))  # 出力: [[1,2,4]]
print(solution.combinationSum3(3, 9))  # 出力: [[1,2,6],[1,3,5],[2,3,4]]
print(solution.combinationSum3(4, 1))  # 出力: []
print(solution.combinationSum3(3, 2))  # 出力: []
print(solution.combinationSum3(9, 45))  # 出力: [[1,2,3,4,5,6,7,8,9]]
