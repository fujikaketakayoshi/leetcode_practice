class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        i, j, k = 0, 0, 0
        n = len(nums)
        while i < n - 2:
            j = i + 1
            while j < n - 1:
                # print(i, j)
                if nums[i] >= nums[j]:
                    break
                k = j + 1
                while k < n:
                    # print(i,j,k)
                    if nums[i] < nums[j] < nums[k]:
                        return True
                    if nums[j] >= nums[k] and nums[k] < nums[i]:
                        i = k
                        j = i + 1
                        break
                    if nums[j] >= nums[k] and nums[k] > nums[i]:
                        j = k
                        k += 1
                        continue
                    k += 1
                if k == n:
                    return False
                j += 1
            if j == n - 1:
                return False
            i += 1
        return False