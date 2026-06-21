class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        words_sets = []
        for w in words:
            words_sets.append({
                'set': set(w),
                'len': len(w),
            })
        print(words_sets[0]['set'])
        
        max_v = 0
        for i in range(n):
            iset = words_sets[i]['set']
            il = words_sets[i]['len']
            for j in range(i + 1, n):
                jl = 0
                if iset.isdisjoint(words_sets[j]['set']):
                    jl = words_sets[j]['len']
                max_v = max(max_v, il * jl)
        return max_v

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
