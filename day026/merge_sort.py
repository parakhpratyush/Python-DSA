class Solution():
    def merge_sort(self,arr): #sort the array withot using inbuilt arr.sort() or sorted(arr)
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left_sorted = self.merge_sort(left)
        right_sorted = self.merge_sort(right)
        return self.merge(left_sorted, right_sorted)


    def merge(self,left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
    
        return result

solver=Solution()

print(solver.merge_sort([38,27,43,3,9,82,10]))
