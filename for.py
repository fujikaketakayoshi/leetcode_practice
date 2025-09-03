nums = [1,2,3,4,5]
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        print (i, j)

for i in range(n, 0, -1):
    print(i)

for i in range(4,7):
    print(i)

for i in list(range(4,7)):
    print(i)


str = "abcdef"
for i in range(len(str)):
    print(i, str[i])
