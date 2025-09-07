x = 12345
y = 0
while x != 0:
    y = y * 10 + x % 10
    x //= 10
print(y)
