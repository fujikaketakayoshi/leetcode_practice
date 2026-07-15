from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        n = len(tickets)
        for f, t in tickets:
            # print(f, t)
            graph[f].append(t)
        # print(graph)

        for f in graph:
            graph[f].sort(reverse=True)
        
        ans = []
        def dfs(f):    
            while graph[f]:
                t = graph[f].pop()
                dfs(t)
            ans.append(f)
        
        dfs('JFK')
        # print(ans)
        ans.reverse()
        return ans