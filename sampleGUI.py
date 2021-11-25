from tkinter import *

''' ------------------- GRID & STATISTICS WINDOW -------------------------- '''

# class for Grid
class Grid:
    # Grid entity to the screen
    def __init__(self, gridFrame):

        for row in range(gridsize):
            for col in range(gridsize):
                # change text accordingly?
                self.e = Label(gridFrame, width=2, fg='blue', font=('Arial', 16),relief='sunken', text='M')
                self.e.grid(row=row, column=col)


gridsize = 10   # accdg to user input

root = Tk()
root.title('MC01 - Gold Miner')
root.resizable(False, False)

gridFrame = LabelFrame(root, padx=5, pady=5)
gridFrame.grid(row=0, column=0, padx=10, pady=10)

t = Grid(gridFrame)

statFrame = LabelFrame(root, text="Miner Statistics", padx=5, pady=5)
statFrame.grid(row=0, column=1, padx=10, pady=10)

scanLbl = Label(statFrame, text="Scan Count: ").grid(row=0, column=0)
rotateLbl = Label(statFrame, text="Rotate Count: ").grid(row=1, column=0)
moveLbl = Label(statFrame, text="Move Count: ").grid(row=2, column=0)
totalLbl = Label(statFrame, text="Total Count: ").grid(row=3, column=0)

scanCtLbl = Label(statFrame, text="0").grid(row=0, column=1)
rotateCtLbl = Label(statFrame, text="0").grid(row=1, column=1)
moveCtLbl = Label(statFrame, text="0").grid(row=2, column=1)
totalCtLbl = Label(statFrame, text="0").grid(row=3, column=1)


''' ------------------- INITIALIZATION WINDOW -------------------------- '''

topLvl = Toplevel()

Menubar = Menu(topLvl)
Filemenu = Menu(topLvl, tearoff=0)
Filemenu.add_command(label="New Grid")
Filemenu.add_separator()
Filemenu.add_command(label="Exit", command=root.quit)
Menubar.add_cascade(label="File", menu=Filemenu)
topLvl.config(menu=Menubar)

GMLbl = Label(topLvl, text="Gold Miner", font=('Arial', 32, 'bold')).grid(row=0, columnspan=3)
GridLbl = Label(topLvl, text="Grid Size").grid(row=1)
GoldLbl = Label(topLvl, text="Gold Pit Coordinate").grid(row=2)
BeaconsLbl = Label(topLvl, text="Beacon(s) Coordinate").grid(row=3)
PitsLbl = Label(topLvl, text="Pit(s) Coordinate").grid(row=4)
Level = Label(topLvl, text="Level Type").grid(row=5)

GridEnt = Spinbox(topLvl, width=2, from_=8, to=16).grid(row=1, column=1)
GoldEnt = Entry(topLvl, width=5).grid(row=2, column=1)
BeaconsEnt = Text(topLvl, height=5, width=10, padx=1, pady=1,relief='ridge', insertborderwidth=2).grid(row=3, column=1) # can't see padding, relief, border on macOS? zzz
PitsEnt = Text(topLvl, height=5, width=10, padx=1, pady=1, relief='ridge', insertborderwidth=2).grid(row=4, column=1) # can't see padding, relief, border on macOS? zzz
RandomRdo = Radiobutton(topLvl, text="Random", value=0).grid(row=5, column=1)
SmartRdo = Radiobutton(topLvl, text="Smart", value=1).grid(row=5, column=2, pady=5)
BeginBtn = Button(topLvl, text="Begin", font=('Arial', 12, 'bold'), width=20, height=2).grid(row=6, columnspan=3, pady=10)


root.mainloop()
