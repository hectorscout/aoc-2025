# I'm pretty sure there's still some edge case(s) in here, but not the ones that are in my input...
# inputFile = "sample.txt"
# inputFile = "sample40.txt"
# inputFile = "sample35.txt"
inputFile = "input1.txt"
with open(inputFile, "r") as file:
    content = file.read()

vertexes = [tuple(map(int, x.split(','))) for x in content.split('\n')]

horizEdges = {}
vertEdges = {}

for i in range(len(vertexes)):
    j = (i + 1) % len(vertexes)
    x1, y1 = vertexes[i]
    x2, y2 = vertexes[j]

    if x1 == x2:
        if x1 not in vertEdges:
            vertEdges[x1] = []
        vertEdges[x1].append((y1, y2) if y1 > y2 else (y2, y1))
    else:
        if y1 not in horizEdges:
            horizEdges[y1] = []
        horizEdges[y1].append((x1, x2) if x1 > x2 else (x2, x1))

vertEdgeIndexes = list(vertEdges.keys())
vertEdgeIndexes.sort()

horizEdgeIndexes = list(horizEdges.keys())
horizEdgeIndexes.sort()

def pointIsInPoly(point):
    if point in vertexes:
        return True
    x, y = point
    count = 0
    for i in vertEdgeIndexes:
        for edge in vertEdges[i]:
            y1, y2 = edge
            if y1 > y >= y2:
                if i == x:
                    return True
                count += 1
        if i >= x:
            break
    return count % 2

def segmentsCross(segment, isVert):
    point1, point2 = segment
    x1, y1 = point1
    x2, y2 = point2
    j = x1 if isVert else y1
    seg = [y1, y2] if isVert else [x1, x2]
    seg.sort()

    edges = horizEdges if isVert else vertEdges
    indexes = horizEdgeIndexes if isVert else vertEdges

    for i in indexes:
        for edge in edges[i]:
            seg1, seg2 = edge
            if seg1 > j > seg2 and seg[0] < i < seg[1]:
                return True
    return False

def rectIsInPoly(corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2
    corner3 = (x1, y2)
    corner4 = (x2, y1)
    vert1 = (corner1, corner3)
    vert2 = (corner2, corner4)
    horiz1 = (corner1, corner4)
    horiz2 = (corner2, corner3)
    if not (pointIsInPoly(corner3) and pointIsInPoly(corner4)):
        return False
    
    crosses = segmentsCross(vert1, True) or segmentsCross(vert2, True) or segmentsCross(horiz1, False) or segmentsCross(horiz2, False)
    return not crosses


def rectArea(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

maxArea = 0
for i in range(len(vertexes) - 1):
    for j in range(i + 1, len(vertexes)):
        myRectArea = rectArea(vertexes[i], vertexes[j])
        if myRectArea > maxArea and rectIsInPoly(vertexes[i], vertexes[j]):
            rect = (vertexes[i], vertexes[j])
            maxArea = myRectArea

print(maxArea)

# 274821960
# 758272366
# 758272366 too low...
# 348836928
# 1194694596
# 1292238828
# 1516897893
# 4605403304 too high...

# 4605538168 even higher...