from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lenp = len(pattern)
        slist = s.split()
        lens = len(slist)
        if lenp != lens:
            return False
        
        dic = defaultdict(str)
        rdic = defaultdict(str)
        for i in range(lenp):
            if slist[i] in dic:
                if dic[slist[i]] != pattern[i]:
                    return False
            else:
                p = pattern[i]
                if p in rdic:
                    if rdic[p] != slist[i]:
                        return False
                else:
                    dic[slist[i]] = p
                    rdic[p] = slist[i]

        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))  # True
print(s.wordPattern("abba", "dog cat cat fish"))  # False
print(s.wordPattern("aaaa", "dog cat cat dog"))  # False
print(s.wordPattern("abba", "dog dog dog dog"))  # False
