# 空の集合を作成
seen = set()

# 要素を追加
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