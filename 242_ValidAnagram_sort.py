class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(sorted(s))
        return sorted(s) == sorted(t)

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))  # False
