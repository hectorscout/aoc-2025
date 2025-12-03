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
   return curMax, maxIndex

def maxVoltage(bank, depth):
    if depth == -1:
       return 0
    
    subBank = bank if depth == 0 else bank[0:(-1 * depth)]

    myMax, myIndex = maxIndex(subBank)
    myVoltage = myMax * (10 ** depth)
    return myVoltage + maxVoltage(bank[myIndex + 1:], depth - 1)

totalVolts = 0

for bank in content.split("\n"):
   totalVolts += maxVoltage(bank, 11)

print(totalVolts)