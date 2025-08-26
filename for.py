nums = [1,2,3,4,5]
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        print (i, j)

for i in range(len(nums), 0, -1):
    print(i)