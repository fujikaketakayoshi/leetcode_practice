from functools import lru_cache

def isMatch(s: str, p: str) -> bool:
    @lru_cache(None)
    def dp(i, j):
        # s[i:] と p[j:] がマッチするか
        if j == len(p):
            return i == len(s)

        first_match = i < len(s) and (p[j] in {s[i], '.'})

        if j + 1 < len(p) and p[j+1] == '*':
            # * を0回使う or 1回以上使う
            return dp(i, j+2) or (first_match and dp(i+1, j))
        else:
            return first_match and dp(i+1, j+1)

    return dp(0, 0)

print(isMatch('aa', 'a*'))