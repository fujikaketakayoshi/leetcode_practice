def expand_around_center(s: str, left: int, right: int) -> (int, int):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

s = "babaabbaabd"

start, end = 0, 0

for i in range(len(s)):
    print(f"i: {i}")
    # 奇数長回文
    l1, r1 = expand_around_center(s, i, i)
    print(f"  l1: {l1}, r1: {r1}")
    # 偶数長回文
    l2, r2 = expand_around_center(s, i, i + 1)
    print(f"  l2: {l2}, r2: {r2}")
    # 今までの最大より長ければ更新
    if r1 - l1 > end - start:
        start, end = l1, r1
        print(f"  update! start: {start}, end: {end}")
    if r2 - l2 > end - start:
        start, end = l2, r2
        print(f"  update! start: {start}, end: {end}")

print(s[start:end + 1])
