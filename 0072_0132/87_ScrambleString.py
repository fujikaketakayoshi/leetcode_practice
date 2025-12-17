class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            if a == b:
                memo[(a, b)] = True
                return True

            # 剪定: 文字種類が違うなら絶対に無理
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            n = len(a)

            for i in range(1, n):
                # case1: swapしない (a[:i] ↔ b[:i] and a[i:] ↔ b[i:])
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True

                # case2: swapする (a[:i] ↔ b[n-i:] and a[i:] ↔ b[:n-i])
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)

Solution = Solution()
print(Solution.isScramble("great", "rgeat"))  # True
print(Solution.isScramble("abcde", "caebd"))  # False
print(Solution.isScramble("a", "a"))          # True
print(Solution.isScramble("abc", "bca"))      # True
print(Solution.isScramble("abb", "bab"))      # True
print(Solution.isScramble("abcd", "bdac"))    # False
print(Solution.isScramble("abcdefghijklmnopq", "efghijklmnopqcadb"))  # False