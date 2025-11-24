class Solution:
    def grayCode(self, n: int) -> list[int]:
        initial = "0" * n
        cache = set()
        cache.add(initial)
        results = []
        def dfs(path):
            if len(path) == 2 ** n:
                l, r = path[0], path[-1]
                diff = 0
                for i in range(len(l)):
                    if l[i] != r[i]:
                        diff += 1
                if diff == 1:
                    results.append(path.copy())
                    return True
            bit = path[-1]
            for i in range(n):
                change = '0' if bit[i] == '1' else '1'
                tmp = bit[0:i] + change + bit[i+1:]
                if tmp in cache:
                    continue
                cache.add(tmp)
                path.append(tmp)
                if dfs(path):
                    return True
                path.pop()
                cache.remove(tmp)

        dfs([initial])
        return [int(r, 2) for r in results[0]]

Solution = Solution()
print(Solution.grayCode(2))  # [0,1,3,2]
print(Solution.grayCode(1))  # [0,1]
print(Solution.grayCode(3))  # [0,1,3,2,6,7,5,4]
print(Solution.grayCode(4))  # [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]