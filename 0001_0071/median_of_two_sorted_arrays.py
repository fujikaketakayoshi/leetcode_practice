def findMedianSortedArrays(nums1: list, nums2: list):
    nums = nums1 + nums2
    n = len(nums)
    nums.sort()
    mod = n % 2
    if mod == 1:
        i = n // 2
        return format(nums[i], ".5f")
    else:
        i = n // 2
        fnum = (nums[i] + nums[i - 1]) / 2
        return format(fnum, ".5f")

def findMedianSortedArrays2(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2
    
    l, r = 0, m
    while True:
        i = (l + r) // 2  # nums1の分割
        j = half - i      # nums2の分割
        
        Aleft  = nums1[i-1] if i > 0 else float("-inf")
        Aright = nums1[i]   if i < m else float("inf")
        Bleft  = nums2[j-1] if j > 0 else float("-inf")
        Bright = nums2[j]   if j < n else float("inf")
        
        # 左の最大値 <= 右の最小値 なら中央値をまたいでいる
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:  # 奇数
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

nums1 = [1, 2, 5]
nums2 = [3, 4, 6]

print(findMedianSortedArrays(nums1, nums2))
print(findMedianSortedArrays2(nums1, nums2))
