def first_true(nums):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid]:  # Trueならもっと左へ
            r = mid
        else:          # Falseならもっと右へ
            l = mid + 1
    return l if l < len(nums) else -1

nums = [False, False, True, True, True, True]
print(first_true(nums))  # 3

nums = [False, False, False, False]
print(first_true(nums))  # -1 (Trueがない場合)

nums = [True, True, True, True]
print(first_true(nums))  # 0 (最初からTrueの場合)
