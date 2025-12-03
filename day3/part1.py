import os
currentDir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

def maxIndex(s):
   curMax = -1
   maxIndex = 0
   for i in range(len(s)):
      if int(s[i]) > curMax:
         curMax = int(s[i])
         maxIndex = i
   return str(curMax), maxIndex

def maxVoltage(bank):
    firstMax, firstIndex = maxIndex(bank[0:-1])
    secondMax, secondIndex = maxIndex(bank[firstIndex + 1:])
    return int(firstMax + secondMax)

totalVolts = 0

for bank in content.split("\n"):
   totalVolts += maxVoltage(bank)

print(totalVolts)