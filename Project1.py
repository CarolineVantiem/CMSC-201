# File:    proj1.py                                                                                                                                                                                                                           
# Author:  Caroline Vantiem                                                                                                                                                                                                                   
# Date:    10/19/2017                                                                                                                                                                                                                         
# Section: 3                                                                                                                                                                                                                                  
# E-mail:  cvantie1@umbc.edu                                                                                                                                                                                                                  
# Description: This program lets a user search through                                                                                                                                                                                        
#              a directory of songs or make a playlist of                                                                                                                                                                                     
#              length 0-10(inclusive)                                                                                                                                                                                                         

# main menu options #                                                                                                                                                                                                                         
USER_QUIT    = -1
MENU_SEARCH  = 0
MENU_CREATE  = 1

MAX_SONG_NUM = 10  # maximum number of songs in a playlist #                                                                                                                                                                                  

# these constants are used to give names to the columns of the 2D list #                                                                                                                                                                      
YEAR     = 0
ARTIST   = 1
TITLE    = 2
GENRE    = 3
DURATION = 4
TEMPO    = 5

DETAIL_MIN = YEAR   # minimum value; used for getValidInput() #                                                                                                                                                                               
DETAIL_MAX = TEMPO  # maximum value #                                                                                                                                                                                                         

# THE REST OF YOUR CONSTANTS GO HERE!! #                                                                                                                                                                                                      

# menu options min/max #                                                                                                                                                                                                                      
MIN_SEARCH = -2
MAX_SEARCH = 2

# options for SEARCH menu choice #                                                                                                                                                                                                            
MAX_OPTION = 6
MIN_OPTION = -1

# playlist options for choosing what kind #                                                                                                                                                                                                   
PL_MIN = 0
PL_MAX = 4

# playlist options #                                                                                                                                                                                                                          
PL_YEAR = 1
PL_ARTIST = 2
PL_GENRE = 3

# playlist length min/max #                                                                                                                                                                                                                   
PL_LENGTHMIN = -1
PL_LENGTHMAX = 11

###############                                                                                                                                                                                                                               
# DON'T TOUCH #                                                                                                                                                                                                                               
###############                                                                                                                                                                                                                               
############################################################################                                                                                                                                                                  
# make2DList() constructs a 2D list from a file that contains information                                                                                                                                                                     
#              about songs in a music library, such as year and artist                                                                                                                                                                        
# Input:       filename;   a string of the music library's file name   
# Output:      resultList; a 2D list of that file in the format below                                                                                                                                                                         
#  __________________________________________________                                                                                                                                                                                         
# |   0  |    1   |   2   |   3   |     4    |   5   |                                                                                                                                                                                        
# |------|--------|-------|-------|----------|-------|                                                                                                                                                                                        
# | year | artist | title | genre | duration | tempo |                                                                                                                                                                                        
# |--------------------------------------------------|                                                                                                                                                                                        
# | year | artist | title | genre | duration | tempo |                                                                                                                                                                                        
# |--------------------------------------------------|                                                                                                                                                                                        
# | year | artist | title | genre | duration | tempo |                                                                                                                                                                                        
# |--------------------------------------------------|                                                                                                                                                                                        
# | year | artist | title | genre | duration | tempo |                                                                                                                                                                                        
#  --------------------------------------------------                                                                                                                                                                                         
def make2DList(filename):
    fileObj = open(filename)
    lines = fileObj.readlines()
    fileObj.close()

    resultList = []
    index = 0

    while index < len(lines):
        line = lines[index].strip().split(",")
        line[YEAR]     = int(line[YEAR])
        line[DURATION] = float(line[DURATION])
        line[TEMPO]    = float(line[TEMPO])
        resultList.append(line)
        index += 1
    return resultList
###############  
# DON'T TOUCH #                                                                                                                                                                                                                               
###############                                                                                                                                                                                                                               
############################################################################                                                                                                                                                                  
# make2DList() constructs a 2D list from a file that contains information                                                                                                                                                                     
#              about songs in a music library, such as year and artist                                                                                                                                                                        
# Input:       filename;   a string of the music library's file name                                                                                                                                                                          
# Output:      resultList; a 2D list of that file in the format below                                                                                                                                                                         
#  __________________________________________________                                                                                                                                                                                         
# |   0  |    1   |   2   |   3   |     4    |   5   |                                                                                                                                                                                        
# |------|--------|-------|-------|----------|-------|                                                                                                                                                                                        
# | year | artist | title | genre | duration | tempo |                                                                                                                                                                                        
# |--------------------------------------------------|                                                                                                                                                                                        
# | year | artist | title | genre | duration | tempo |                                                                                                                                                                                        
# |--------------------------------------------------|                                                                                                                                                                                        
# | year | artist | title | genre | duration | tempo |                                                                                                                                                                                        
# |--------------------------------------------------|                                                                                                                                                                                        
# | year | artist | title | genre | duration | tempo |                                                                                                                                                                                        
#  --------------------------------------------------                                                                                                                                                                                         
def make2DList(filename):
    fileObj = open(filename)
    lines = fileObj.readlines()
    fileObj.close()

    resultList = []
    index = 0

    while index < len(lines):
        line = lines[index].strip().split(",")
        line[YEAR]     = int(line[YEAR])
        line[DURATION] = float(line[DURATION])
        line[TEMPO]    = float(line[TEMPO])
        resultList.append(line)
        index += 1
    return resultList
###############                                                                                                                                                                                                                               
# DON'T TOUCH #                                                                                                                                                                                                                               
###############                                                                                                                                                                                                                               

# OTHER FUNCTIONS GO HERE #                                                                                                                                                                                                                   

###########################################                                                                                                                                                                                                   
# mainMenuLoop () loops the main menu     #                                                                                                                                                                                                   
# Input:          prompt; the users input #                                                                                                                                                                                                   
# Output:         newPrompt; returned int #                                                                                                                                                                                                   
#                 value                   #                                                                                                                                                                                                   
###########################################                                                                                                                                                                                                   
def mainMenuLoop():
    displayMainMenu()
    prompt = "Enter a menu choice (0 - 1) or '-1' to exit: "
    newPrompt = getValidInput(prompt, MIN_SEARCH, MAX_SEARCH)
    return newPrompt

#############################################################                                                                                                                                                                                 
# displayMainMenu() prints out the main menu of the program #                                                                                                                                                                                 
# Input:            none                                    #                                                                                                                                                                                 
# Output:           none                                    #                                                                                                                                                                                 
#############################################################                                                                                                                                                                                 
def displayMainMenu():
    print("\n")
    print("What would you like to do next?")
    print("\t" "0) Perform a search")
    print("\t" "1) Create a playlist")
    print("\n")

#############################################################                                                                                                                                                                                 
# displayOptions() prints out a list of the six             #                                                                                                                                                                                 
#                  different attributes shown for each song #                                                                                                                                                                                 
# Input:           none                                     #                                                                                                                                                                                 
# Output:          none                                     #                                                                                                                                                                                 
#############################################################                                                                                                                                                                                 
def displayOptions():
    print("\t" "Index Value")
    print("\t" "0 - Year")
    print("\t" "1 - Artist")
    print("\t" "2 - Title")
    print("\t" "3 - Genre")
    print("\t" "4 - Duration")
    print("\t" "5 - Tempo")
###################################################################################                                                                                                                                                           
# displayPLOptions() prints out the three different options for creating playlist #                                                                                                                                                           
# Input:             none                                                         #                                                                                                                                                           
# Output:            none                                                         #                                                                                                                                                           
###################################################################################                                                                                                                                                           
def displayPLOptions():
    print("\n")
    print("What playlist type do you want to create?")
    print("1) Year Playlist")
    print("2) Artist Playlist")
    print("3) Genre Playlist")

######################################################################                                                                                                                                                                        
# printSongs() prints the details of every song in the given 2D list #                                                                                                                                                                        
# Input:       songs; 2D list of songs                               #                                                                                                                                                                        
# Output:      none                                                  #                                                                                                                                                                        
######################################################################                                                                                                                                                                        
def printSongs(songs):
    print("\n")
    print("Found the following: ")
    counter = 0
    while counter < len(songs):
        print(songToString(songs[counter]))
        counter += 1

###########################################################                                                                                                                                                                                   
# songToString() converts a songs information to a string #                                                                                                                                                                                   
# Input:         songs; 1D list of songs                  #                                                                                                                                                                                   
# Output:        finalString; the song to a final string  #                                                                                                                                                                                   
###########################################################         
def songToString(songs):
    finalString = " "
    finalString = str(songs[YEAR]) + " - " + songs[GENRE] + " - " + songs[ARTIST] + " - " + songs[TITLE]
    return finalString

##################################################################                                                                                                                                                                            
# getValidInput() gets a valid integer from the user that        #                                                                                                                                                                            
#                 falls within the appropriate range; uses       #                                                                                                                                                                            
#                 a prompt provided at function call             #                                                                                                                                                                            
# Input:          prompt;  a string to use when asking for input #                                                                                                                                                                            
#                 minimum; a minimum integer                     #                                                                                                                                                                            
#                 maximum; a maximum integer                     #                                                                                                                                                                            
# Output:         userInput; an integer within the range         #                                                                                                                                                                            
##################################################################                                                                                                                                                                            
def getValidInput(prompt, minimum, maximum):
    userInput = int(input(prompt))
    while userInput <= minimum or userInput >= maximum:
        print("You entered an invalid input.")
        userInput = int(input(prompt))
    return userInput

#############################################################################                                                                                                                                                                 
# colToString() converts a number to the corresponding column heading       #                                                                                                                                                                 
# Input:        column; an integer                                          #                                                                                                                                                                 
# Ouput:        columnHeading; a string containing the column heading       #                                                                                                                                                                 
#############################################################################        
def colToString(column):
    columnHeading = " "
    if column == YEAR:
        columnHeading = "Year"
    elif column == ARTIST:
        columnHeading = "Artist"
    elif column == TITLE:
        columnHeading = "Title"
    elif column == GENRE:
        columnHeading = "Genre"
    elif column == DURATION:
        columnHeading = "Duration"
    elif column == TEMPO:
       columnHeading = "Tempo"
    return columnHeading

##########################################################################                                                                                                                                                                    
# search() create a 2D list of all of the values that are being searched #                                                                                                                                                                    
# Input:   songs; 2D list                                                #                                                                                                                                                                    
#          col; int between 0-5. LOOK AT CONSTANTS                       #                                                                                                                                                                    
#          value; value being searched for                               #                                                                                                                                                                    
# Output:  searchList; 2D list returned that contains                    #                                                                                                                                                                    
#          the values being searched for                                 #                                                                                                                                                                    
##########################################################################                     
def search(songs, col, value):

    searchList = []
    counter = 0
    if col == YEAR or col == ARTIST or col == TITLE or col == GENRE:
        # iterate through 2D list #                                                                                                                                                                                                           
        while counter < len(songs):
            if songs[counter][col] == value:
                searchList.append(songs[counter])
            counter += 1

    elif col == DURATION or col == TEMPO:
        # iterate through 2D list #                                                                                                                                                                                                           
        while counter < len(songs):
            if songs[counter][col] >= value:
                searchList.append(songs[counter])
            counter += 1
    return searchList

###############################################################                                                                                                                                                                               
# createPlaylist() create a 2D list of all of the values that #                                                                                                                                                                               
#                  are being searched                         #                                                                                                                                                                               
# Input:           songs; list of 2D songs                    #                                                                                                                                                                               
#                  choice; int between 1-3                    #                                                                                                                                                                               
#                  length; int between 0-10                   #                                                                                                                                                                               
# Output:          playList; 2D list returned that contains   #                                                                                                                                                                               
#                  the values being searched for              #                                                                                                                                                                               
###############################################################                                                                                                                                                                               
def createPlaylist(songs, choice, length):

    # playlist - YEAR #                                                                                                                                                                                                                       
    if choice == PL_YEAR:
        choice = YEAR
        col = choice
        value = int(input("Enter a year to make a playlist of: "))
        playList = search(songs, col, value)
        newList = []
        counter = 0
        # control length #                                                                                                                                                                                                                    
        while counter < length and counter < len(playList):
                newList.append(playList[counter])
                counter += 1
        if newList == []:
            print("Sorry, that year", value, "doesn't exist in your library.")
        else:
            printSongs(newList)

    # playlist - ARTIST #                                                                                                                                                                                                                     
    elif choice == PL_ARTIST:
        choice = ARTIST
        col = choice
        value = str(input("Enter an artist to make a playlist of: "))
        playList = search(songs, col, value)
        newList = []
        counter = 0
        # control length #                                                                                                                                                                                                                    
        while counter < length and counter < len(playList):
            newList.append(playList[counter])
            counter += 1
        if newList == []:
            print("Sorry, that artist", value, "doesn't exist in your library.")
        else:
            printSongs(newList)

    # playlist - GENRE #                                                                                                                                                                                                                      
    elif choice == PL_GENRE:
        choice = GENRE
        col = choice
        value = str(input("Enter an genre to make a playlist of: "))
        playList = search(songs, col, value)
        newList = []
        counter = 0
        # control length #                                                                                                                                                                                                                    
        while counter < length and counter < len(playList):
            newList.append(playList[counter])
            counter += 1
        if newList == []:
            print("Sorry, that genre", value, "doesn't exist in your library.")
        else:
            printSongs(newList)

    return newList

########                                                                                                                                                                                                                                      
# MAIN #                                                                                                                                                                                                                                      
########                                                                                                                                                                                                                                      
def main():
    print("This is the Music Organizer 3000!" "\n")

    # FILENAME #                                                                                                                                                                                                                              
    filename = input("Enter the filename of your song library: ")
    songs = make2DList(filename)
    # MENU #                                                                                                                                                                                                                                  
    displayMainMenu()
    prompt = "Enter a menu choice (0 - 1) or '-1' to exit: "
    newPrompt = getValidInput(prompt, MIN_SEARCH, MAX_SEARCH)

    # WHILE != USER_QUIT #                                                                                                                                                                                                                    
    while newPrompt != USER_QUIT:

        # SEARCH - 0 #                                                                                                                                                                                                                        
        if newPrompt == MENU_SEARCH:
            displayOptions()
            prompt = "Enter a column choice (0 - 5): "
            newPrompt = getValidInput(prompt, MIN_OPTION, MAX_OPTION)

            # YEAR #                                                                                                                                                                                                                          
            if newPrompt == YEAR:
                column = newPrompt
                searchCol = colToString(column)
                col = newPrompt
                value = int(input("Enter the value you want to search for YEAR: "))
                search(songs, col, value)
                # print if search returned results or not #                                                                                                                                                                                   
                if search(songs, col, value) == []:
                    print("Your search returned no results.")
                else:
                    printSongs(search(songs, col, value))

            # ARTIST #                               
                       elif newPrompt == ARTIST:
                column = newPrompt
                searchCol = colToString(column)
                col = newPrompt
                value = str(input("Enter the value you want to search for ARTIST: "))
                search(songs, col, value)
                # print if search returned results or not #                                                                                                                                                                                   
                if search(songs, col, value) == []:
                    print("Your search returned no results.")
                else:
                    printSongs(search(songs, col, value))

            # TITLE #                                                                                                                                                                                                                         
            elif newPrompt == TITLE:
                column = newPrompt
                searchCol = colToString(column)
                col = newPrompt
                value = str(input("Enter the value you want to search for TITLE: "))
                search(songs, col, value)
                # print if search returned results or not #                                                                                                                                                                                   
                if search(songs, col, value) == []:
                    print("Your search returned no results.")
                else:
                    printSongs(search(songs, col, value))

            # GENRE #                                                                                                                                                                                                                         
            elif newPrompt == GENRE:
              column = newPrompt
                searchCol = colToString(column)
                col = newPrompt
                value = str(input("Enter the value you want to search for GENRE: "))
                search(songs, col, value)
                # print if search returned results or not #                                                                                                                                                                                   
                if search(songs, col, value) == []:
                    print("Your search returned no results.")
                else:
                    printSongs(search(songs, col, value))

            # DURATION #                                                                                                                                                                                                                      
            elif newPrompt == DURATION:
                column = newPrompt
                searchCol = colToString(column)
                col = newPrompt
                value = int(input("Enter the value you want to search for DURATION: "))
                search(songs, col, value)
                # print if search returned results or not #                                                                                                                                                                                   
                if search(songs, col, value) == []:
                    print("Your search returned no results.")
                else:
                    printSongs(search(songs, col, value))

            # TEMPO #                                                                                                                                                                                                                         
            elif newPrompt == TEMPO:
                column = newPrompt
              searchCol = colToString(column)
                col = newPrompt
                value = int(input("Enter the value you want to search for TEMPO: "))
                search(songs, col, value)
                # print if search returned results or not #                                                                                                                                                                                   
                if search(songs, col, value) == []:
                    print("Your search returned no results.")
                else:
                    printSongs(search(songs, col, value))

        # PLAYLIST - 1 #                                                                                                                                                                                                                      
        elif newPrompt == MENU_CREATE:
            displayPLOptions()
            prompt = "Choose a playlist to make: "
            newPrompt = getValidInput(prompt, PL_MIN, PL_MAX)

            # YEAR #                                                                                                                                                                                                                          
            if newPrompt == PL_YEAR:
                choice = newPrompt
                length = int(input("Enter the length of your playlist (0 - 10): "))
                # control PL length #                                                                                                                                                                                                         
                while length <= PL_LENGTHMIN or length >= PL_LENGTHMAX:
                    print("You entered an invalid input.")
                    length = int(input("Enter the length of your playlist (0 - 10): "))
                # print if search returned results or not #                                                                                                                                                                                   
                createPlaylist(songs, choice, length)
           # ARTIST #                                                                                                                                                                                                                        
            elif newPrompt == PL_ARTIST:
                choice = newPrompt
                length = int(input("Enter the length of your playlist (0 - 10): "))
                # control PL length #                                                                                                                                                                                                         
                while length <= PL_LENGTHMIN or length >= PL_LENGTHMAX:
                    print("You entered an invalid input.")
                    length = int(input("Enter the length of your playlist (0 - 10): "))
                # print if search returned results or not #                                                                                                                                                                                   
                createPlaylist(songs, choice, length)

            # GENRE #                                                                                                                                                                                                                         
            elif newPrompt == PL_GENRE:
                choice = newPrompt
                length = int(input("Enter the length of your playlist (0 - 10): "))
                # control PL length #                                                                                                                                                                                                         
                while length <= PL_LENGTHMIN or length >= PL_LENGTHMAX:
                    print("You entered an invalid input.")
                    length = int(input("Enter the length of your playlist (0 - 10): "))
                # print if search returned results or not #                                                                                                                                                                                   
                createPlaylist(songs, choice, length)

        # loop until USER_QUIT #                                                                                                                                                                                                              
        newPrompt = mainMenuLoop()
    print("Thank you for using the Music Organizer 3000, come again!")

main()






