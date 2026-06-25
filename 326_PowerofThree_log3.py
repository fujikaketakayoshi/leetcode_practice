import math

print(math.log(2 ** 31 - 1, 3))

n = 0
MAX = 2 ** 31 - 1
while True:
    if 3 ** n > MAX:
        break
    print(n, 3 ** n)
    n += 1