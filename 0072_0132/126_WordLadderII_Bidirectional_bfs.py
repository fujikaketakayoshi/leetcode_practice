class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        from collections import defaultdict
        # 双方向 BFS 用
        begin_front = {beginWord}
        end_front = {endWord}
        is_forward = True
        children = defaultdict(list)
        word_len = len(beginWord)

        found = False

        while begin_front and end_front and not found:
            # 小さい側を進める（双方向 BFS のキモ）
            if len(begin_front) > len(end_front):
                begin_front, end_front = end_front, begin_front
                is_forward = not is_forward

            next_front = set()
            wordSet -= begin_front

            for word in begin_front:
                for i in range(word_len):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]: 
                            continue
                        new_word = word[:i] + c + word[i+1:]
                        if new_word not in wordSet:
                            continue
                        if new_word in end_front:
                            found = True
                        else:
                            next_front.add(new_word)

                        # 向きの調整（双方向 BFS の注意点）
                        if is_forward:
                            children[word].append(new_word)
                        else:
                            children[new_word].append(word)

            begin_front = next_front

        # 見つからなかった
        if not found:
            return []

        # DFS で経路復元
        res = []
        path = [beginWord]

        def dfs(word):
            if word == endWord:
                res.append(path[:])
                return
            for nxt in children[word]:
                path.append(nxt)
                dfs(nxt)
                path.pop()

        dfs(beginWord)
        return res

Solution = Solution()
print(Solution.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution.findLadders("a", "c", ["a","b","c"]))
print(Solution.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
