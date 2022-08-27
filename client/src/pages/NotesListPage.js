import React, { useEffect, useState } from "react";
// import notes from "../assets/data";
import AddButton from "../components/AddButton";
import ListItem from "../components/ListItem";

const NotesListPage = () => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    getNotes();
  }, []);

  const getNotes = async () => {
    console.log("testing");
    const response = await fetch("/api/notes/");
    const data = await response.json();

    console.log("data :", data);
    setNotes(data);
  };

  return (
    <div>
      <div className="notes">
        <div className="notes-header">
          <h2 className="notes-title">&#9782; Notes</h2>
          <p>{notes.length}</p>
        </div>

        <div className="notes-list">
          {notes.map((note, index) => (
            <ListItem key={index} note={note} />
          ))}
        </div>
      </div>
      <AddButton />
    </div>
  );
};

export default NotesListPage;
