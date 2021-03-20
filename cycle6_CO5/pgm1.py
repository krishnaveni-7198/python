# Write a Python program to read a file line by line and store it into a list.

f = open("demofile", "r")
list1 = []
for x in f:
    # print(x)

    list1.append(x)
