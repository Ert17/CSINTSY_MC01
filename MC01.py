import random

miner = [[1, 1], [1, 2]]
#        pX  pY  fX  fY
direction = 1 # 1 - right, 2 - down, 3 - left, 4 - up
gold = []
beacons = []
pits = []
scanCtr = 0
rotateCtr = 0
moveCtr = 0

def scan():
    print("scan to")

    global scanCtr
    scanCtr += 1
    #return nearest entity

def rotate():
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

def move():
    global miner
    global direction
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

    global moveCtr
    moveCtr += 1

''' ------------ INITIALIZATION --------------- '''
valid = False
grid = 8 # default value
while (not valid):
    grid = int(input("Input grid size: "))
    if(grid >= 8 or grid <= 64):
        valid = True
print("grid size is " + str(grid))

goldX = input("Input gold X coordinate: ")
goldY = input("Input gold Y coordinate: ")

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

print("Pit Val: " + str(pitval))
print("Beacon Val: " + str(beaval))

for i in range(pitval):
    pitX = int(input("Input Pit X Coordinate: "))
    pitY = int(input("Input Pit Y Coordinate: "))
    pits.append([pitX,pitY])

for i in range(beaval):
    beaX = int(input("Input Beacon X Coordinate: "))
    beaY = int(input("Input Beacon Y Coordinate: "))
    beacons.append([beaX,beaY])
''' ----------------------------------------------'''

checker = True
print("start: " + str(miner) + " direction: " + str(direction))
while checker:

    # randomize action
    act = random.randint(1, 3)

    if (act == 1): # Scan
        # print result
        scan()
        print("nag-scan: " + str(miner) + " direction: " + str(direction))

    elif (act == 2): # Rotate
        rotate()
        print("nag-rotate: " + str(miner) + " direction: " + str(direction))

    elif (act == 3): # Move
       # 1 - right, 2 - down, 3 - left, 4 - up
        # if edge -> rotate x 1

        if (miner[0][0] == 1 and direction == 4):
            if (miner[0][1] == 1 and direction == 3): #top left
                print("nasa-edge so rotate: " + str(miner) + " direction: " + str(direction))
                rotate()
            if (miner[0][1] == grid and direction == 1): #top right
                print("nasa-edge so rotate: " + str(miner) + " direction: " + str(direction))
                rotate()
            rotate()
        elif (miner[0][1] == 1 and direction == 3):
            if (miner[1][0] == 1 and direction == 4): # top left
                print("nasa-edge so rotate: " + str(miner) + " direction: " + str(direction))
                rotate()
            if (miner[1][0] == grid and direction == 2): #bottom left
                print("nasa-edge so rotate: " + str(miner) + " direction: " + str(direction))
                rotate()
            rotate()
        elif (miner[0][0] == grid and direction == 2):
            if (miner[0][1] == 1 and direction == 3): # bottom left
                print("nasa-edge so rotate: " + str(miner) + " direction: " + str(direction))
                rotate()
            if (miner[0][1] == grid and direction == 1): #bottom right
                print("nasa-edge so rotate: " + str(miner) + " direction: " + str(direction))
                rotate()
            rotate()
        elif (miner[0][1] == grid and direction == 1):
            if (miner[0][0] == 1 and direction == 4): # top right
                print("nasa-edge so rotate: " + str(miner) + " direction: " + str(direction))
                rotate()
            if (miner[0][0] == grid and direction == 2): #bottom right
                print("nasa-edge so rotate: " + str(miner) + " direction: " + str(direction))
                rotate()
            rotate()
        else:
            move()
            print("normal move: " + str(miner) + " direction: " + str(direction))

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
                print("may result dito"  + str(miner) + " direction: " + str(direction))
                # print kung gano kalayo beacon

print("Total Scan: " + str(scanCtr))
print("Total Rotate: " + str(rotateCtr))
print("Total Move: " + str(moveCtr))
