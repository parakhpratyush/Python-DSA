#for loop
for i in range(5):
    print(i,end="\t")

print("\n----------")

#while loop
n=0
while n<5:
    print(n,end="\t")
    n+=1

print("\n----------")

#nested loop
for i in range(3):
    for j in range(3):
        print(i," ",j)

print("\n----------")

#break
for i in range(10):
    if i==5:
        break
    print(i,end="\t")

print("\n----------")

#continue
for i in range(10):
    if i%2==0:
        continue
    print(i,end="\t")  
    