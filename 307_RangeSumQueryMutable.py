class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.presum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.presum[i + 1] = self.presum[i] + nums[i]
        print(self.presum)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        for i in range(index + 1, len(self.presum)):
            self.presum[i] += diff
        print(self.presum)

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right + 1] - self.presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Your NumArray object will be instantiated and called as such:
obj = NumArray([1, 3, 5])
obj.update(1, 2)
param_2 = obj.sumRange(0, 2)
print(param_2)
