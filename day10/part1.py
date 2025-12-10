import re
inputFile = "sample.txt"
inputFile = "input1.txt"
with open(inputFile, "r") as file:
    content = file.read()

machines = content.split('\n')

def parseMachine(machine):
    lights = [0 if x == '.' else 1 for x in re.search('\[.*\]', machine)[0].replace('[', '').replace(']', '')]
    buttons = [list(map(int, x.split(','))) for x in re.search('\(.*\)', machine)[0].replace('(', '').replace(')', '').split()]
    # print('lights:', lights, 'buttons:', buttons)
    return lights, buttons

def pushButton(button, lights):
    newLights = [x for x in lights]
    for light in button:
        newLights[light] = (lights[light] + 1) % 2
    return newLights

def isCorrect(lights, lightsGoal, debug=False):
    # if debug:
        # print('checking', lights, lightsGoal)
    for i in range(len(lights)):
        if lights[i] != lightsGoal[i]:
            return False
    return True

def getMachineCount(lightsGoal, buttons):
    cache = []
    for i in range(len(buttons)):
        newLights = pushButton(buttons[i], [0]*len(lightsGoal))
        if isCorrect(newLights, lightsGoal):
            return 1
    for i in range(len(buttons)):
        iLights = pushButton(buttons[i], [0]*len(lightsGoal))
        # print("after one:", lightsGoal, iLights)
        for j in range(len(buttons)):
            jLights = pushButton(buttons[j], iLights)
            if isCorrect(jLights, lightsGoal, True):
                # print(jLights, lightsGoal, 'was correct after 2', i, j)
                return 2
    for k in range(len(buttons)):
        kLights = pushButton(buttons[k], [0]*len(lightsGoal))
        for i in range(len(buttons)):
            iLights = pushButton(buttons[i], kLights)
            for j in range(len(buttons)):
                jLights = pushButton(buttons[j], iLights)
                if isCorrect(jLights, lightsGoal, True):
                    return 3
    for k in range(len(buttons)):
        kLights = pushButton(buttons[k], [0]*len(lightsGoal))
        for l in range(len(buttons)):
            lLights = pushButton(buttons[l], kLights)
            for i in range(len(buttons)):
                iLights = pushButton(buttons[i], lLights)
                for j in range(len(buttons)):
                    jLights = pushButton(buttons[j], iLights)
                    if isCorrect(jLights, lightsGoal, True):
                        return 4
    for k in range(len(buttons)):
        kLights = pushButton(buttons[k], [0]*len(lightsGoal))
        for m in range(len(buttons)):
            mLights = pushButton(buttons[m], kLights)
            for l in range(len(buttons)):
                lLights = pushButton(buttons[l], mLights)
                for i in range(len(buttons)):
                    iLights = pushButton(buttons[i], lLights)
                    for j in range(len(buttons)):
                        jLights = pushButton(buttons[j], iLights)
                        if isCorrect(jLights, lightsGoal, True):
                            return 5
    for k in range(len(buttons)):
        kLights = pushButton(buttons[k], [0]*len(lightsGoal))
        for n in range(len(buttons)):
            nLights = pushButton(buttons[n], kLights)
            for m in range(len(buttons)):
                mLights = pushButton(buttons[m], nLights)
                for l in range(len(buttons)):
                    lLights = pushButton(buttons[l], mLights)
                    for i in range(len(buttons)):
                        iLights = pushButton(buttons[i], lLights)
                        for j in range(len(buttons)):
                            jLights = pushButton(buttons[j], iLights)
                            if isCorrect(jLights, lightsGoal, True):
                                return 6
    for k in range(len(buttons)):
        kLights = pushButton(buttons[k], [0]*len(lightsGoal))
        for p in range(len(buttons)):
            pLights = pushButton(buttons[p], kLights)
            for n in range(len(buttons)):
                nLights = pushButton(buttons[n], pLights)
                for m in range(len(buttons)):
                    mLights = pushButton(buttons[m], nLights)
                    for l in range(len(buttons)):
                        lLights = pushButton(buttons[l], mLights)
                        for i in range(len(buttons)):
                            iLights = pushButton(buttons[i], lLights)
                            for j in range(len(buttons)):
                                jLights = pushButton(buttons[j], iLights)
                                if isCorrect(jLights, lightsGoal, True):
                                    return 7
    return 0
        # print(newLights, isCorrect(newLights, lightsGoal))

sum = 0
shallowCount = 0
for machine in machines:
    lightsGoal, buttons = parseMachine(machine)
    count = getMachineCount(lightsGoal, buttons)
    if count == 0:
        shallowCount += 1
    sum += count
    # while True:
print(sum)
print("missing:", shallowCount)