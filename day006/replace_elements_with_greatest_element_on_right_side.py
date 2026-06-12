# WORKS BUT REACHED TIME LIMIT(TLE)
class Solution(object):
    def replaceElements(arr):
        c_max=0
        f_max=0
        for i in range(1,len(arr)):
            c_max=max(arr[i::])
            if c_max>f_max:
                f_max=c_max
                c_max=0
                arr[i-1]=f_max
                f_max=0
        arr[len(arr)-1]=-1    
        return arr
    
print(Solution.replaceElements([400]))
print(Solution.replaceElements([17,18,5,4,6,1]))


#TIME COMPLEXITY O(N)
class Solution(object):
    def replaceElements(arr):
        max_from_right = -1
        for i in range(len(arr) - 1, -1, -1):
            current_val = arr[i]
            arr[i] = max_from_right
            if current_val > max_from_right:
                max_from_right = current_val
        return arr
print(Solution.replaceElements([400]))
print(Solution.replaceElements([17,18,5,4,6,1]))