from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import board, move, piece, position, move_validator

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

from board import *
from move import *
from piece import *
from position import *
from move_validator import *

app = Flask(__name__)
allowed_origins = [
    "http://10.2.27.52:3000",
    "http://localhost:3000",
]

CORS(app, origins=allowed_origins)
socketio = SocketIO(app, cors_allowed_origins=allowed_origins)

# Dictionary to store users and their assigned rooms
players = {}

@app.route('/')
def index():
    return '<p>hello<p>'

testBoard = Board()
testBoard.initialise()

# Handle new user joining
@socketio.on('join')
def handle_join(username):
    if not players.get(request.sid):
        players[request.sid] = "P"+len(players)
    join_room(players[request.sid])  # Each user gets their own "room"
    emit("message", f"{username} joined the chat", room=username)

# Handle user messages
@socketio.on('message')
def handle_message(data):
    username = players.get(request.sid)  # Get the user's name
    emit("message", f"{username}: {data}", broadcast=True)  # Send to everyone

@socketio.on('moves')
def handle_move(data):
    print(data)
    print("asda")

# Handle disconnects
@socketio.on('disconnect')
def handle_disconnect():
    username = players.pop(request.sid, "Anonymous")
    emit("message", f"{username} left the chat", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")