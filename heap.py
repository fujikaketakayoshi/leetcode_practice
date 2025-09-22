import heapq

lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

# 各リストの先頭を (値, リスト番号, インデックス) でヒープに入れる
heap = []
for i, lst in enumerate(lists):
    if lst:  # 空リストはスキップ
        heapq.heappush(heap, (lst[0], i, 0))

result = []

while heap:
    print(heap)
    val, li, idx = heapq.heappop(heap)
    result.append(val)

    # 取り出した要素の次があれば push
    if idx + 1 < len(lists[li]):
        next_val = lists[li][idx + 1]
        heapq.heappush(heap, (next_val, li, idx + 1))

print(result)  # => [1, 1, 2, 3, 4, 4, 5, 6]
