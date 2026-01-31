import './App.css'
import './styles.css'
import ChessBoard from './pages/ChessBoard';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";

function App() {

  return (
    <Router>
      <div>
        <h1>Chess 4v4</h1>
      </div>
    

    <Routes>
      <Route path="/" element={<ChessBoard />} />
      
    </Routes>
    </Router>
  );
}

export default App
