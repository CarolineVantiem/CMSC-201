# CMSC-201
UMBC CMSC 201

Project 1 - Allow a user to “load in” a database of their choosing, and
to either (1) search the database, using any of the details listed above; or (2)
create a playlist of length 10 or less, based on year, artist, or genre. 

Project 2 - Simple cellular automata game, called
Conway's Game of Life. In this game, you have a grid where pixels can
either be on or off (dead or alive). In the game, as time marches on, there
are simple rules that govern whether each pixel will be on or off (dead or
alive) at the next time step.

Project 3 - (This assignment will focus on file I/O, manipulating lists, calling functions, and recursion.)
computing power of Python to solve a maze, using a recursive search algorithm. You will need to understand algorithms, 

Python data structures, file I/O, and recursion to complete this project.
The maze will be rectangular, comprised of square spaces. The Maze Solver
can move freely between two adjacent squares, as long as the movement is
horizontal or vertical (no diagonal moves), and the way is not blocked by a
wall. The dimensions, finishing square, and configuration of each maze are
provided in a separate file. The starting square from which the maze solution
is attempted is chosen by the user.

Your Maze Solver must use a recursive algorithm. Starting from the start
square, your algorithm will scan for all the adjacent squares it can legally
travel to in the next step. For each candidate “next square,” it will first check
that it has not already been there. If not, it will try adding that square to the
path built so far, and will use recursion to find a path from that new square to
the end. If that recursion fails, it moves on to the next candidate. If all “next
square” candidates fail, this instance of the recursion itself fails.
