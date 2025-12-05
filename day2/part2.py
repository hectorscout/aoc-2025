import os
currentDir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

def stringChunks(s, chunkLength):
   return [s[i:i + chunkLength] for i in range(0, len(s), chunkLength)]

def isInvalid(id):
   for i in range(1, (len(id)//2) + 1):
      if len(set(stringChunks(str(id), i))) == 1:
         return True
   return False

sum = 0
for curRange in content.split(","):
   start, end = map(int, curRange.split("-"))
   for id in range(start, end+1):
      if isInvalid(str(id)):
        sum += id

print(sum) 