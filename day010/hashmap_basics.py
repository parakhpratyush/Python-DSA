# Creating
freq = {}
freq = dict()

# Inserting
freq["a"] = 1
freq["b"] = 2

# Safe insertion — don't overwrite if exists
freq.setdefault("a", 0)  # keeps existing value
freq.setdefault("c", 0)  # adds c:0 since c didn't exist

# Increment pattern — most common in DSA
s = "aabbccaaa"
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
print(count)  # {'a': 5, 'b': 2, 'c': 2}

# Checking existence
if "a" in count:
    print("a exists:", count["a"])

# Iterating
for key, value in count.items():
    print(f"{key}: {value}")

for key in count.keys():
    print(key)

for value in count.values():
    print(value)

# Deleting
del count["b"]
popped = count.pop("c", None)  # None = default if key missing
print(count)

# Most common pattern — Counter
from collections import Counter
s = "aabbccaaa"
c = Counter(s)
print(c)                    # Counter({'a': 5, 'b': 2, 'c': 2})
print(c.most_common(2))     # [('a', 5), ('b', 2)] — top 2

# DefaultDict — never get KeyError
from collections import defaultdict
graph = defaultdict(list)
graph[1].append(2)
graph[1].append(3)
graph[2].append(4)
print(graph)  # {1: [2, 3], 2: [4]}