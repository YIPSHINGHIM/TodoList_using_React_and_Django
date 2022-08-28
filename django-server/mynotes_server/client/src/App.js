import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import "./App.css";
import Header from "./components/Header";
import NotePage from "./pages/NotePage";
import NotesListPage from "./pages/NotesListPage";

// project tutorial about react b  
// https://www.youtube.com/watch?v=6fM3ueN9nYM

function App() {
  // Wrap multiple elements into a single variable
  const appElements = (
    <div className="container dark">
      <div className="app">
        <Header />
        <NotesListPage />
      </div>
    </div>
  );

  // we can pass the wrapped elements to a single path
  // Or pass an element directly
  return (
    <Router>
      <Routes>
        <Route path="/" exact element={appElements} />
        <Route path="/note/:id" exact element={<NotePage />} />
      </Routes>
    </Router>
  );
}

export default App;
