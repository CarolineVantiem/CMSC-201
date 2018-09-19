# File: proj3.py                                                                                                                                                                                                                           
# Author: Caroline Vantiem                                                                                                                                                                                                                 
# Date: 11/27/2017                                                                                                                                                                                                                         
# Section: 3                                                                                                                                                                                                                               
# E-mail: cvantie1@umbc.edu                                                                                                                                                                                                                
# Description: Maze solver                                                                                                                                                                                                                 

#############                                                                                                                                                                                                                              
# CONSTANTS #                                                                                                                                                                                                                              
#############                                                                                                                                                                                                                              
# wall directions #                                                                                                                                                                                                                        
RIGHT = 0
BOTTOM = 1
LEFT = 2
TOP = 3

# minimum input validation for row/column #                                                                                                                                                                                                
MAZE_MIN = 0

# open/closed wall #                                                                                                                                                                                                                       
OPEN = 0
CLOSED = 1

# row/column text file indices #                                                                                                                                                                                                           
ROW_INDEX = 0

COLUMN_TWO = 2
COLUMN_THREE = 3
COLUMN_FIVE = 5

# dimensions/position text file indices #                                                                                                                                                                                                  
DIMENSIONS = 0
FINISH_POSITION = 1
WALLS = 4

##################################################                                                                                                                                                                                         
# readMaze() read in the specified text file and #                                                                                                                                                                                         
#            create a 3D list format for a maze  #                                                                                                                                                                                         
# Input:     filename; specified text to open    #                                                                                                                                                                                         
# Outut:     maze; 3D list of the maze           #                                                                                                                                                                                         
##################################################           
def readMaze(filename):
    # get row/column dimensions #                                                                                                                                                                                                          
    myFile = open(filename, "r")
    linesToRead = myFile.readlines()
    # if maze dimensions are single digits #                                                                                                                                                                                               
    if (len(linesToRead[ROW_INDEX])) == 4:
        row = int(linesToRead[DIMENSIONS][ROW_INDEX])
        column = int(linesToRead[DIMENSIONS][COLUMN_TWO])
    # if maze dimensions are double digits #                                                                                                                                                                                               
    elif (len(linesToRead[ROW_INDEX])) == 6:
        row = int(linesToRead[DIMENSIONS][ROW_INDEX:COLUMN_TWO])
        column = int(linesToRead[DIMENSIONS][COLUMN_THREE:COLUMN_FIVE])
    myFile.close()

    # 3D maze #                                                                                                                                                                                                                            
    maze = []
    counter = 2
    for a in range(row): # append num of rows #                                                                                                                                                                                            
        middle = []
        for b in range(column): # append num of columns #                                                                                                                                                                                  
            inner = []
            counterOne = 0
            for c in range(WALLS): # append FOUR numbers #                                                                                                                                                                                 
                inner.append(int(linesToRead[counter][counterOne]))
                counterOne += 2
            counter += 1
            middle.append(inner)
        maze.append(middle)
    return maze
#####################################################                                                                                                                                                                                      
# searchMaze() using recursion finds a solution     #                                                                                                                                                                                      
#              to the maze                          #                                                                                                                                                                                      
# Input:       maze; 3D maze                        #                                                                                                                                                                                      
#              currRow; current row position        #                                                                                                                                                                                      
#              currColumn; current column position  #                                                                                                                                                                                      
#              finRow; finish row position          #                                                                                                                                                                                      
#              finColumn; finish column position    #                                                                                                                                                                                      
#              path; path of solutions              #                                                                                                                                                                                      
# Output:      none (solutions are printed in main) #                                                                                                                                                                                      
#####################################################                                                                                                                                                                                      
def searchMaze(maze, currRow, currColumn, finRow, finColumn, path):

    # BASE CASES #                                                                                                                                                                                                                         
    if currRow == finRow and currColumn == finColumn: # finish position #                                                                                                                                                                  
        print("\n""Solution found!")
        return path

    # NO SOLUTION --- boxed in #                                                                                                                                                                                                           
    if maze[currRow][currColumn][RIGHT] == CLOSED: # RIGHT WALL #                                                                                                                                                                          
        if maze[currRow][currColumn][BOTTOM] == CLOSED: # BOTTOM WALL #                                                                                                                                                                    
            if maze[currRow][currColumn][LEFT] == CLOSED: # LEFT WALL #                                                                                                                                                                    
                if maze[currRow][currColumn][TOP] == CLOSED: # TOP WALL #                                                                                                                                                                  
                    path = []
                    return path
    # RECURSIVE CASES #                                                                                                                                                                                                                    

    # RIGHT WALL #                                                                                                                                                                                                                         
    if maze[currRow][currColumn][RIGHT] == OPEN:
        currPath = []
        currPath.append("(")
        currPath.append(currRow)
        currPath.append(", ")
        currPath.append(currColumn + 1)
        currPath.append(")")
        # check if current position is not in path #                                                                                                                                                                                       
        if currPath not in path:
            newPath = []
            for i in range(len(path)): # deep copy #                                                                                                                                                                                       
                inner = list(path[i])
                newPath.append(inner)
            path.append(currPath)
            search = searchMaze(maze, currRow, currColumn+ 1 ,finRow, finColumn, path)
            # check if hit dead end #                                                                                                                                                                                                      
            if search != None:
                return search
            else:
                path.remove(currPath)

   # BOTTOM WALL #                                                                                                                                                                                                                         
    if maze[currRow][currColumn][BOTTOM] == OPEN:
        currPath = []
        currPath.append("(")
	currPath.append(currRow + 1)
        currPath.append(", ")
	currPath.append(currColumn)
        currPath.append(")")
        # check if current position is not in path #                                                                                                                                                                                       
        if currPath not in path:
            newPath = []
            for i in range(len(path)): # deep copy #                                                                                                                                                                                       
                inner = list(path[i])
                newPath.append(inner)
            path.append(currPath)
            search = searchMaze(maze, currRow + 1 , currColumn, finRow, finColumn, path)
            # check if hit dead end #                                                                                                                                                                                                      
            if search != None:
                return search
            else:
                path.remove(currPath)

    # LEFT WALL #                                                                                                                                                                                                                          
    if maze[currRow][currColumn][LEFT] == OPEN:
        currPath = []
        currPath.append("(")
        currPath.append(currRow)
        currPath.append(", ")
	currPath.append(currColumn-1)
        currPath.append(")")
        # check if current position is not in path #                                                                                                                                                                                       
        if currPath not in path:
            newPath = []
            for i in range(len(path)): # deep copy #                                                                                                                                                                                       
                inner = list(path[i])
                newPath.append(inner)
            path.append(currPath)
            search = searchMaze(maze, currRow, currColumn - 1 , finRow, finColumn, path)
            # check if hit dead end #                                                                                                                                                                                                      
            if search != None:
                return search
            else:
                path.remove(currPath)

    # TOP WALL #                                                                                                                                                                                                                           
    if maze[currRow][currColumn][TOP] == OPEN:
        currPath = []
        currPath.append("(")
        currPath.append(currRow-1)
        currPath.append(", ")
	currPath.append(currColumn)
        currPath.append(")")
        # check if current position is not in path #                                                                                                                                                                                       
        if currPath not in path:
            newPath = []
            for i in range(len(path)): # deep copy #                                                                                                                                                                                       
                inner = list(path[i])
                newPath.append(inner)
            path.append(currPath)
            search = searchMaze(maze, currRow - 1, currColumn, finRow, finColumn, path)
            # check if hit dead end #                                                                                                                                                                                                      
            if search != None:
                return search
            else:
                path.remove(currPath)

#################                          
def main():

    # welcome message #                                                                                                                                                                                                                    
    print("\n""Welcome to the Maze Solver!" "\n")

    # read in filename #                                                                                                                                                                                                                   
    filename = input("Please enter the filename of the maze: ")
    # call function --- readMaze() #                                                                                                                                                                                                       
    maze = readMaze(filename)

    ###########################################                                                                                                                                                                                            
    # row/column - dimensions/finish position #                                                                                                                                                                                            
    myFile = open(filename, "r")
    linesToRead = myFile.readlines()
    # if maze dimensions are single digits #                                                                                                                                                                                               
    if (len(linesToRead[ROW_INDEX])) == 4:
        row = int(linesToRead[DIMENSIONS][ROW_INDEX])
        column = int(linesToRead[DIMENSIONS][COLUMN_TWO])
    # if maze dimensions are double digits #                                                                                                                                                                                               
    elif (len(linesToRead[ROW_INDEX])) == 6:
        row = int(linesToRead[DIMENSIONS][ROW_INDEX:COLUMN_TWO])
        column = int(linesToRead[DIMENSIONS][COLUMN_THREE:COLUMN_FIVE])

    # if finish position is single digits #                                                                                                                                                                                                
    if (len(linesToRead[FINISH_POSITION])) == 4:
        finRow = int(linesToRead[FINISH_POSITION][ROW_INDEX])
        finColumn = int(linesToRead[FINISH_POSITION][COLUMN_TWO])
    # if finish position is double digits #                                                                                                                                                                                                
    if (len(linesToRead[FINISH_POSITION])) == 6:
        finRow = int(linesToRead[FINISH_POSITION][ROW_INDEX:COLUMN_TWO])
        finColumn = int(linesToRead[FINISH_POSITION][COLUMN_THREE:COLUMN:FIVE])
    myFile.close()
    #############################################                                                                                                                                                                                          

    # row/colummn input validation values #                                                                                                                                                                                                
    rowOne = row - 1
    columnOne = column - 1

    # user input --- starting row #                                                                                                                                                                                                        
    currRow = int(input("\n""Please enter the starting row: "))
    while currRow < MAZE_MIN or currRow > rowOne:
        print("Invalid, enter a number between", MAZE_MIN, "and", rowOne, "(inclusive)")
        currRow = int(input("Please enter the starting row: "))
    # user input --- starting column #                                                                                                                                                                                                     
    currColumn = int(input("\n""Please enter the starting column: "))
    while currColumn < MAZE_MIN or currColumn > columnOne:
        print("Invalid, enter a number between", MAZE_MIN, "and", columnOne, "(inclusive)")
        currColumn = int(input("Please enter the starting column: "))

    # path list #                                                                                                                                                                                                                          
    path = []
    newList = []
    newList.append("(")
    newList.append(currRow)
    newList.append(", ")
    newList.append(currColumn)
    newList.append(")")
    path.append(newList)

    # call function --- searchMaze() #                                                                                                                                                                                                     
    solution = searchMaze(maze, currRow, currColumn, finRow, finColumn, path)

    # print solutions #                                                                                                                                                                                                                    
    if (len(solution)) == 0:
        print("\n""No solution found!""\n")
    else:
        for x in range(len(solution)):
            for y in range(len(solution[x])):
                print(str(solution[x][y]), end="")
            print("\n")

main()

