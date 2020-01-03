#Create a new empty set
x = set()
print(x)
#Create a non empty set
n = set([0, 1, 2, 3, 4])
print(n)

for num in n:
    print(num)

n.add(5)

print(n)

n.remove(5)

print(n)

n.update([5,6,7])

print(n)

n.discard(9)

print(n)

n.discard(5)

print(n)


