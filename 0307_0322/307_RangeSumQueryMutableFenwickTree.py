class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self.add(i + 1, num)
        print(self.bit)

    def add(self, idx, delta):
        print('here', idx, self.bit)
        while idx <= self.n:
            self.bit[idx] += delta
            print(idx, self.bit)
            idx += idx & -idx

    def prefix_sum(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, diff)

    def sumRange(self, left, right):
        return self.prefix_sum(right + 1) - self.prefix_sum(left)

# Your NumArray object will be instantiated and called as such:
obj = NumArray([1, 3, 5, 7, 9, 11])
obj.update(0, 2)
param_2 = obj.sumRange(0, 2)
print(param_2)