class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        n = len(words)
        ans = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                target = words[i] + words[j]
                # print(target, target[::-1])
                if target == target[::-1]:
                    ans.append([i, j])
        return ans