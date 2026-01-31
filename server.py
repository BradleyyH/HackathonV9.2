import flask

def makeGrid(size, fill=0):
    return [[fill for _ in range(size)] for _ in range(size)]

