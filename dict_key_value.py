my_dict = {"apple": 100, "banana": 200, "orange": 150}

for value in my_dict.values():
    print(value)

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(f"キー: {key}, バリュー: {value}")

del my_dict["banana"]
print(my_dict)

popped = my_dict.pop("orange")
print(f"Popped value: {popped}")
print(my_dict)

my_dict["grape"] = 180
print(my_dict)
apple = my_dict.get("apple", 20)
print(apple)
print(my_dict.get("napple", 20))