import sys
import fileinput

# Input - Using sys.stdin
for line in sys.stdin:
    if "exit" == line.rstrip():
        break
    print(line)

# Input - Using input function
data = input("What's up? ")
print(data)

# Input - Using fileinput module
for mydata in fileinput.input():
    if "exit" == mydata.rstrip():
        break
    print(mydata)