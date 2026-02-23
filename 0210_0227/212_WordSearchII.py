class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        prewords = set()
        setwords = set(words)
        for w in words:
            pre = ''
            for c in w:
                pre += c
                prewords.add(pre)

        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        H, W = len(board), len(board[0])

        results = set()

        def dfs(y, x, path):
            if not path in prewords:
                return
            if path in setwords:
                results.add(path)

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny <= H - 1 and 0 <= nx <= W - 1:
                    if visited[ny][nx]:
                        continue
                    visited[ny][nx] = True
                    dfs(ny, nx, path + board[ny][nx])
                    visited[ny][nx] = False
        
        for y in range(H):
            for x in range(W):
                visited = [[False] * W for _ in range(H)]
                visited[y][x] = True
                dfs(y, x, board[y][x])
        
        return list(results)

solution = Solution()
print(solution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(solution.findWords([["a","b"],["c","d"]], ["abcb"]))
print(solution.findWords([["a"]], ["a","b"]))
print(solution.findWords([["a","a"]], ["aaa"]))
print(solution.findWords([["a","b","c"],["a","e","d"],["a","f","g"]], ["abcdefg","gfedcba","eaabcdgf","befa","dgc","ade"])) 
print(solution.findWords([["a","b","c","e"],["s","f","c","s"],["a","d","e","e"]], ["see","se","abcb"])) 