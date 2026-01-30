from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        rgraph = [[] for _ in range(numCourses)]
        for (u, v) in prerequisites:
            graph[u].append(v)
            rgraph[v].append(u)
        
        # print(graph, rgraph)
        visited = [False] * numCourses
        for i, vs in enumerate(graph):
            if len(vs) == 0:
                visited[i] = True
                stack = deque([rgraph[i]])
                # print(i, stack)
                while stack:
                    us = stack.pop()
                    for u in us:
                        if visited[u]:
                            continue
                        if all([visited[x] for x in graph[u]]):
                            visited[u] = True
                            stack.append(rgraph[u])
        # print(visited)
                
        return all(visited)

solution = Solution()
print(solution.canFinish(2, [[1,0]]))  # True
print(solution.canFinish(2, [[1,0],[0,1]]))  # False
print(solution.canFinish(3, [[1,0],[2,1]]))  # True
print(solution.canFinish(3, [[1,0],[0,2],[2,1]]))  # False
