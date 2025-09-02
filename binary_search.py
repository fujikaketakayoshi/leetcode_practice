def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        print(mid)
        print(l, r)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1   # 右半分へ
        else:
            r = mid - 1   # 左半分へ
    return -1  # 見つからなかった場合

nums = [1, 2, 3, 5, 6, 7, 8, 9, 12, 15, 18, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90]
target = 12
result = binary_search(nums, target)
print(result)
