arr = [0, 1, 2, 5, 9]

print(arr[2:])
print(arr[:2])
print(arr[1:3])

#arr2 = arr[2:]

for k, v in enumerate(arr[2:]):
    print(k, v)


last = arr.pop()
print(last)
print(arr)

first = arr.pop(0)
print(first)
print(arr)

arr.insert(0, 99)
print(arr)

arr.insert(10, 22)
print(arr)

arr[2:2] = [33, 44, 55]
print(arr)