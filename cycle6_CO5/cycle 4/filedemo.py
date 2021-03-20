#open and read a file

file1 = open("demo.py", "r")
print("file: ",file1)
print()
print(file1.read())
file1.close()

#edit a file

file2 = open("demo.py", "r")
print("file: ", file2)
print("before editing:")
print()
print(file2.read())
print()
print("after editing")
file2 = open("demo.py", "w")
file2.write("file is edited2")
print(file2.read())
