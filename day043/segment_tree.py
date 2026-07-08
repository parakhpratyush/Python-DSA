class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        # Leaf nodes fill karo
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        # Internal nodes build karo
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def update(self, i, val):
        # Leaf node update karo
        i += self.n
        self.tree[i] = val
        # Upar tak propagate karo
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def query(self, left, right):
        # [left, right) range ka sum
        result = 0
        left += self.n
        right += self.n
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