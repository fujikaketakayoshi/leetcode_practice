class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        from collections import defaultdict, deque

        # --- BFS ---
        neighbors = defaultdict(list)
        distance = {beginWord: 0}
        q = deque([beginWord])

        found_end = False
        level = 0
        word_len = len(beginWord)

        while q and not found_end:
            level += 1
            next_level_words = set()
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(word_len):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue
                        nxt = word[:i] + c + word[i+1:]
                        if nxt not in wordSet:
                            continue
                        neighbors[word].append(nxt)
                        if nxt not in distance:
                            distance[nxt] = level
                            next_level_words.add(nxt)
                            if nxt == endWord:
                                found_end = True
            # 次のレベルの単語をキューに入れる
            q.extend(next_level_words)
            # このレベルで使った単語は削除（重複探索防止）
            wordSet -= next_level_words

        if endWord not in distance:
            return []

        # --- DFS to collect all shortest paths ---
        res = []
        path = [beginWord]

        def dfs(word):
            if word == endWord:
                res.append(path[:])
                return
            for nxt in neighbors[word]:
                # 距離が必ず +1 になる場合だけ進む（最短経路のみ）
                if distance.get(nxt, -1) == distance[word] + 1:
                    path.append(nxt)
                    dfs(nxt)
                    path.pop()

        dfs(beginWord)
        return res
Solution = Solution()
print(Solution.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution.findLadders("a", "c", ["a","b","c"]))
print(Solution.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))    