# Writing to file
with open("notes.txt", "w") as f:
    f.write("Day 8 of coding journey\n")
    f.write("Learning file handling\n")

# Reading from file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# Appending
with open("notes.txt", "a") as f:
    f.write("This is appended text\n")

# Reading line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())