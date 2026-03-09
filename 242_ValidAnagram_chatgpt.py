from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))  # False
