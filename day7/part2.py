## I think this would have gotten the answer, but waaayyy too slow...
import os
# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

rows = [list(row) for row in content.split("\n")]
numRows = len(rows)
width = len(rows[0])

print(width)

timelines = 0
def getTimelines(depth, i):
    myTimelines = 0
    if depth >= numRows:
        print("ended", i)
        return 1
    if rows[depth][i] == '^':
        myTimelines += getTimelines(depth + 1, i - 1)
        myTimelines += getTimelines(depth + 1, i + 1)
    else:
        myTimelines += getTimelines(depth + 1, i)
    print(myTimelines, depth)
    return myTimelines

timelines = getTimelines(1, rows[0].index("S"))

print(timelines)