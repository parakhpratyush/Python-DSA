import bisect

class TimeMap(object):

    def __init__(self):
        # Map each key to a list of lists/tuples: [timestamp, value]
        self.store = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        # Timestamps are strictly increasing, so appending maintains sorted order
        self.store[key].append([timestamp, value])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""
        
        values = self.store[key]
        
        # Binary search for the right insertion point for the target timestamp
        # bisect_right uses a key function or directly compares list elements
        # Since each element is [timestamp, value], comparing with [timestamp, chr(127)] 
        # allows us to find the element efficiently.
        idx = bisect.bisect_right(values, [timestamp, chr(127)])
        
        # If idx is 0, it means all stored timestamps are strictly greater than the requested timestamp
        if idx == 0:
            return ""
        
        # Otherwise, the correct element is at index idx - 1
        return values[idx - 1][1]
