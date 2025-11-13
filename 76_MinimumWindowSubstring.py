class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        if ns < nt:
            return ''

        lt = list(t)
        elt = []
        i = 0
        tmp_str = ''
        results = []
        while i < ns:
            if s[i] in lt:
                lt.remove(s[i])
                elt.append(s[i])
                tmp_str = s[i]
                j = i + 1
                if len(lt) == 0:
                    results.append(tmp_str)
                    tmp_str = ''
                    lt = list(t)
                    elt =[]
                    j = i
                    break
                while j < ns:
                    tmp_str += s[j]
                    if not s[j] in lt and s[j] in elt:
                        tmp_str = ''
                        j = i
                        lt = list(t)
                        elt =[]
                        break
                    if s[j] in lt:
                        lt.remove(s[j])
                        elt.append(s[j])
                    if len(lt) == 0:
                        results.append(tmp_str)
                        tmp_str = ''
                        lt = list(t)
                        elt =[]
                        j = i
                        break
                    j += 1
            i += 1
        
        min_str_len = 10 ^ 5 + 1
        min_str = ''
        for i in results:
            if len(i) < min_str_len:
                min_str_len = len(i)
                min_str = i
        return min_str

solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t))  # 出力: "BANC"
s = "a"
t = "a"
print(solution.minWindow(s, t))  # 出力: "a"
s = "a"
t = "aa"
print(solution.minWindow(s, t))  # 出力: ""
s = "ab"
t = "b"
print(solution.minWindow(s, t))  # 出力: "b"
s = "aaflslflsldkalskaaa"
t = "aaa"
print(solution.minWindow(s, t))  # 出力: "aaa" "a"で正しくない
