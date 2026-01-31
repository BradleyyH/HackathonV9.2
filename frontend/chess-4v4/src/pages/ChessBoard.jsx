// src/pages/ChessBoard.jsx
import { useState } from 'react';
import { Chessboard } from 'react-chessboard';
import { Chess } from 'chess.js';

function ChessBoard() {
  const [game, setGame] = useState(new Chess());

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
      // TODO: WebSocket send to backend
      return true;
    } catch (error) {
      return false;
    }
  }

  return (
    <div style={{ width: '1000px', margin: 'auto', paddingTop: '50px' }}>
      <h1>4v4 Chess</h1>
      <Chessboard position={game.fen()} onPieceDrop={onDrop} />
    </div>
  );
}

export default ChessBoard;