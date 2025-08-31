def dict_ver(s:str) -> int:
    last_seen = {}   # 文字 -> インデックス
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            # 重複が出たので、左ポインタを更新
            left = last_seen[ch] + 1
        # 今見た文字の位置を更新
        last_seen[ch] = right
        # 最大長を更新
        max_len = max(max_len, right - left + 1)
    return max_len

def set_ver(s:str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        while ch in seen:
            # 重複が出たので、左ポインタを右に動かす
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        max_len = max(max_len, right - left + 1)
    return max_len

s = "abcabcbbefgissgaisgasoigjsaj"

print(dict_ver(s))
print(set_ver(s))
