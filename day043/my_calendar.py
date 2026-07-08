class MyCalendar(object):

    def __init__(self):
        # Sorted list of (start, end) events
        self.events = []

    def book(self, start, end):
        # Binary search se insert position dhundho
        lo, hi = 0, len(self.events)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.events[mid][0] < start:
                lo = mid + 1
            else:
                hi = mid
        
        # Overlap check karo — left neighbor aur right neighbor
        if lo > 0 and self.events[lo-1][1] > start:
            return False
        if lo < len(self.events) and self.events[lo][0] < end:
            return False
        
        self.events.insert(lo, (start, end))
        return True

#----Testing----
solver = MyCalendar()
print(solver.book(10, 20))   # True
print(solver.book(15, 25))   # False (overlap)
print(solver.book(20, 30))   # True