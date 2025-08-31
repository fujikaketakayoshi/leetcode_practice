nums = [0, 12, 34, 9]
target = 21
seen = {}
for i, num in enumerate(nums):
    print(i, num)
    complement = target - num  # ペアになるべき相手
    if complement in seen:     # すでに見たことがあれば答え
        print([seen[complement], i], 'goal!')
    seen[num] = i
    print(seen)


s = 'abcdef'
for i, ch in enumerate(s):
    print(i, ch)
