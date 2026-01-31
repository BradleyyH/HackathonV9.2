import './App.css'
import './styles.css'
import ChessBoard from './pages/ChessBoard';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="app-container">
        <h1>Chess 4v4</h1>
        <Routes>
          <Route path="/" element={<ChessBoard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App
