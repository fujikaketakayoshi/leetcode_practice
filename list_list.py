list = [[], [], []]
print(list)

lists = [[] for _ in range(5)]
print(lists)

lists[0].append(1)
lists[1].append(2)
lists[2].append(3)
print(lists)

lists[5].append(4)
print(lists)
