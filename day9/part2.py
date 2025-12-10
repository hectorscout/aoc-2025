# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(inputFile, "r") as file:
    content = file.read()

vertexes = [tuple(map(int, x.split(','))) for x in content.split('\n')]

# edges = set()
maxX = 0
maxY = 0
for x, y in vertexes:
    maxX = max(maxX, x)
    maxY = max(maxY, y)

segments = []
for i in range(len(vertexes)):
    j = (i + 1) % len(vertexes)
    segments.append((vertexes[i], vertexes[j]))

# def getEdges(vert1, vert2):
    # myEdges = set()
    # x1, y1 = vert1
    # x2, y2 = vert2
    # if (x1 == x2):
        # yRange = [y1, y2]
        # yRange.sort()
        # for y in range(yRange[0] + 1, yRange[1]):
            # myEdges.add((x1, y))
    # else:
        # xRange = [x1, x2]
        # xRange.sort()
        # for x in range(xRange[0] + 1, xRange[1]):
            # myEdges.add((x, y1))
    # return myEdges

# edges = getEdges(vertexes[0], vertexes[-1])
# for i in range(len(vertexes) - 1):
    # edges = edges.union(getEdges(vertexes[i], vertexes[i + 1]))

def rectArea(point1, point2):
    return abs(point1[0] - point2[0] + 1) * abs(point1[1] - point2[1] + 1)

def pointIsOnEdge(point):
    x, y = point
    for point1, point2 in segments:
        x1, y1 = point1
        x2, y2 = point2
        if x1 == x2 == x and (y1 >= y >= y2 or y1 <= y <=y2):
            return True
    return False

# TODO: handle exiting through a vertex?
def pointIsInPoly(point):
    # print(point)
    if pointIsOnEdge(point) or point in vertexes:
        return True
    inside = False
    # crossings = 0
    x, y = point
    for point1, point2 in segments:
        x1, y1 = point1
        x2, y2 = point2
        if y2 - y1 and segmentsCross((point1, point2), (point, (maxX, y))):
            inside = not inside
        # if y1 > y != y2 > y and y2 - y1:
            # xIntersect = ( (y - y1) * (x2 - x1) ) / (y2 - y1) + x1
            # if x < xIntersect:
                # inside = not inside
    return inside
        
    # x += 1
    # y += 1
    # while 0 <= x <= maxX and 0 <= y <= maxY:
        # if pointIsOnEdge(x, y):
            # crossings += 1
        # x += 1
        # y += 1
    # print("crossings", crossings)
    # return crossings % 2 == 1

def numBetween(n, x1, x2):
    return x1 <= n <= x2 or x1 >= n >= x2

def segmentsCross(seg1, seg2):
    pointI, pointJ = seg1
    xi, yi = pointI
    xj, yj = pointJ
    point1, point2 = seg2
    x1, y1 = point1
    x2, y2 = point2

    if xi == xj and y1 == y2 and numBetween(xi, x1, x2) and numBetween(y1, yi, yj):
        return True
    elif yi == yj and x1 == x2 and numBetween(yi, y1, y2) and numBetween(x1, xi, xj):
        return True
    return False


    # if xi == xj:
    #     for vertPoint1, vertPoint2 in vertEdges:
    #         vpx1, vpy1 = vertPoint1
    #         vpx2, vpy2 = vertPoint2
    #         if (vpx1 >= xi >= vpx2 or vpx1 <= xi <= vpx2) and (yi >= vpy1 >= yj or yi <= vpy1 <= yj):
    #             return False
    # else:                
    #     for horizPoint1, horizPoint2 in horizEdges:
    #         hpx1, hpy1 = horizPoint1
    #         hpx2, hpy2 = horizPoint2
    #         if (hpy1 >= yi >= hpy2 or hpy1 <= yi <= hpy2) and (xi >= hpx1 >= xj or xi <= hpx1 <= xj):
    #             return False


def rectIsInPoly(vert1, vert2):
    x1, y1 = vert1
    x2, y2 = vert2
    if not pointIsInPoly((x1, y2)) or not pointIsInPoly((x2, y1)):
        # print('points not in poly')
        return False

    vertEdges = [((x1, y1), (x1, y2)), ((x2, y1), (x2, y2))]
    horizEdges = [((x1, y1), (x2, y1)), ((x1, y2), (x2, y2))]

    for pointI, pointJ in segments:
        xi, yi = pointI
        xj, yj = pointJ
        if xi == xj:
            for vertPoint1, vertPoint2 in vertEdges:
                if segmentsCross((pointI, pointJ), (vertPoint1, vertPoint2)):
                    # print("vert crossed")
                    # print((pointI, pointJ), (vertPoint1, vertPoint2))
                    return False
                # vpx1, vpy1 = vertPoint1
                # vpx2, vpy2 = vertPoint2
                # if (vpx1 >= xi >= vpx2 or vpx1 <= xi <= vpx2) and (yi >= vpy1 >= yj or yi <= vpy1 <= yj):
                #     return False
        else:                
            for horizPoint1, horizPoint2 in horizEdges:
                if segmentsCross((pointI, pointJ), (horizPoint1, horizPoint2)):
                    # print("horiz crossed")
                    # print((pointI, pointJ), (horizPoint1, horizPoint2))
                    return False
                # hpx1, hpy1 = horizPoint1
                # hpx2, hpy2 = horizPoint2
                # if (hpy1 >= yi >= hpy2 or hpy1 <= yi <= hpy2) and (xi >= hpx1 >= xj or xi <= hpx1 <= xj):
                #     return False
    return True


    # myEdges = getEdges(point1, (x1, y2))
    # myEdges = myEdges.union(point2, (x1, y2))
    # myEdges = myEdges.union(point2, (x2, y1))
    # myEdges = myEdges.union(point1, (x2, y1))
    # return len(myEdges.intersection(edges)) == 0

# print(rectIsInPoly((9,5), (2,3)))

maxArea = 0
for i in range(len(vertexes) - 1):
    for j in range(i + 1, len(vertexes)):
        myRectArea = rectArea(vertexes[i], vertexes[j])
        # print(vertexes[i], vertexes[j], myRectArea, rectIsInPoly(vertexes[i], vertexes[j]))
        if myRectArea > maxArea and rectIsInPoly(vertexes[i], vertexes[j]):
            maxArea = myRectArea


# print(edges)
# print(len(edges))
print(maxArea)