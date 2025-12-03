import os
currentDir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

curVal = 50
numZeros = 0

for line in content.split("\n"):
    if line[0] == "R":
        curVal += int(line.removeprefix("R"))
    else:
        curVal -= int(line.removeprefix("L"))

    if not (curVal % 100):
        numZeros += 1

print(numZeros)
