import os
# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

rows = [list(row) for row in content.split("\n")]
width = len(rows[0])

beamCounts = [0] * width

for i in range(width):
    if rows[0][i] == "S":
        rows[1][i] = '|'
        beamCounts[i] = 1
for i in range(2, len(rows)):
    for j in range(width):
        if rows[i-1][j] == '|':
            if rows[i][j] == '^':
                beamCounts[j-1] += beamCounts[j]
                beamCounts[j+1] += beamCounts[j]
                beamCounts[j] = 0
                rows[i][j-1] = '|'
                rows[i][j+1] = '|'
            else:
                rows[i][j] = '|'

print(sum(beamCounts))