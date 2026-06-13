import heapq

# MIN HEAP
# heapq hamesha MIN heap hai Python mein
nums = [5, 3, 8, 1, 9, 2, 7]

# List ko heap mein convert karo — O(n)
# Ye array ko in-place restructure karta hai heap property follow karne ke liye
heapq.heapify(nums)
print("Min heap array:", nums)  # [1, 3, 2, 5, 9, 8, 7]
# Note: ye sorted nahi hai, bas heap property follow karta hai

# Sabse chota element dekhna — O(1)
print("Minimum:", nums[0])  # 1 — hamesha index 0 pe hoga

# Naya element add karna — O(log n)
# heappush element ko sahi jagah pe insert karta hai heap property maintain karte hue
heapq.heappush(nums, 4)
print("After pushing 4:", nums)

# Sabse chota element nikalna — O(log n)
# heappop root nikalta hai, phir heap restructure hoti hai
smallest = heapq.heappop(nums)
print("Popped minimum:", smallest)  # 1
print("Heap after pop:", nums)

# MAX HEAP — Python mein trick use karni padti hai
# Negative sign lagao — chota negative = bada original number
max_heap = []
for num in [5, 3, 8, 1, 9, 2, 7]:
    heapq.heappush(max_heap, -num)  # -9, -8, -7... store hoga

# Sabse bada element nikalna
largest = -heapq.heappop(max_heap)  # negative wapas karo
print("Maximum:", largest)  # 9

# N LARGEST / N SMALLEST — built in functions
original = [5, 3, 8, 1, 9, 2, 7, 4, 6]
print("3 largest:", heapq.nlargest(3, original))   # [9, 8, 7]
print("3 smallest:", heapq.nsmallest(3, original)) # [1, 2, 3]