import { useEffect, useState } from 'react';
import { Chessboard } from 'react-chessboard';
import { Chess } from 'chess.js';
import io from 'socket.io-client';

function ChessBoard() {
  const [game, setGame] = useState(new Chess());
  const [socket, setSocket] = useState(null);

 

  useEffect(() => {
    const newSocket = io('http://10.2.189.7:5000/');
    setSocket(newSocket);

    newSocket.on('move', (move) => {
      const gameCopy = new Chess(game.fen());
      gameCopy.move(move);
      setGame(gameCopy);
    });

    return () => newSocket.close();
}, []);

  function onDrop(sourceSquare, targetSquare) {
    try {
      const gameCopy = new Chess(game.fen());
      const move = gameCopy.move({
        from: sourceSquare,
        to: targetSquare,
        promotion: 'q'
      });
      
      if (move === null) return false;
      
      setGame(gameCopy);
      
      if (socket) {
        socket.emit('moves', {
            from: sourceSquare,
            to: targetSquare,
            promotion: 'q'
        });
      }
      return true;
    } catch (error) {
      return false;
    }
  }

  return (
    <div className="chess-board-container">
      <Chessboard 
        position={game.fen()} 
        onPieceDrop={onDrop}
        boardWidth={600}
      />
    </div>
  );
}

export default ChessBoard;