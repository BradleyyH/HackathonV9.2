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
    console.log('🔌 Connected to server via Socket.IO');

    newSocket.on('moves', (move) => {
      const gameCopy = new Chess(game.fen());
      gameCopy.move(move);
      setGame(gameCopy);
      console.log('📥 Move received from server:', move);
    });

    return () => newSocket.close();
}, []);

 function onDrop(sourceSquare, targetSquare) {
    console.log('🚨 ONDROP CALLED!!!', sourceSquare, targetSquare); 
    console.log('🖱️ Piece dropped from', sourceSquare, 'to', targetSquare);
    
    try {
      const gameCopy = new Chess(game.fen());
      console.log('📋 Current FEN before move:', gameCopy.fen());
      
      const move = gameCopy.move({
        from: sourceSquare,
        to: targetSquare,
        promotion: 'q'
      });
      
      console.log('🎯 Move attempted:', move);
      
      if (move === null) {
        console.log('❌ Move is ILLEGAL');
        return false;
      }
      
      console.log('✅ Move is LEGAL');
      console.log('📋 New FEN after move:', gameCopy.fen());
      
      
      if (socket) {
        console.log('📤 Sending move to server:', {
          from: sourceSquare,
          to: targetSquare,
          promotion: 'q'
        });
        socket.emit('moves', {
            from: sourceSquare,
            to: targetSquare,
            promotion: 'q'
        });
      } else {
        console.log('⚠️ Socket is null, cannot send move');
      }
      
      return true;
    } catch (error) {
      console.log('💥 ERROR during move:', error);
      return false;
    }
  }

  return (
    <div style={{ width: '1000px', margin: 'auto', paddingTop: '50px' }}>
      <h1>4v4 Chess</h1>
      {console.log('🎨 Rendering Chessboard with position:', game.fen())}
      <Chessboard position={game.fen()} onPieceDrop={onDrop} isDraggablePiece={() => true} />
    </div>
  );
}

export default ChessBoard;