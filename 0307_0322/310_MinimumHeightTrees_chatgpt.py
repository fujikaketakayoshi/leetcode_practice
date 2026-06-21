from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque()

        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        remain = n

        while remain > 2:

            sz = len(leaves)
            remain -= sz

            for _ in range(sz):

                leaf = leaves.popleft()

                for nxt in graph[leaf]:

                    degree[nxt] -= 1

                    if degree[nxt] == 1:
                        leaves.append(nxt)

        return list(leaves)

s = Solution()
print(s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(s.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
