# Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
# read the CSV file and display the content.

f = open("New.csv", "a")
import json

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("New.csv", "r")
print(f.read())
