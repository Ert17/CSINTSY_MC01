import tkinter as tk
from tkinter import ttk
import random
import time

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
totalCtr = 0
scanChecker = 0
scanResults = []
totalRotate = 0
needRotate = 0
grid = 8
levels = ["Random", "Smart"]
views = ["Fast", "Step"]
level = None

''' ------------------- Grid Class -------------------------- '''
#gridsize = 20
# class for Grid
class Grid (tk.Frame):
    # Grid entity to the screen
    def __init__(self, parent, gridsize):
        self.gridsize = gridsize
        self.pieces = {}

        # Conditions for board size initialization
        if gridsize <= 8:
            self.size = 96
        elif gridsize <= 16:
            self.size = 48
        elif gridsize <= 24:
            self.size = 32
        elif gridsize <= 32:
            self.size = 24
        elif gridsize <= 40:
            self.size = 19
        elif gridsize <= 48:
            self.size = 16
        elif gridsize <= 56:
            self.size = 14
        elif gridsize <= 64:
            self.size = 12

        canvas_width = gridsize * self.size
        canvas_height = gridsize * self.size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, width=canvas_width, height=canvas_height, background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row, column):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    # Place elements on Grid
    def placepiece(self, name, row, column):
        '''Place an element at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    # Grid update
    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.gridsize)
        ysize = int((event.height-1) / self.gridsize)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        for row in range(self.gridsize):
            for col in range(self.gridsize):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", tags="square")
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


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


def scan(grid): #Miner picked 1
    global direction
    global miner
    global scanCtr
    global totalCtr

    totalCtr += 1
    scanCtr += 1


    x = miner[0][0]
    y = miner[0][1]

    content = []

    for pit in pits:
        content.append([pit[0],pit[1],"P"])
    for beacon in beacons:
        content.append([beacon[0],beacon[1],"B"])

    content.append([gold[0], gold[1], "G"])

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


def rotate(): #Miner picked 2
    global miner
    global direction
    global rotateCtr
    global totalCtr

    totalCtr += 1
    rotateCtr += 1

    frontX = miner[0][0]
    frontY = miner[0][1]

    #facing right
    if direction == 1:
        miner[1][0] = (frontX + 1)
        miner[1][1] = frontY
        direction = 2
    #facing down
    elif direction == 2:
        miner[1][0] = frontX
        miner[1][1] = (frontY - 1)
        direction = 3
    #facing left
    elif direction == 3:
        miner[1][0] = (frontX - 1)
        miner[1][1] = frontY
        direction = 4
    #facing up
    elif direction == 4:
        miner[1][0] = frontX
        miner[1][1] = (frontY + 1)
        direction = 1


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


def beacon(gold, miner):
    #Shortest distance of beacon to gold
    a = abs(gold[0] - miner[0])
    b = abs(gold[1] - miner[1])
    beacon = a + b

    return beacon

def initializeElements():
    global gold
    global pits
    global beacons

    valid = False
    goldX = 1
    goldY = 1
    while ((goldX == 1 and goldY == 1)):
        # As long as not 1,1 and greater than 0 and less than grid size -> accept random number
        # goldX = int(input("Input gold X coordinate: "))
        # goldY = int(input("Input gold Y coordinate: "))
        goldX = random.randint(1, grid)
        goldY = random.randint(1, grid)

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

    for i in range(beaval):

        # as long as not miner position and gold position;
        # as long as greater than 0
        # as long as less that or equal to grid size
        #beaX = int(input("Input Beacon X Coordinate: "))
        #beaY = int(input("Input Beacon Y Coordinate: "))
        valid = False
        while not valid:
            beaX = random.randint(1, grid)
            beaY = random.randint(1, grid)
            duplicate = False

            if beaX == 1 and beaY == 1: # If beacon is in miner position
                duplicate = True
            elif beaX == gold[0] and beaY == gold[1]: # If same coordinate with gold
                duplicate = True
            elif len(beacons) > 1:
                # To check the coordinates of other beacons if same
                for beacon in beacons:
                    if beaX == beacon[0] and beaY == beacon[1]:
                        duplicate = True

            if duplicate is False:
                beacons.append([beaX,beaY])
                print("Beacon added: " + str(beacons))
                valid = True
            else:
                print("Invalid coordinate for beacon")

    for i in range(pitval):

        valid = False
        while not valid:
            pitX = random.randint(1, grid)
            pitY = random.randint(1, grid)
            duplicate = False

            if pitX == 1 and pitY == 1: # If beacon is in miner position
                duplicate = True
            elif pitX == gold[0] and pitY == gold[1]: # If same coordinate with gold
                duplicate = True
                # To check the coordinates of other beacons if same
            for beacon in beacons:
                if pitX == beacon[0] and pitY == beacon[1]:
                    duplicate = True
            if len(pits) > 1:
                for pit in pits:
                    if pitX == pit[0] and pitY == pit[1]:
                        duplicate = True

            if duplicate is False:
                pits.append([pitX,pitY])
                print("Pits added: " + str(pits))
                valid = True
            else:
                print("Invalid coordinate for pit")

    level = 0
    '''
    while (not valid):
        print("[1] Random\n[2] Smart\n[3] User Input")
        level = int(input("Choose Level: "))
        if level == 1 or level == 2 or level == 3:
            valid = True
        else:
            print("Invalid Input")
    '''


def randomLevel():
    global miner
    global pastCoors
    global moveCtr
    global totalCtr

    for pastCoor in pastCoors:
        if miner[1][0] == pastCoor[0] and miner[1][1] == pastCoor[1]:
            return 2 #rotate

    # if out of bounds
    bounds = OOB()
    if bounds:
        return 2 #rotate

    totalCtr += 1
    moveCtr+=1
    return 3 #move


def smartLevel():
    print("in smartLevel")
    global miner
    global pastCoors
    global scanChecker
    global moveCtr
    global totalCtr
    global scanResults
    global totalRotate
    global needRotate

    print("Total Rotate: " + str(totalRotate))

    for pastCoor in pastCoors:
        if miner[1][0] == pastCoor[0] and miner[1][1] == pastCoor[1]:
            return 2 #rotate

    # if out of bounds
    bounds = OOB()
    if bounds:
        return 2 #rotate

    if totalRotate >= 4:
        if scanResults[0] is not 'P':
            print("Pumasok sa if\n")

            if scanResults[0] == 'G':
                # totalRotate remains at 4, agent keeps doing MOVE til Gold
                moveCtr += 1
                totalCtr += 1
                return 3
            elif scanResults[0] == 'Null' or scanResults[0] == 'B':
                #smartmove -> move + rotate
                moveCtr += 1
                totalCtr += 1

                scanResults = []
                scanChecker = 0
                totalRotate = 0
                return 4 #smartmove -> move + rotate

        else:
            for r in range(1, 3):
                if scanResults[r] == 'G':
                    needRotate = r
                    scanChecker = 0
                    break
                elif scanResults[r] == 'B':
                    needRotate = r
                    scanChecker = 0
                    totalRotate = 0
                    break
                elif scanResults[r] == 'Null':
                    needRotate = r
                    break

            return 5 #smart rotate -> rotate N times then move
    else:
        #need to put condition kung less than counter tapos Gold yung nadetect
        #if scanResults
        if scanChecker is not 1:
            scanChecker = 1
            return 1                 #scan
        else:
            scanChecker = 0
            totalRotate += 1
            return 2                 #rotate


def showGrid():
    global root
    global grid
    global level
    global pits, beacons, gold
    global miner, direction
    global scanCtDisplay, rotateCtDisplay, moveCtDisplay
    global scanChecker, scanResults, totalRotate
    global needRotate

    pits = []
    beacons = []
    gold = []

    grid = gridSize.get()

    if level_val.get() == "Random":
        level = 1
    elif level_val.get() == "Smart":
        level = 2

    print("Level: " + str(level))
    print("Grid: " + str(grid))

    ''' ------------------- GRID & STAT WINDOW -------------------------- '''
    initializeElements()

    gridWin = tk.Toplevel()
    gridWin.resizable(False, False)

    gridFrame = tk.LabelFrame(gridWin, padx=5, pady=5)
    gridFrame.grid(row=0, column=0, pady=10)

    minerImg = 'miner.png'
    pitImg = 'pit.png'
    goldImg = 'gold.png'
    beaconImg = 'beacon.png'

    goldX = gold[0] - 1
    goldY = gold[1] - 1

    minerPI = tk.PhotoImage(file=minerImg)
    pitPI = tk.PhotoImage(file=pitImg)
    goldPI = tk.PhotoImage(file=goldImg)
    beaconPI = tk.PhotoImage(file=beaconImg)

    t = Grid(gridFrame, grid)
    t.grid(row = 0, column = 0)

    t.addpiece("miner", minerPI, 0, 0)
    t.addpiece("gold", goldPI, goldX, goldY)

    for p in pits:
        pitX = p[0] - 1
        pitY = p[1] - 1
        name = "pit" + str(p)
        t.addpiece(name, pitPI, pitX, pitY)

    for b in beacons:
        beaconX = b[0] - 1
        beaconY = b[1] - 1
        name = "beacon" + str(b)
        t.addpiece(name, beaconPI, beaconX, beaconY)

    # Miner Statistics
    statFrame = tk.LabelFrame(gridWin, text="Miner Statistics", padx=5, pady=5)
    statFrame.grid(row=0, column=1, padx=10, pady=10)

    directionLbl = tk.Label(statFrame, text="Miner Direction: ").grid(row=0, column=0)
    scanRtnLbl = tk.Label(statFrame, text="Scan Return: ").grid(row=1, column=0)
    beacRtnLbl = tk.Label(statFrame, text="Beacon Return: ").grid(row=2, column=0)
    scanLbl = tk.Label(statFrame, text="Scan Count: ").grid(row=3, column=0)
    rotateLbl = tk.Label(statFrame, text="Rotate Count: ").grid(row=4, column=0)
    moveLbl = tk.Label(statFrame, text="Move Count: ").grid(row=5, column=0)
    totalLbl = tk.Label(statFrame, text="Total Count: ").grid(row=6, column=0)
    gameStateLbl = tk.Label(statFrame, text="Game State: ").grid(row=7, column=0)

    dirRText = tk.StringVar()
    dirresultDisplay = tk.Label(statFrame, textvariable = dirRText).grid(row=0, column=1)
    scanRText = tk.StringVar()
    scanRtndisplay = tk.Label(statFrame, textvariable = scanRText).grid(row=1, column=1)
    beaconText = tk.StringVar()
    beacRtnDisplay = tk.Label(statFrame, textvariable = beaconText).grid(row=2, column=1)
    scanText = tk.StringVar()
    scanCtDisplay = tk.Label(statFrame, textvariable = scanText).grid(row=3, column=1)
    rotateText = tk.StringVar()
    rotateCtDisplay = tk.Label(statFrame, textvariable = rotateText).grid(row=4, column=1)
    moveText = tk.StringVar()
    moveCtDisplay = tk.Label(statFrame, textvariable = moveText).grid(row=5, column=1)
    totalText = tk.StringVar()
    totalCtDisplay = tk.Label(statFrame, textvariable = totalText).grid(row=6, column=1)
    gameText = tk.StringVar()
    gameStateDisplay = tk.Label(statFrame, textvariable = gameText).grid(row=7, column=1, columnspan=2)

    dirRText.set("R")
    scanRText.set(" ")
    beaconText.set(" ")
    scanText.set("0")
    rotateText.set("0")
    moveText.set("0")
    totalText.set("0")
    gameText.set(" ")

    gridWin.update()

    checker = True
    print("start: " + str(miner) + " direction: " + str(direction))
    act = 0

    while checker:
        if level == 1:
            # random here
            act = randomLevel()
        elif level == 2:
            act = smartLevel()

        if (act == 1): # Scan

            result = scan(grid)
            scanResults.append(result)
            print(scanResults)

            #GUI
            scanText.set(str(scanCtr))
            totalText.set(str(totalCtr))

            print("SCAN in position: " + str(miner) + " DIRECTION: " + str(direction) + " RESULT: " + result)

        elif (act == 2): # Rotate
            rotate()

            rotateText.set(str(rotateCtr))
            totalText.set(str(totalCtr))

            # update direction
            if direction is 1:
                dirRText.set("R")
            elif direction is 2:
                dirRText.set("D")
            elif direction is 3:
                dirRText.set("L")
            elif direction is 4:
                dirRText.set("U")

            print("ROTATE in position: " + str(miner) + " DIRECTION: " + str(direction))

        elif (act == 3):
            frontX = miner[1][0] - 1
            frontY = miner[1][1] - 1
            move()
            moveText.set(str(moveCtr))
            totalText.set(str(totalCtr))

            print("MOVED to position: " + str(miner) + " DIRECTION: " + str(direction))

            #if gold
            if miner[0][0] == gold[0] and miner[0][1] == gold[1]:
                gameText.set("Win")
                print("GOLD in position: " + str(miner) + " DIRECTION: " + str(direction))
                checker = False

            #if pit
            for p in pits:
                if miner[0][0] == p[0] and miner[0][1] == p[1]:
                    gameText.set("Lose")
                    print("PIT in position: " + str(miner) + " DIRECTION: " + str(direction))
                    checker = False

            #if beacon
            for b in beacons:
                if miner[0][0] == b[0] and miner[0][1] == b[1]:
                    beaconFinal = beacon(gold, miner[0])
                    beaconText.set(str(beaconFinal))
                    # value of m; beacon's distance from Gold
                    # return result
                    print("BEACON in position: " + str(miner) + " DIRECTION: " + str(direction) + " RESULT: " + str(beaconFinal))

            t.placepiece("miner", frontX, frontY)

        elif (act == 4):
            frontX = miner[1][0] - 1
            frontY = miner[1][1] - 1
            move()
            moveText.set(str(moveCtr))
            totalText.set(str(totalCtr))

            print("MOVED to position: " + str(miner) + " DIRECTION: " + str(direction))

            #if gold
            if miner[0][0] == gold[0] and miner[0][1] == gold[1]:
                gameText.set("Win")
                print("GOLD in position: " + str(miner) + " DIRECTION: " + str(direction))
                checker = False

            #if pit
            for p in pits:
                if miner[0][0] == p[0] and miner[0][1] == p[1]:
                    gameText.set("Lose")
                    print("PIT in position: " + str(miner) + " DIRECTION: " + str(direction))
                    checker = False

            #if beacon
            for b in beacons:
                if miner[0][0] == b[0] and miner[0][1] == b[1]:
                    beaconFinal = beacon(gold, miner[0])
                    beaconText.set(str(beaconFinal))
                    # value of m; beacon's distance from Gold
                    # return result
                    print("BEACON in position: " + str(miner) + " DIRECTION: " + str(direction) + " RESULT: " + str(beaconFinal))

            t.placepiece("miner", frontX, frontY)

            rotate()

            rotateText.set(str(rotateCtr))
            totalText.set(str(totalCtr))

            # update direction
            if direction is 1:
                dirRText.set("R")
            elif direction is 2:
                dirRText.set("D")
            elif direction is 3:
                dirRText.set("L")
            elif direction is 4:
                dirRText.set("U")

            print("ROTATE in position: " + str(miner) + " DIRECTION: " + str(direction))

        elif (act == 5):
            for n in range(0, needRotate):
                rotate()
                rotateText.set(str(rotateCtr))
                totalText.set(str(totalCtr))

                # update direction
                if direction is 1:
                    dirRText.set("R")
                elif direction is 2:
                    dirRText.set("D")
                elif direction is 3:
                    dirRText.set("L")
                elif direction is 4:
                    dirRText.set("U")

            scanResults = []
            scanChecker = 0
            totalRotate = 0

            print("ROTATE in position: " + str(miner) + " DIRECTION: " + str(direction))

            frontX = miner[1][0] - 1
            frontY = miner[1][1] - 1
            move()
            moveText.set(str(moveCtr))
            totalText.set(str(totalCtr))

            print("MOVED to position: " + str(miner) + " DIRECTION: " + str(direction))

            #if gold
            if miner[0][0] == gold[0] and miner[0][1] == gold[1]:
                gameText.set("Win")
                print("GOLD in position: " + str(miner) + " DIRECTION: " + str(direction))
                checker = False

            #if pit
            for p in pits:
                if miner[0][0] == p[0] and miner[0][1] == p[1]:
                    gameText.set("Lose")
                    print("PIT in position: " + str(miner) + " DIRECTION: " + str(direction))
                    checker = False

            #if beacon
            for b in beacons:
                if miner[0][0] == b[0] and miner[0][1] == b[1]:
                    beaconFinal = beacon(gold, miner[0])
                    beaconText.set(str(beaconFinal))
                    # value of m; beacon's distance from Gold
                    # return result
                    print("BEACON in position: " + str(miner) + " DIRECTION: " + str(direction) + " RESULT: " + str(beaconFinal))

            t.placepiece("miner", frontX, frontY)
            
        gridWin.update()

        if view_val.get() == "Fast":
            ts = 0.3
        elif view_val.get() == "Step":
            ts = 1.5

        time.sleep(ts)

    gridWin.mainloop()

if __name__ == "__main__":
    ''' ------------------- INITIALIZATION WINDOW -------------------------- '''
    global root
    root = tk.Tk()
    root.title('MC01 - Gold Miner')
    root.resizable(False,False)

    Menubar = tk.Menu(root)
    Filemenu = tk.Menu(root, tearoff=0)
    Filemenu.add_command(label="New Grid")
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit", command=root.quit)
    Menubar.add_cascade(label="File", menu=Filemenu)
    root.config(menu=Menubar)

    GMLbl = tk.Label(root, text="Gold Miner", font=('Arial', 32, 'bold')).grid(row=0, columnspan=2)
    GridLbl = tk.Label(root, text="Grid Size").grid(row=1, column=0)
    LevelLbl = tk.Label(root, text="Level").grid(row=2, column=0)
    ViewLbl = tk.Label(root, text="View").grid(row=3, column=0)
    gridSize = tk.IntVar()
    GridEnt = tk.Spinbox(root, width = 2, from_ = 8, to = 64, textvariable = gridSize).grid(row=1, column=1)

    level_val = tk.StringVar()
    levelDrp = ttk.Combobox(root, value=levels, width=8, textvariable=level_val)
    levelDrp.current(0)
    levelDrp.grid(row=2, column=1, columnspan=2)
    view_val = tk.StringVar()
    viewDrp = ttk.Combobox(root, value=views, width=8, textvariable=view_val)
    viewDrp.current(0)
    viewDrp.grid(row=3, column=1, columnspan=2)
    BeginBtn = tk.Button(root, text="Begin", font=('Arial', 12, 'bold'), width=20, height=2, command = showGrid).grid(row=4, columnspan=2, pady=10)


    root.mainloop()
