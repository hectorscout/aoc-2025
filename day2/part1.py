import os
currentDir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

def isInvalid(id):
   n = len(id)
   return id[0:n//2] == id[n//2:]

sum = 0

for curRange in content.split(","):
   start, end = curRange.split("-")
   for id in range(int(start), int(end)+1):
      if isInvalid(str(id)):
        sum += id

print(sum) 