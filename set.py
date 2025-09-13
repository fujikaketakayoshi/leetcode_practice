# 空の集合を作成
seen = set()

# 要素を追加
seen.add("a")
seen.add("a")
seen.add("b")
print(seen)   # {'a', 'b'}

# 要素を削除
seen.remove("a")
print(seen)   # {'b'}

# 要素が含まれるか調べる
print("b" in seen)  # True
print("c" in seen)  # False
print(len(seen))  # 1

seen2 = set()
lst1 = [-1, 0, 1]
lst2 = [-1, -1, 2]
seen2.add(tuple(lst1))
seen2.add(tuple(lst1))
seen2.add(tuple(lst2))
print(seen2)
for i in seen2:
    lst = list(i)
    print(lst)
