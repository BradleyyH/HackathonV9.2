function startScreen() {
    return (
        <div>
            <h1>
                welcome to 4v4 chess
            </h1>
            <button onClick="startGame()">Start Game</button>
            <img src="chessBoard.png" alt="Chess Board" />
            <style>
                {`body { background-color: #2f4238; }`}
                {`h1 { color: #22b854; text-align: center; font-family: 'Arial', sans-serif; }`}
            </style>
        </div>
    );
}