#!/usr/bin/python3

for i in range(10):
    
    j = i + 1
    while  j < 10:
        if (i != 0 or j != 1):
            print(", ", end = "")
        print("{}{}".format(i, j), end = "")
        j += 1
print("\n")
