# Python program to copy odd lines of one file to other

f = open("demofile", "r")
list1 = []
for x in f:
    list1.append(x)
c = len(list1)
f1 = open("demo1.txt", "x")
for i in range(0,c,2):
    f1.write(list1[i])
f1.close()
