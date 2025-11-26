def isMatch(s: str, p: str) -> bool:
    memo = {}  # (i, j) → True/False をキャッシュ

    def dp(i, j):
        print(i, j)
        # 既に計算済みなら返す
        if (i, j) in memo:
            return memo[(i, j)]

        # パターンが尽きた場合
        if j == len(p):
            ans = (i == len(s))

        else:
            # 1文字目がマッチするかどうか
            first_match = i < len(s) and (p[j] in {s[i], '.'})

            if j + 1 < len(p) and p[j+1] == '*':
                # '*' がある場合 → 0回使う or 1回以上使う
                ans = dp(i, j+2) or (first_match and dp(i+1, j))
            else:
                # 普通の1文字マッチ
                ans = first_match and dp(i+1, j+1)

        # 計算結果をキャッシュに保存
        memo[(i, j)] = ans
        print(memo)
        return ans

    return dp(0, 0)

print(isMatch('aaa', 'aa*'))
