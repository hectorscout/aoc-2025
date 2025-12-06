import math
import os
inputFile = "input1.txt"
# inputFile = "sample.txt")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

rows = [line.split() for line in content.split('\n')]

total = 0
for i in range(len(rows[0])):
    nums = [int(rows[j][i]) for j in range(len(rows) -1)]
    if rows[-1][i] == "*":
        total += math.prod(nums)
    else:
        total += sum(nums)

print(total)