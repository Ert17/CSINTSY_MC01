import random

miner = [[1, 1], [1, 2]]
#        pX  pY  fX  fY
#     [0,0][0,1][1,0][1,1]

direction = 1 # 1 - right, 2 - down, 3 - left, 4 - up
gold = []
beacons = []
pits = []
pastCoors = [[1,1]] #array for the coordinates na nadaan na
scanCtr = 0
rotateCtr = 0
moveCtr = 0

# returns 1 if miner will be OOB, else 0
def OOB():
    global miner
    global direction
    global grid

    #Check miner if out of bounds
    if (miner[0][0] == 1 and direction == 4):
        if (miner[0][1] == 1 and direction == 3): #top left
            return 1
        if (miner[0][1] == grid and direction == 1): #top right
            return 1
        return 1
    elif (miner[0][1] == 1 and direction == 3):
        if (miner[1][0] == 1 and direction == 4): # top left
            return 1
        if (miner[1][0] == grid and direction == 2): #bottom left
            return 1
        return 1
    elif (miner[0][0] == grid and direction == 2):
        if (miner[0][1] == 1 and direction == 3): # bottom left
            return 1
        if (miner[0][1] == grid and direction == 1): #bottom right
            return 1
        return 1
    elif (miner[0][1] == grid and direction == 1):
        if (miner[0][0] == 1 and direction == 4): # top right
            return 1
        if (miner[0][0] == grid and direction == 2): #bottom right
            return 1
        return 1

    return 0

def randomLevel():
    print("in randomLevel")
    global miner
    global pastCoors

    for pastCoor in pastCoors:
        if miner[1][0] == pastCoor[0] and miner[1][1] == pastCoor[1]:
            print ("in pastCoor func")
            return 2 #rotate

    # if out of bounds
    bounds = OOB()
    if bounds:
        print("in OOB func")
        return 2 #rotate

    print("Returning Move")
    return 3 #move

def smartLevel():
    act = int(input("Act: "))
    return act

def scan(grid): #Miner picked 1
    global direction
    global miner
    global scanCtr

    scanCtr += 1

    x = miner[0][0]
    y = miner[0][1]

    content = []

    for pit in pits:
        content.append([pit[0],pit[1],"P"])
    for beacon in beacons:
        content.append([beacon[0],beacon[1],"B"])

    content.append([gold[0], gold[1], "G"])

    print("SCAN: x - " + str(x) + " y - " + str(y))
    print("Contents: " + str(content))

    if direction == 1: # Right
        front = y + 1
        while front <= grid:
            print("x: " + str(x) + " front: " + str(front))
            for c in content:
                if c[0] == x and c[1] == front:
                    return c[2]
            front += 1
        return "Null"

    elif direction == 2: # Down
        front = x + 1
        while front <= grid:
            for c in content:
                if c[0] == front and c[1] == y:
                    return c[2]
            front += 1
        return "Null"

    elif direction == 3: # Left
        front = y - 1
        while front > 0:
            for c in content:
                if c[0] == x and c[1] == front:
                    return c[2]
            front -= 1
        return "Null"

    elif direction == 4: # Up
        front = x - 1
        while front > 0:
            for c in content:
                if c[0] == front and c[1] == y:
                    return c[2]
            front -= 1
        return "Null"

    #return nearest entity

def rotate(): #Miner picked 2
    global miner
    global direction
    frontX = miner[0][0]
    frontY = miner[0][1]

    #facing right
    if direction == 1:
        print("facing right cond")
        miner[1][0] = (frontX + 1)
        miner[1][1] = frontY
        direction = 2
    #facing down
    elif direction == 2:
        print("facing down cond")
        miner[1][0] = frontX
        miner[1][1] = (frontY - 1)
        direction = 3
    #facing left
    elif direction == 3:
        print("facing left cond")
        miner[1][0] = (frontX - 1)
        miner[1][1] = frontY
        direction = 4
    #facing up
    elif direction == 4:
        print("facing up cond")
        miner[1][0] = frontX
        miner[1][1] = (frontY + 1)
        direction = 1

    global rotateCtr
    rotateCtr += 1

def move(): #Miner picked 3
    global miner
    global direction

    pastCoors.append([miner[0][0],miner[0][1]])

    #set position to front
    miner[0][0] = miner[1][0]
    miner[0][1] = miner[1][1]

    frontX = miner[1][0]
    frontY = miner[1][1]

    #adjust front
    if direction == 1:  # right
        miner[1][1] = frontY + 1
    elif direction == 2:  # down
        miner[1][0] = frontX + 1
    elif direction == 3:  # left
        miner[1][1] = frontY - 1
    elif direction == 4:  # up
        miner[1][0] = frontX - 1


''' ------------ INITIALIZATION --------------- '''
valid = False
grid = 8 # default value
while (not valid):
    grid = int(input("Input grid size: "))
    if(grid >= 8 and grid <= 64):
        valid = True
print("grid size is " + str(grid))

valid = False
while (not valid):
    goldX = int(input("Input gold X coordinate: "))
    goldY = int(input("Input gold Y coordinate: "))

    if((goldX > 0 and goldY > 0) and (goldX <= grid and goldY <= grid)):
        valid = True

    gold.append(goldX)
    gold.append(goldY)
    print("Gold coordinate is: ")
    print(gold)

pitval = (int(round(float(grid) * 0.25)))
beaval = (int(round(float(grid) * 0.1)))

if pitval < 1:
    pitval = 1

if beaval < 1:
    beaval = 1

print("# of Pits: " + str(pitval))
print("# of Beacons: " + str(beaval))

for i in range(pitval):
    valid = False
    while (not valid):
        pitX = int(input("Input Pit X Coordinate: "))
        pitY = int(input("Input Pit Y Coordinate: "))
        if((pitX > 0 and pitY > 0) and (pitX <= grid and pitY <= grid) and (pitX != gold[0] and pitY != gold[1])):
            pits.append([pitX,pitY])
            valid = True
        else:
            print("Invalid coordinate for pit")

for i in range(beaval):
    valid = False
    while (not valid):

        beaX = int(input("Input Beacon X Coordinate: "))
        beaY = int(input("Input Beacon Y Coordinate: "))
        duplicate = False

        for p in pits:
            if beaX == p[0] and beaY == p[1]:
                duplicate = True

        if beaX == gold[0] and beaY == gold[1]:
            duplicate = True

        if (not duplicate):
            beacons.append([beaX,beaY])
            valid = True
        else:
            print("Invalid coordinate for beacon.")

valid = False
level = 0
while (not valid):
    print("[1] Random\n[2] Smart")
    level = int(input("Choose Level: "))
    if level == 1 or level == 2:
        valid = True
    else:
        print("Invalid Input")

''' --------------------MAIN--------------------------'''
checker = True
print("start: " + str(miner) + " direction: " + str(direction))
act = 0

while checker:

    #next = input("Next?")

    if level == 1:
        # add current front to PastCoors
        #pastCoors.append([miner[0][0],miner[0][1]])
        # checks if Miner has been to Front coordinate
        act = randomLevel()
    elif level == 2:
        act = smartLevel()

    #Miner Moves
    if (act == 1): # Scan
        # print result
        result = scan(grid)
        print("nag-scan: " + str(miner) + " direction: " + str(direction) + " result: " + result)
        #act += 1

    elif (act == 2): # Rotate
        rotate()
        print("nag-rotate: " + str(miner) + " direction: " + str(direction))
        #act += 1

    elif (act == 3): # Move
        move()
        print("normal move: " + str(miner) + " direction: " + str(direction))
       # 1 - right, 2 - down, 3 - left, 4 - up
        # if edge -> rotate x 1
        moveCtr += 1

        '''---------CHECKERS-----------'''
    #if gold
    if miner[0][0] == gold[0] and miner[0][1] == gold[1]:
        print("yey winner: " + str(miner) + " direction: " + str(direction))
        checker = False

    #if pit
    for p in pits:
        if miner[0][0] == p[0] and miner[0][1] == p[1]:
            checker = False
            print("ew loser" + str(miner) + " direction: " + str(direction))

    #if beacon
    for b in beacons:
        if miner[0][0] == b[0] and miner[0][1] == b[1]:
            #gold - beacon?
            a = abs(gold[0] - miner[0][0])
            b = abs(gold[1] - miner[0][1])
            beacon = a + b

            # value of m; beacon's distance from Gold
            print("Beacon: M is " + str(beacon))

print("Total Scan: " + str(scanCtr))
print("Total Rotate: " + str(rotateCtr))
print("Total Move: " + str(moveCtr))
