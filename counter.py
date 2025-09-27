from collections import Counter

words = ["foo", "foo", "bar"]
words_counter = Counter(words)
print(words_counter)
print(words_counter.most_common(1)) # 出現頻度が最も高い要素とその数をタプルで返す
print(words_counter['foo'])
print(words_counter['bar'])
print(words_counter['baz'])  # 存在しないキーは0を返す
words_counter['foo'] += 1
print(words_counter)
words_counter['bar'] += 2
print(words_counter)
print(words_counter.most_common(1)) # 出現頻度が最も高い要素とその数をタプルで返すが、同数の場合はどちらか
