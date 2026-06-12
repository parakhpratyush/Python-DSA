class Solution(object):
    def dailyTemperatures(temps):
        result = [0] * len(temps)
        stack = []  # stores indices
    
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
    
        return result
    

print(Solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution.dailyTemperatures([30,40,50,60]))
print(Solution.dailyTemperatures([30,60,90]))