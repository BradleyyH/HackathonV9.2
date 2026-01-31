pieces = ["p", "b", "h", "r", "q", "k"]

def makeGrid(size):
    grid = [['' for _ in range(size)] for _ in range(size)]#
    return grid

def addPieces(grid):
    layout = "rhbqkbhr"
    data = [["w", 6], ["b", 1]]
    for d in data:
        y, clr = d[1], d[0]
        for x in range(8):
            grid[y][x] = "0"+clr

    for y in [0,7]:
        clrs = ["b", "w"]
        clr = clrs[y%2]
        for x, s in enumerate(layout):
            grid[y][x] = str(pieces.index(s)) + clr

    return grid

board = makeGrid(8)
addPieces(board)

turnIndex = -1
teams = ["white", "black"]
while True:
    turnIndex += 1
    currentTeam = teams[turnIndex%2]

    for x in board:
        print(x)

    print(f"Current team: {currentTeam}")
    cstr = input("Enter coordinate of piece: ")
    c1 = [int(cstr[0]), int(cstr[1])]
    print(c1)
    dstr = input("Enter destination coordinate: ")
    c2 = [int(dstr[0]), int(dstr[1])]

    piece = board[c1[0]-1][c1[1]-1]
    board[c1[0]-1,c1[1]-1] = ''
    board[c2[0]-1,c2[1]-1] = piece

    

grid = makeGrid(8)
addPieces(grid) 
    