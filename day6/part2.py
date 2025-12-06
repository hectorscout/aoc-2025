import math
import os
inputFile = "input1.txt"
# inputFile = "sample.txt")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

rows = content.split('\n')

total = 0
curNumStrs = []
for i in reversed(range(len(rows[0]))):
    curNum = "".join([rows[j][i] for j in range(len(rows) - 1) if rows[j][i] != " "])

    if curNum == "":
        curNumStrs = []
        continue
    curNumStrs.append(int(curNum))
    if rows[-1][i] == "*":
        total += math.prod(curNumStrs)
    elif rows[-1][i] == "+":
        total += sum(curNumStrs)

print(total)
