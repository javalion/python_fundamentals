
x = 5
y = 3
if x == 5:
    print("x==5")
elif y == 3:
    print("x!=5 AND y==3")
else:
    print("x!=5")

print("x==5" if (x==5) else "x!=5")

print(x==5 and y==3)
print(x!=5 or y==3)

print("xyz" in ["abc", "def"])

print([1,2,3] is [1,2,3])

lst = [1, 2, 3]
print(lst is lst)
print(not lst is lst)