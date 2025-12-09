inputFile = "sample.txt"
# inputFile = "input1.txt"
with open(inputFile, "r") as file:
    content = file.read()

tiles = [tuple(map(int, x.split(','))) for x in content.split('\n')]

def rectArea(point1, point2):
    return abs(point1[0] - point2[0] + 1) * abs(point1[1] - point2[1] + 1)

maxArea = 0
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        # print(tiles[i], tiles[j], rectArea(tiles[i], tiles[j]))
        maxArea = max(maxArea, rectArea(tiles[i], tiles[j]))


print(maxArea)