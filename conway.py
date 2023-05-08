# conway`s game of life
import random, time, copy
WIDTH = 60
HEIGHT = 60

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
           column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines
    currentCells = copy.deepcopy(nextCells)
    # Print currentCell on the screen 
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space
        print() # print  a newline at the end of the row.

    # calculate the next step`s cells based on current steps cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get  neighboring coordinates:
            # % WIDHT ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            #Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 