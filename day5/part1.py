import os
currentDir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDir, "sample.txt")
# filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

ranges = []
ingredients = []

doingRanges = True

for line in content.split("\n"):
    if doingRanges:
        if line == '':
            doingRanges = False
        else:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))
    else:
        ingredients.append(int(line))

freshCount = 0

for ingredient in ingredients:
    for start, end in ranges:
        if ingredient >= start and ingredient <= end:
            freshCount += 1
            break

print(freshCount)