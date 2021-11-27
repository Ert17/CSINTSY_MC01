import tkinter as tk
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
scanChecker = 0
grid = 8

''' ------------------- Grid Class -------------------------- '''
#gridsize = 20
# class for Grid
class Grid (tk.Frame):
    # Grid entity to the screen
    def __init__(self, parent, gridsize):
        self.gridsize = gridsize

        # Conditions for board size initialization
        if gridsize <= 8:
            size = 96
        elif gridsize <= 16:
            size = 48
        elif gridsize <= 24:
            size = 32
        elif gridsize <= 32:
            size = 24
        elif gridsize <= 40:
            size = 19
        elif gridsize <= 48:
            size = 16
        elif gridsize <= 56:
            size = 14
        elif gridsize <= 64:
            size = 12

        canvas_width = gridsize * size
        canvas_height = gridsize * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, width=canvas_width, height=canvas_height, background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
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


        #        for p in pits:
        #            if beaX == p[0] and beaY == p[1]:
        #                duplicate = True


    for i in range(pitval):

        '''---asking for pit--'''
            # as long as not miner, gold, and beacon/s position
            # as long as greater than 0
            # as long as less than or equal to grid size
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
    while (not valid):
        print("[1] Random\n[2] Smart\n[3] User Input")
        level = int(input("Choose Level: "))
        if level == 1 or level == 2 or level == 3:
            valid = True
        else:
            print("Invalid Input")


def showGrid():
    global grid
    global pits
    global beacons
    global gold

    pits = []
    beacons = []
    gold = []

    grid = gridSize.get()
    initializeElements()
    #print(grid)

    ''' ------------------- GRID & STAT WINDOW -------------------------- '''
    gridWin = tk.Toplevel()
    gridWin.resizable(True, True)

    gridFrame = tk.LabelFrame(gridWin, padx=5, pady=5)
    gridFrame.grid(row=0, column=0, pady=10)

    t = Grid(gridFrame, grid)
    t.grid(row = 0, column = 0)

    # Miner Statistics
    statFrame = tk.LabelFrame(gridWin, text="Miner Statistics", padx=5, pady=5)
    statFrame.grid(row=0, column=1, padx=10, pady=10)

    scanLbl = tk.Label(statFrame, text="Scan Count: ").grid(row=0, column=0)
    rotateLbl = tk.Label(statFrame, text="Rotate Count: ").grid(row=1, column=0)
    moveLbl = tk.Label(statFrame, text="Move Count: ").grid(row=2, column=0)
    totalLbl = tk.Label(statFrame, text="Total Count: ").grid(row=3, column=0)

    scanCtLbl = tk.Label(statFrame, text="0").grid(row=0, column=1)
    rotateCtLbl = tk.Label(statFrame, text="0").grid(row=1, column=1)
    moveCtLbl = tk.Label(statFrame, text="0").grid(row=2, column=1)
    totalCtLbl = tk.Label(statFrame, text="0").grid(row=3, column=1)


''' ------------------- INITIALIZATION WINDOW -------------------------- '''
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
gridSize = tk.IntVar()
GridEnt = tk.Spinbox(root, width = 2, from_ = 8, to = 64, textvariable = gridSize).grid(row=1, column=1)

# GoldLbl = tk.Label(root, text="Gold Pit Coordinate").grid(row=2)
# BeaconsLbl = tk.Label(root, text="Beacon(s) Coordinate").grid(row=3)
# PitsLbl = tk.Label(root, text="Pit(s) Coordinate").grid(row=4)
# Level = tk.Label(root, text="Level Type").grid(row=5)
#
# GoldEnt = tk.Entry(root, width=5).grid(row=2, column=1)
# BeaconsEnt = tk.Text(root, height=5, width=10, padx=1, pady=1,relief='ridge', insertborderwidth=2).grid(row=3, column=1) # can't see padding, relief, border on macOS? zzz
# PitsEnt = tk.Text(root, height=5, width=10, padx=1, pady=1, relief='ridge', insertborderwidth=2).grid(row=4, column=1) # can't see padding, relief, border on macOS? zzz

RandomRdo = tk.Radiobutton(root, text="Random", value=0).grid(row=2, column=0)
SmartRdo = tk.Radiobutton(root, text="Smart", value=1).grid(row=2, column=1, pady=5)
BeginBtn = tk.Button(root, text="Begin", font=('Arial', 12, 'bold'), width=20, height=2, command = showGrid).grid(row=3, columnspan=2, pady=10)


root.mainloop()
