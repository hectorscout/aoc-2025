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
        curDir = 1
        curRange = range(int(line.removeprefix("R")))
    else:
        curRange = range(int(line.removeprefix("L")))
        curDir = -1

    for i in curRange:
        curVal += curDir
        if not (curVal % 100):
            numZeros += 1

print(numZeros)
