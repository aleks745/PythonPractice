import random

a = []

for i in range(0,30):
    n = random.randint(-100,100)
    a.append(n)

print(a)
print("max element ", max(a)," and its index ", a.index(max(a))+1)

b = [n for n in a if n%2!=0]
b.sort(reverse = True)
print("Array is converted")
print(b)