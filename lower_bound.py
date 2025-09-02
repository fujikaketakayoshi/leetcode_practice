def lower_bound(nums, x):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        print(mid, l, r)
        if nums[mid] >= x:
            r = mid   # 条件を満たす → もっと左にあるかも
        else:
            l = mid + 1   # 条件を満たさない → 右へ
    return l



nums = [1, 1, 3, 3, 5, 7, 9]
x = 4
result = lower_bound(nums, x)
print(result)
x = 3
result = lower_bound(nums, x)
print(result)  
x = 10
result = lower_bound(nums, x)
print(result)