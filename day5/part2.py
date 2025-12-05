import os
currentDir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.path.join(currentDir, "sample.txt")
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

originalRanges = []

for line in content.split("\n"):
    if line == '':
        break
    start, end = line.split("-")
    originalRanges.append((int(start), int(end)))

def inRange(num, range):
    start, end = range
    return num >= start and num <= end

def hasOverlap(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return inRange(start1, range2) or inRange(end1, range2) or inRange(start2, range1) or inRange(end2, range1)

def expandRange(range1, range2):
    start = min(range1[0], range2[0])
    end = max(range1[1], range2[1])
    return start, end



def combineRanges(ranges):
    swallowedRanges = set()
    uniqueRanges = []
    for i in range(len(ranges)):
        if i not in swallowedRanges:
            start1, end1 = ranges[i]
            for j in range(i + 1, len(ranges)):
                # print("j: " + str(j), ranges[i], ranges[j])
                if j not in swallowedRanges and hasOverlap((start1, end1), ranges[j]):
                    # print("in range")
                    # print((start1, end1), ranges[j])
                    swallowedRanges.add(j)
                    newStart, newEnd = expandRange((start1, end1), ranges[j])
                    start1 = newStart
                    end1 = newEnd
                    # print('new')
                    # print(start1, end1)
            # print('adding range')
            # print(start1, end1)
            uniqueRanges.append((start1, end1))
    return uniqueRanges

curRanges = originalRanges

while True:
    rangesLength = len(curRanges)
    curRanges = combineRanges(curRanges)
    if len(curRanges) == rangesLength:
        break

# print(curRanges)

freshIngredients = 0
for start, end in curRanges:
    freshIngredients += end - start + 1

print(freshIngredients)