class NumArray(object):

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2*index] + self.tree[2*index+1]

    def sumRange(self, left, right):
        left += self.n
        right += self.n + 1
        result = 0
        while left < right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

#----Testing----
solver = NumArray([1, 3, 5])
print(solver.sumRange(0, 2))   # 9
solver.update(1, 2)
print(solver.sumRange(0, 2))   # 8