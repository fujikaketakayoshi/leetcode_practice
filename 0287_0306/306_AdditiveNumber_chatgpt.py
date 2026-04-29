class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def dfs(a, b, idx):
            if idx == n:
                return True

            s = str(a + b)

            if not num.startswith(s, idx):
                return False

            return dfs(b, a + b, idx + len(s))

        for i in range(1, n):
            for j in range(i + 1, n):

                first = num[:i]
                second = num[i:j]

                # leading zero禁止
                if len(first) > 1 and first[0] == '0':
                    continue
                if len(second) > 1 and second[0] == '0':
                    continue

                if dfs(int(first), int(second), j):
                    return True

        return False
s = Solution()
print(s.isAdditiveNumber("112358"))
print(s.isAdditiveNumber("199100199"))