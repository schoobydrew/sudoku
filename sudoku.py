class Cell(object):
    def __init__(self, cellValue):
        self.given = False
        self.value = 0
        self.notes = ["*" for i in range(9)]
        if cellValue:
            self.given = True
            self.value = cellValue
            self.notes[4] = cellValue
gameFile = open("grid.txt", "r")
#read the file provided by the user and split the lines into rows on gameboard
grid = gameFile.read()
gameFile.close()
grid = grid.split()
#split each row into indivudal cells and instantiate the cell class
for i in range(len(grid)):
    grid[i] = map(int, str(grid[i]))
    for j in range(len(grid[i])):
        grid[i][j] = Cell(grid[i][j])
#associate each cell to its respective row
A = grid[0]
B = grid[1]
C = grid[2]
D = grid[3]
E = grid[4]
F = grid[5]
G = grid[6]
H = grid[7]
I = grid[8]
ROWgroup = [A, B, C, D, E, F, G, H, I]
#associate each cell to its respective column
ONE = [i[0] for i in ROWgroup]
TWO = [i[1] for i in ROWgroup]
THREE = [i[2] for i in ROWgroup]
FOUR = [i[3] for i in ROWgroup]
FIVE = [i[4] for i in ROWgroup]
SIX = [i[5] for i in ROWgroup]
SEVEN = [i[6] for i in ROWgroup]
EIGHT = [i[7] for i in ROWgroup]
NINE = [i[8] for i in ROWgroup]
COLUMNgroup = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
#associate each cell to its respective family
TL = [A[0], A[1], A[2], B[0], B[1], B[2], C[0], C[1], C[2]]
TM = [A[3], A[4], A[5], B[3], B[4], B[5], C[3], C[4], C[5]]
TR = [A[6], A[7], A[8], B[6], B[7], B[8], C[6], C[7], C[8]]
ML = [D[0], D[1], D[2], E[0], E[1], E[2], F[0], F[1], F[2]]
MM = [D[3], D[4], D[5], E[3], E[4], E[5], F[3], F[4], F[5]]
MR = [D[6], D[7], D[8], E[6], E[7], E[8], F[6], F[7], F[8]]
BL = [G[0], G[1], G[2], H[0], H[1], H[2], I[0], I[1], I[2]]
BM = [G[3], G[4], G[5], H[3], H[4], H[5], I[3], I[4], I[5]]
BR = [G[6], G[7], G[8], H[6], H[7], H[8], I[6], I[7], I[8]]
FAMILYgroup = [TL, TM, TR, ML, MM, MR, BL, BM, BR]
#main logic
#starts off with a family
for family in FAMILYgroup:
    for cell in family:
        #if the cell is not a default given by the puzzle then it will try to find a note
        if not cell.given:
            #sudoku plays 1-9 this is python syntax
            for i in range(1, 10):
                #flag variable
                addMe = True
                #checks the other cells in the family to make sure that the number is not invalid
                for others in family:
                    if i == others.value:
                        addMe = False
                #tries to find the cell's appropriate row and then checks that row to see if the number is right
                for rows in ROWgroup:
                    if cell in rows:
                        for others in rows:
                            if i == others.value:
                                addMe = False
                #same logic as row probably means i can break this into a function
                #but honestly that would probs add more lines of code defining a function and returning and passing so im not
                for columns in COLUMNgroup:
                    if cell in columns:
                        for others in columns:
                            if i == others.value:
                                addMe = False
                if addMe:
                    cell.notes[i-1] = i
NOTES = open("NOTES.txt", "w+")
z = 0
for row in ROWgroup:
    z += 1
    write = ""
    x = 0
    for cell in row:
        x += 1
        y = 0
        for i in range(3):
            y += 1
            write += "{}".format(cell.notes[i])
            if (y%3) == 0:
                write += "|"
        if (x%3) == 0:
            write += "||"
    print >> NOTES, write
    write = ""
    x = 0
    for cell in row:
        x += 1
        y = 0
        for i in range(3, 6):
            y += 1
            write += "{}".format(cell.notes[i])
            if (y%3) == 0:
                write += "|"
        if (x%3) == 0:
            write += "||"
    print >> NOTES, write
    write = ""
    x = 0
    for cell in row:
        x += 1
        y = 0
        for i in range(6, 9):
            y += 1
            write += "{}".format(cell.notes[i])
            if (y%3) == 0:
                write += "|"
        if (x%3) == 0:
            write += "||"
    print >> NOTES, write
    if (z%3) == 0:
        print >> NOTES, "-"*42
    else:
        print >> NOTES, "|"*42
NOTES.close()
