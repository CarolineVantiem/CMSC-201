# File: proj2.py                                                                                                                                                                                                                              
# Author: Caroline                                                                                                                                                                                                                            
# Date: 11/9/2017                                                                                                                                                                                                                             
# Section: 3                                                                                                                                                                                                                                  
# E-mail: Cvantie1@umbc.edu                                                                                                                                                                                                                   
# Description: This program is a simulation of Conway's                                                                                                                                                                                       
#              Game of Life. Lets the user interact and                                                                                                                                                                                       
#              pick which cells to turn on and how many                                                                                                                                                                                       
#              iterations to run.                                                                                                                                                                                                             

# constants                                                                                                                                                                                                                                   
# main menu prompt                                                                                                                                                                                                                            
ROW_MIN = 0      # row input                                                                                                                                                                                                                  
COLUMN_MIN = 0   # column input                                                                                                                                                                                                               

# second menu prompt                                                                                                                                                                                                                          
USER_QUIT = "q"  # for user to quit                                                                                                                                                                                                           

# third prompt                                                                                                                                                                                                                                
ITER_MIN = 0     # iteration input min                                                                                                                                                                                                        

# assigning cells                                                                                                                                                                                                                             
ALIVE_CELL = "A" # alive cell                                                                                                                                                                                                                 
DEAD_CELL = "."  # dead cell                                                                                                                                                                                                                  

# 1                                                                                                                                                                                                                                           
##################################################################                                                                                                                                                                            
# getValidInput() gets a valid integer from the user that        #                                                                                                                                                                            
#                 falls within the appropriate range; uses       #                                                                                                                                                                            
#                 a prompt provided at function call             #                                                                                                                                                                            
# Input:          prompt;  a string to use when asking for input #                                                                                                                                                                            
#                 minimum; a minimum integer                     #                                                                                                                                                                            
# Output:         userInput; an integer within the range         #                                                                                                                                                                            
##################################################################                                                                                                                                                                            
def getValidInput(prompt, minimum):
    userInput = int(input(prompt))
    while userInput <= minimum:
        print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 1")
        userInput = int(input(prompt))
    return userInput

# 2                                                                                      
#####################################################################                                                                                                                                                                         
# getValidInputTwo() gets a valid integer from the user that        #                                                                                                                                                                         
#                    falls within the appropriate range; uses       #                                                                                                                                                                         
#                    a prompt provided at function call             #                                                                                                                                                                         
# Input:             prompt;  a string to use when asking for input #                                                                                                                                                                         
#                    maximum; a maximum integer                     #                                                                                                                                                                         
# Output:            userInput; an integer within the range         #                                                                                                                                                                         
#####################################################################                                                                                                                                                                         
def getValidInputTwo(promptTwo, maximum):
    userInput = int(input(promptTwo))
    while userInput < COLUMN_MIN or userInput >= maximum:
        print("\tThat is not a valid value; please enter a number\n\tbetween", COLUMN_MIN, "and", maximum - 1, "inclusive")
        userInput = int(input(promptTwo))
    return userInput

# 3                                                                                                                                                                                                                                           
#################################################################                                                                                                                                                                             
# startBoard() makes the starting board for the game            #                                                                                                                                                                             
#              and turns on the cells                           #                                                                                                                                                                             
# Input:       numRow; number of rows                           #                                                                                                                                                                             
#              numColumn; number of columns                     #                                                                                                                                                                             
#              rowColumnList; a 2D list of the cells to turn on #                                                                                                                                                                             
# Output:      startList; a 2D list of the starting board       #                                                                                                                                                                             
#################################################################      
def startBoard(numRow, numColumn, rowColumnList):
    # make 2D list of starting board #                                                                                                                                                                                                        
    startList = []
    innerList = []
    counter = 0
    while counter < numRow:
        counterOne = 0
        while counterOne < numColumn:
            innerList.append(DEAD_CELL)
            counterOne += 1
        startList.append(innerList)
        innerList = []
        counter += 1

    # turn cells on #                                                                                                                                                                                                                         
    index = 0
    outerCounter = 0 #                                                                                                                                                                                                                        
    constantCounter = 0 # always be 0 find index [a][0] #                                                                                                                                                                                     
    innerConstant = 1 # always 1 find index [a][1] #                                                                                                                                                                                          
    while index < len(rowColumnList):
        startList[rowColumnList[outerCounter][constantCounter]][rowColumnList[outerCounter][innerConstant]] = "A"
        outerCounter += 1
        index += 1
    return startList

# 4                                                                                                                                                                                                                                           
################################################                                                                                                                                                                                              
# printBoard() takes in the current board and  #                                                                                                                                                                                              
#              prints out the board            #                                                                                                                                                                                              
# Input:       currentBoard; the current board #                                                                                                                                                                                              
#              numRow; number of rows          #                                                                                                                                                                                              
#              numColumn; number of columns    #                                                                                                                                                                                              
# Output:      none                            #                                                                                                                                                                                              
################################################                                                                                                                                                                                              
def printBoard(currentBoard, numRow, numColumn):
    counter = 0
    while counter < numRow:
        counterOne = 0
        while counterOne < numColumn:
            print(currentBoard[counter][counterOne], end="")
            counterOne += 1
        counter += 1
        print()
# 5                                                                                                                                                                                                                                           
###############################################################                                                                                                                                                                               
# nextIteration() takes in the current board and prints       #                                                                                                                                                                               
#                 out the next boards iteration               #                                                                                                                                                                               
# Input:          currentBoard; the current board             #                                                                                                                                                                               
#                 numRow; number of rows                      #                                                                                                                                                                               
#                 numColumn; number of columns                #                                                                                                                                                                               
# Output          newBoard; new 2D list of the next iteration #                                                                                                                                                                               
###############################################################                                                                                                                                                                               
##################################                                                                                                                                                                                                            
# COMMENTS KEY                   #                                                                                                                                                                                                            
# checking each neighbor         #                                                                                                                                                                                                            
# 0 - left top diagonal cell     #                                                                                                                                                                                                            
# 1 - above cell                 #                                                                                                                                                                                                            
# 2 - right top diagonal cell    #                                                                                                                                                                                                            
# 3 - left cell                  #                                                                                                                                                                                                            
# 4 - right cell                 #                                                                                                                                                                                                            
# 5 - left bottom diagonal cell  #                                                                                                                                                                                                            
# 6 - bottom cell                #                                                                                                                                                                                                            
# 7 - right bottom diagonal cell #                                                                                                                                                                                                            
##################################                 
def nextIteration(currentBoard, numRow, numColumn):
    newBoard = list(currentBoard)

    # top left cell #                                                                                                                                                                                                                         
    constantZero = 0
    constantOne = 1
    found = 0
    if currentBoard[constantZero][constantZero] == DEAD_CELL: # if the cell is dead #                                                                                                                                                         
        # CHECK EACH NEIGHBOR #                                                                                                                                                                                                               
        if currentBoard[constantZero][constantOne] == ALIVE_CELL:
            found += 1
        if currentBoard[constantOne][constantOne] == ALIVE_CELL:
            found += 1
        if currentBoard[constantOne][constantZero] == ALIVE_CELL:
            found += 1
        if found == 3: # turn cell on #                                                                                                                                                                                                       
            newBoard[constantZero][constantZero] = ALIVE_CELL
        else: # cell remains off #                                                                                                                                                                                                            
            newBoard[constantZero][constantZero] = DEAD_CELL
        found = 0
    elif currentBoard[constantZero][constantZero] == ALIVE_CELL: # if the cell is alive #                                                                                                                                                     
        # CHECK EACH NEIGHBOR #                                                                                                                                                                                                               
        if currentBoard[constantZero][constantOne] == ALIVE_CELL:
            found += 1
        if currentBoard[constantOne][constantOne] == ALIVE_CELL:
            found += 1
        if currentBoard[constantOne][constantZero] == ALIVE_CELL:
            found += 1
        if found != 2 and found != 3: # cell remains off #                                                                                                                                                                                    
            newBoard[constantZero][constantZero] = DEAD_CELL
        else: # turn cell on #                                                                                                                                                                                                                
            newBoard[constantZero][constantZero] = ALIVE_CELL
        found = 0
   
    # top row #                                                                                                                                                                                                                               
    counter = 0
    row = 0
    column = 1
    found = 0
    while counter < numColumn - 2:
        if currentBoard[row][column] == DEAD_CELL: # if the cell is dead #                                                                                                                                                                    
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                           
            if currentBoard[row][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column + 1] == ALIVE_CELL:
                found += 1
            if found == 3: # turn cell on #                                                                                                                                                                                                   
                newBoard[row][column] = ALIVE_CELL
            else: # cell remains off #                                                                                                                                                                                                        
                newBoard[row][column] = DEAD_CELL
            found = 0
            column += 1
        elif currentBoard[row][column] == ALIVE_CELL: # if the cell is alive #                                                                                                                                                                
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                           
            if currentBoard[row][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column + 1] == ALIVE_CELL:
                found += 1
            if found != 2 and found != 3: # cell remains off #                                   
                              newBoard[row][column] = DEAD_CELL
            else: # turn cell on #                                                                                                                                                                                                            
                newBoard[row][column] = ALIVE_CELL
            found = 0
            column += 1
        counter += 1
   
    # top right cell #                                                                                                                                                                                                                        
    row = 0
    column = numColumn - 1
    found = 0
    if currentBoard[row][column] == DEAD_CELL: # if the cell is dead #                                                                                                                                                                        
        # CHECK EACH NEIGHBOR #                                                                                                                                                                                                               
        if currentBoard[row][column - 1] == ALIVE_CELL:
            found += 1
        if currentBoard[row + 1][column - 1] == ALIVE_CELL:
            found += 1
        if currentBoard[row + 1][column] == ALIVE_CELL:
            found += 1
        if found == 3: # turn cell on #                                                                                                                                                                                                       
            newBoard[row][column] = ALIVE_CELL
        else: # cell remains off #                                                                                                                                                                                                            
            newBoard[row][column] = DEAD_CELL
        found = 0
    elif currentBoard[row][column] == ALIVE_CELL: # if the cell is alive #                                                                                                                                                                    
        # CHECK EACH NEIGHBOR #                                                                                                                                                                                                               
        if currentBoard[row][column - 1] == ALIVE_CELL:
            found += 1
        if currentBoard[row + 1][column - 1] == ALIVE_CELL:
            found += 1
        if currentBoard[row + 1][column] == ALIVE_CELL:
            found += 1
        if found != 2 and found != 3: # cell remains off #                                                                                                                                                                                    
            newBoard[row][column] = DEAD_CELL
        else: # turn cell on #                                                                                                                                                                                                                
            newBoard[row][column] = ALIVE_CELL
        found = 0

    # left side #                                                                                                                                                                                                                             
    counter = 0
    row = 1
    column = 0
    found = 0
    while counter < numRow - 2:
        if currentBoard[row][column] == DEAD_CELL: # if the cell is dead #                                                                                                                                                                    
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                           
            if currentBoard[row - 1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column] == ALIVE_CELL:
                found += 1
            if found == 3: # turn cell on #                                                                                                                                                                                                   
                newBoard[row][column] = ALIVE_CELL
            else: # cell remains off #                                                                                                                                                                                                        
                newBoard[row][column] = DEAD_CELL
            found = 0
            row += 1
        elif currentBoard[row][column] == ALIVE_CELL: # if the cell is alive #                                                                                                                                                                
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                           
            if currentBoard[row - 1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column] == ALIVE_CELL:
                found += 1
            if found != 2 and found != 3: # cell remains off #                                                                                                                                                                                
                newBoard[row][column] = DEAD_CELL
            else: # turn cell on #                                                                                                                                                                                                            
                newBoard[row][column] = ALIVE_CELL
            found = 0
            row += 1
        counter += 1

    # right side #                                                                                                                                                                                                                            
    counter = 0
    row = 1
    column = numColumn - 1
    found = 0
    while counter < numRow - 2:
        if currentBoard[row][column] == DEAD_CELL: # if the cell is dead #                                                                                                                                                                    
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                           
            if currentBoard[row - 1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column] == ALIVE_CELL:
                found += 1
            if found == 3: # turn cell on #                                                                                                                                                                                                   
                newBoard[row][column] = ALIVE_CELL
            else: # cell remains off #                                                                                                                                                                                                        
                newBoard[row][column] = DEAD_CELL
            found = 0
            row += 1
        elif currentBoard[row][column] == ALIVE_CELL: # if the cell is alive #                                                                                                                                                                
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                           
            if currentBoard[row - 1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row + 1][column] == ALIVE_CELL:
                found += 1
                        if found != 2 and found != 3: # cell remains off #                                                                                                                                                                                
                newBoard[row][column] = DEAD_CELL
            else: # turn cell on #                                                                                                                                                                                                            
                newBoard[row][column] = ALIVE_CELL
            found = 0
            row += 1
        counter += 1

        
    # bottom left cell #                                                                                                                                                                                                                      
    row = numRow - 1
    column = 0
    found = 0
    if currentBoard[row][column] == DEAD_CELL: # if the cell is dead #                                                                                                                                                                        
        # CHECK EACH NEIGHBOR #                                                                                                                                                                                                               
        if currentBoard[row - 1][column] == ALIVE_CELL:
            found += 1
        if currentBoard[row - 1][column + 1] == ALIVE_CELL:
            found += 1
        if currentBoard[row][column + 1] == ALIVE_CELL:
            found += 1
        if found == 3: # turn cell on #                                                                                                                                                                                                       
            newBoard[row][column] = ALIVE_CELL
        else: # cell remains off #                                                                                                                                                                                                            
            newBoard[row][column] = DEAD_CELL
        found = 0
    elif currentBoard[row][column] == ALIVE_CELL: # if the cell is alive #                                                                                                                                                                    
        # CHECK EACH NEIGHBOR #                                                                                                                                                                                                               
        if currentBoard[row - 1][column] == ALIVE_CELL:
            found += 1
        if currentBoard[row - 1][column + 1] == ALIVE_CELL:
            found += 1
        if currentBoard[row][column + 1] == ALIVE_CELL:
            found += 1
        if found != 2 and found != 3: # cell remains off #                                                                                                                                                                                    
            newBoard[row][column] = DEAD_CELL
        else: # turn cell on #                                                                                                                                                                                                                
            newBoard[row][column] = ALIVE_CELL
        found = 0


    # bottom row #                                                                                                                                                                                                                            
    counter = 0
    row = numRow - 1
    column = 1
    found = 0
    while counter < numColumn - 2:
        if currentBoard[row][column] == DEAD_CELL: # if the cell is dead #                                                                                                                                                                    
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                           
            if currentBoard[row][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column + 1] == ALIVE_CELL:
                found += 1
            if found == 3: # turn cell on #                                                                                                                                                                                                   
                newBoard[row][column] = ALIVE_CELL
            else: # cell remains off #                                                                                                                                                                                                        
                newBoard[row][column] = DEAD_CELL
            found = 0
            column += 1
        elif currentBoard[row][column] == ALIVE_CELL: # if the cell is alive #                                                                                                                                                                
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                           
            if currentBoard[row][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column - 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row - 1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row -1][column + 1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column + 1] == ALIVE_CELL:
                found += 1
            if found != 2 and found != 3: # cell remains off #                                                                                                                                                                                
                newBoard[row][column] = DEAD_CELL
            else: # turn cell on #                                                                                                                                                                                                            
                newBoard[row][column] = ALIVE_CELL
            found = 0
            column += 1
        counter += 1

    # bottom right cell #                                                                                                                                                                                                                     
    row = numRow - 1
    column = numColumn - 1
    found = 0
    if currentBoard[row][column] == DEAD_CELL: # if the cell is dead                                                                                                                                                                          
        # CHECK EACH NEIGHBOR #                                                                                                                                                                                                               
        if currentBoard[row - 1][column] == ALIVE_CELL:
            found += 1
        if currentBoard[row - 1][column - 1] == ALIVE_CELL:
            found += 1
        if currentBoard[row][column - 1] == ALIVE_CELL:
            found += 1
        if found == 3: # turn cell on #                                                                                                                                                                                                       
            newBoard[row][column] = ALIVE_CELL
        else: # cell remains off #                                                                                                                                                                                                            
            newBoard[row][column] = DEAD_CELL
        found = 0
    elif currentBoard[row][column] == ALIVE_CELL: # if the cell is alive #                                                                                                                                                                    
        # CHECK EACH NEIGHBOR #                                                                                                                                                                                                               
        if currentBoard[row - 1][column] == ALIVE_CELL:
            found += 1
        if currentBoard[row - 1][column - 1] == ALIVE_CELL:
            found += 1
        if currentBoard[row][column - 1] == ALIVE_CELL:
            found += 1
        if found != 2 and found != 3: # cell remains off #                                                                                                                                                                                    
            newBoard[row][column] = DEAD_CELL
        else: # turn cell on #                                                                                                                                                                                                                
            newBoard[row][column] = ALIVE_CELL
        found = 0
  # first row #                                                                                                                                                                                                                          
    counter = 0
    row = 1
    column = 1
    found = 0
    while counter < numColumn - 2:
        if currentBoard[row][column] == DEAD_CELL: # if cell is dead #                                                                                                                                                                     
            # CHECK EACH NEIGHBOR #                                                                                                                                                                                                        
            if currentBoard[row-1][column-1] == ALIVE_CELL:
                found += 1
            if currentBoard[row-1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row-1][column+1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column-1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column+1] == ALIVE_CELL:
                found += 1
            if currentBoard[row+1][column-1] == ALIVE_CELL:
                found +=1
            if currentBoard[row+1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row+1][column+1] == ALIVE_CELL:
                found += 1
            if found == 3:
                newBoard[row][column] = ALIVE_CELL
            else:
                newBoard[row][column] = DEAD_CELL
            found = 0
            column += 1
        elif currentBoard[row][column] == ALIVE_CELL: # if cell is dead #                                                                                                                                                                  
            if currentBoard[row-1][column-1] == ALIVE_CELL:
                found += 1
            if currentBoard[row-1][column] == ALIVE_CELL:
               found += 1
            if currentBoard[row-1][column+1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column-1] == ALIVE_CELL:
                found += 1
            if currentBoard[row][column+1] == ALIVE_CELL:
                found += 1
            if currentBoard[row+1][column-1] == ALIVE_CELL:
                found +=1
            if currentBoard[row+1][column] == ALIVE_CELL:
                found += 1
            if currentBoard[row+1][column+1] == ALIVE_CELL:
                found += 1
            if found < 2:
                newBoard[row][column] = DEAD_CELL
            elif found > 3:
                newBoard[row][column] = DEAD_CELL
            else:
                newBoard[row][column] = ALIVE_CELL
            found = 0
            column += 1
        counter += 1

    return newBoard

# main #                                                                                                                                                                                                                                   
def main():
    # PART 1#                                                                                                                                                                                                                              
    # ask user for rows #                                                                                                                                                                                                                  
    prompt = "Please enter number of rows: "
    numRow = getValidInput(prompt, ROW_MIN)

    # ask user for columns #                                                                                                                                                                                                               
    prompt = "Please enter the number of columns: "
    numColumn = getValidInput(prompt, COLUMN_MIN)

    # ask user for row ON/'q' to quit #                                                                                                                                                                                                    
    storeList = [] # store row/column values in 2D list #                                                                                                                                                                                  
    validList = [] # append to list IF VALID #                                                                                                                                                                                             
    promptOne = input("\nPlease enter the row of a cell to turn on (or q to exit): ")
    while promptOne != USER_QUIT:
        rowOn = int(promptOne)
        if rowOn < ROW_MIN or rowOn >= numRow:
            print("\tThat is not a valid value; please enter a number\n\tbetween", ROW_MIN, "and", numRow - 1, "inclusive")
            promptOne = input("\nPlease enter the row of a cell to turn on (or q to exit): ")
        elif rowOn >= ROW_MIN or rowOn < numRow:
            rowValid = rowOn
            validList.append(rowValid) # append row value only IF VALID #                                                                                                                                                                  
            # ask the user for the column/check valid input #                                                                                                                                                                              
            promptTwo = "Please enter a column for that cell: "
            columnOn = getValidInputTwo(promptTwo, numColumn)
            validList.append(columnOn) # append column value only IF VALID #                                                                                                                                                               
            storeList.append(validList) # append to list to make 2D list [row][column] #                                                                                                                                                   
            promptOne = input("\nPlease enter the row of a cell to turn on (or q to exit): ")
            validList = [] # clear list until user enters "q" #                                                                                                                                                                            

    # ask user for iterations #                                                                                                                                                                                                            
    iterNum = int(input("\nHow many iterations should I run? "))
    while iterNum < ITER_MIN:
        print("\tThat is not a valid value: please enter a number\n\tgreater than or equal to 0")
        iterNum = int(input("\nHow many iterations should I run? "))

    # show starting board #                                                                                                                                                                                                                
    print("\nStarting Board: ")
    currentBoard = startBoard(numRow, numColumn, storeList)
    printBoard(currentBoard, numRow, numColumn)
####################################################################################                                                                                                                                                       

####################################################################################                                                                                                                                                       
    # PART 2 #                                                                                                                                                                                                                             
    # start iterations if iterNum > 0 #                                                                                                                                                                                                    
    counter = 0
    iterationNum = 1
    while counter < iterNum:
        print("\nIteration",iterationNum,":")
        currentBoard = nextIteration(currentBoard, numRow, numColumn) # run nextIteration #                                                                                                                                                
        printBoard(currentBoard, numRow, numColumn)
        iterationNum +=1
        counter += 1

main()


