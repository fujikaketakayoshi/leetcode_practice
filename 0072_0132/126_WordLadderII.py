class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if not endWord in wordList:
            return []
        
        n = len(beginWord)
        tmp = [beginWord]
        results = []
        def dfs(word, words):
            match_num = 0
            for i in range(n):
                if word[i] == endWord[i]:
                    match_num += 1
            if match_num == n - 1:
                tmp.append(endWord)
                return results.append(tmp.copy())
            for w in words:
                match_num = 0
                for i in range(n):
                    if word[i] == w[i]:
                        match_num += 1
                if match_num == n - 1:
                    tmp.append(w)
                    words.remove(w)
                    dfs(w, words)
                    tmp.pop()
                    words.append(w)
                else:
                    return
        
        dfs(beginWord, wordList)
        min_len = float('INF')
        result = []
        for r in results:
            if min_len > len(r):
                min_len = len(r)
                result.append(r)
            elif min_len == len(r):
                result.append(r)
        return result

Solution = Solution()
print(Solution.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution.findLadders("a", "c", ["a","b","c"]))
print(Solution.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))

