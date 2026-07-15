from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(lambda: defaultdict(int))
        n = len(tickets)
        for f, t in tickets:
            # print(f, t)
            graph[f][t] += 1
        print(graph)

        min_path = []
        def dfs(f, path):
            nonlocal min_path
            if len(path) >= 2:
                if min_path and min_path < path:
                    return
            if len(path) == n + 1:
                min_path = path[:]
                return

            ts = list(graph[f].keys())
            for t in ts:
                path.append(t)
                graph[f][t] -= 1
                if graph[f][t] == 0:
                    del graph[f][t]
                dfs(t, path)
                path.pop()
                graph[f][t] += 1
            return
        
        dfs('JFK', ['JFK'])
        return min_path