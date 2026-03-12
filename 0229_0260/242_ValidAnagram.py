from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        for c in t:
            cnt[c] -= 1
        
        return all(val == 0 for val in cnt.values())

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))  # False
