import math
import os
# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

points = [tuple(map(int, x.split(","))) for x in content.split('\n')]

def getDistance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt(((x1 - x2) **2) + ((y1 - y2) **2) + ((z1 - z2) **2))

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append((points[i], points[j], getDistance(points[i], points[j])))

def distanceSorter(e):
    return e[2]

distances.sort(key=distanceSorter)

pointGraph = {}
for point1, point2, distance in distances[:1000]:
    if not point1 in pointGraph:
        pointGraph[point1] = []
    if not point2 in pointGraph:
        pointGraph[point2] = []
    pointGraph[point1].append(point2)
    pointGraph[point2].append(point1)
    
visitedPoints = {}

def getGraphNodeCount(point):  
    if point in visitedPoints:
        return 0
    visitedPoints[point] = True
    count = 1
    if not point in pointGraph:
        return count
    for edge in pointGraph[point]:
        count += getGraphNodeCount(edge)
    return count

graphs = []
for point, edges in pointGraph.items():
    if point in visitedPoints:
        continue
    graphs.append(getGraphNodeCount(point))

graphs.sort(reverse=True)
print(math.prod(graphs[:3]))
