from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        for es in edges:
            graph[es[0]].append(es[1])
            graph[es[1]].append(es[0])
        print(graph)
        ans = []
        q = deque()
        min_mht = None
        for i in range(n):
            q.append([i, 0])
            max_h = 0
            visited = [False] * n
            visited[i] = True
            while q:
                u, h = q.popleft()
                max_h = max(max_h, h)
                if min_mht != None and max_h > min_mht:
                    break
                for v in graph[u]:
                    if visited[v]:
                        continue
                    q.append([v, h + 1])
                    visited[v] = True
            print(i, min_mht, max_h)
            if min_mht == None:
                min_mht = max_h
                ans.append(i)
            elif min_mht > max_h:
                min_mht = max_h
                ans = [i]
            elif min_mht == max_h:
                ans.append(i)
        return ans
s = Solution()
print(s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(s.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
