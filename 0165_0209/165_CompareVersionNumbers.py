class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1s = version1.split('.')
        v2s = version2.split('.')
        n1, n2 = len(v1s), len(v2s)
        n = max(n1, n2)
        i = 0
        while i < n:
            if n1 <= i:
                v1 = 0
                v2 = int(v2s[i])
            elif n2 <= i:
                v1 = int(v1s[i])
                v2 = 0
            else:
                v1 = int(v1s[i])
                v2 = int(v2s[i])
            
            if v1 > v2:
                return 1
            elif v2 > v1:
                return -1
            i += 1
        return 0

solution = Solution()
print(solution.compareVersion("1.01", "1.001"))  # Output: 0
print(solution.compareVersion("1.0", "1.0.0"))  # Output: 0
print(solution.compareVersion("0.1", "1.1"))    # Output: -1
print(solution.compareVersion("1.0.1", "1"))    # Output: 1
print(solution.compareVersion("1.0.1", "1.0"))  # Output: 1