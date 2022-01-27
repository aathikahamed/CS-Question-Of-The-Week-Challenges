# Bronze
import json

with open("example_bronze.json", "r") as content:
    data = json.load(content)

s = ''

for i in data:
    a = 0
    for x in i:
        a += x
    s += str(a)
print(s)
