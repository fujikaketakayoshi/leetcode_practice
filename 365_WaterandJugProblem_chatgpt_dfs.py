class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()

        def dfs(a, b):
            if (a, b) in visited:
                return False

            visited.add((a, b))

            if a == target or b == target or a + b == target:
                return True

            # aを満杯
            if dfs(x, b):
                return True

            # bを満杯
            if dfs(a, y):
                return True

            # aを空にする
            if dfs(0, b):
                return True

            # bを空にする
            if dfs(a, 0):
                return True

            # a -> b
            move = min(a, y - b)
            if dfs(a - move, b + move):
                return True

            # b -> a
            move = min(b, x - a)
            if dfs(a + move, b - move):
                return True

            return False

        return dfs(0, 0)

s = Solution()
print(s.canMeasureWater(3, 5, 4))
print(s.canMeasureWater(13, 11, 1))