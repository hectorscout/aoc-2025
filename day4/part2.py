import os
currentDir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.path.join(currentDir, "sample.txt")
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

rows = content.split("\n")

def rollIsFree(i, j):
    if rows[i][j] != "@":
        return False
    count = 0
    down = i + 1
    up = i - 1
    left = j - 1
    right = j + 1
    if up >= 0 and left >=0 and rows[up][left] == "@":
        count += 1
    if up >= 0 and rows[up][j] == "@":
        count += 1
    if up >= 0 and right < len(rows[i]) and rows[up][right] == "@":
        count += 1
    if left >=0 and rows[i][left] == "@":
        count += 1
    if left >=0 and down < len(rows) and rows[down][left] == "@":
        count += 1
    if down < len(rows) and rows[down][j] == "@":
        count += 1
    if down < len(rows) and right < len(rows[i]) and rows[down][right] == "@":
        count += 1
    if right < len(rows[i]) and rows[i][right] == "@":
        count += 1

    return count < 4
        
freeRolls = 0

def removeRolls():
    rollsToRemove = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rollIsFree(i, j):
                rollsToRemove.append((i,j))
    for i, j in rollsToRemove:
        rows[i] = rows[i][:j] + '.' + rows[i][j+1:]
    return len(rollsToRemove)

while True:
    removed = removeRolls()
    freeRolls += removed
    if removed == 0:
        break

print(freeRolls)