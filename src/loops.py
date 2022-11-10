
# While - loop with else and continue
i = 0
while i < 6:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
else:
    print("In Else Block")
print("End Of Loop")



# For - loop over list elements
primes = [2,3,5,7]
for prime in primes:
    print(prime)

nums = (1,2,3)
print("Loop through tuple")
for n in nums:
    print(n)

# For - loop with range (0-4)
print("Loop with Range")
for i in range(5):
    print(i)

# For - loop over set elements
print("Loop over set elements")
z = {1, 2, 3}
for a in z:
    print(a)

# While - loop over tuple elements with while
print("Loop over set elements using while")
y = (4, 5, 6)
wi = 0
while wi < len(y):
    print(y[wi])
    wi += 1

# For - loop over dictionary
print("Loop over dictionary")
lookup = {'key1': 1974, 'key2': 1978, 'key3': 2016, 'key4': 2019}
for key in lookup:
    print(key, lookup[key])





