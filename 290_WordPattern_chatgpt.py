class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for p, w in zip(pattern, words):
            if p in p_to_w and p_to_w[p] != w:
                return False
            if w in w_to_p and w_to_p[w] != p:
                return False

            p_to_w[p] = w
            w_to_p[w] = p

        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))  # True
print(s.wordPattern("abba", "dog cat cat fish"))  # False
print(s.wordPattern("aaaa", "dog cat cat dog"))  # False
print(s.wordPattern("abba", "dog dog dog dog"))  # False
