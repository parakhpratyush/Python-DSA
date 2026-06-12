s = "  Hello World  "

# Case operations
print(s.upper())
print(s.lower())
print(s.title())

# Cleaning
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Searching
print(s.find("World"))
print(s.count("l"))
print(s.startswith("  Hello"))
print(s.endswith("  "))

# Replacing
print(s.replace("World", "sir"))

# Splitting
sentence = "I am going to college"
words = sentence.split(" ")
print(words)
print(len(words))

# Joining (opposite of split)
joined = "-".join(words)
print(joined)

# Checking content
print("hello123".isalnum())
print("hello".isalpha())
print("123".isdigit())
print(" ".isspace())