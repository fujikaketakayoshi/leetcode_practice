from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        results = []
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        stack = deque()
        for k, v in enumerate(indeg):
            if v == 0:
                stack.append(k)
                results.append(k)
        
        while stack:
            v = stack.popleft()
            for u in graph[v]:
                indeg[u] -= 1
                if indeg[u] == 0:
                    stack.append(u)
                    results.append(u)
        
        if len(results) != numCourses:
            return []
        return results

solution = Solution()
print(solution.findOrder(3, [[1,0],[1,2],[0,1]]))
