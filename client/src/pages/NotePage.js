import React, { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { ReactComponent as ArrowLeft } from "../assets/arrow-left.svg";
// import notes from "../assets/data";

const NotePage = () => {
  //please check this link for navigate
  // https://reactrouter.com/en/v6.3.0/upgrading/v5#use-usenavigate-instead-of-usehistory
  const navigate = useNavigate();

  // console.log(useParams());
  const { id: noteId } = useParams();

  const [note, setNote] = useState(null);

  // using Api to replace the local file
  // const note = notes.find((note) => note.id === Number(id));
  //   console.log(note);

  useEffect(() => {
    getNote();
  }, [noteId]);

  const getNote = async () => {
    if (noteId === "new") return;
    const response = await fetch(`http://localhost:8000/Notes/${noteId}`);
    const data = await response.json();
    // console.log(data);
    setNote(data);
  };

  // * This is the function we do put request on API
  const createNote = async () => {
    console.log("Note Created");
    await fetch(`http://localhost:8000/Notes/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...note, updated: new Date() }),
    });
  };

  // * This is the function we do put request on API
  const updateNote = async () => {
    await fetch(`http://localhost:8000/Notes/${noteId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...note, updated: new Date() }),
    });
  };

  // * This is the function we do DELETE request on API
  const deleteNote = async () => {
    await fetch(`http://localhost:8000/Notes/${noteId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(note),
    });
    navigate("/");
  };

  const handleSubmit = () => {
    if (noteId !== "new" && !note.body) {
      deleteNote();
    } else if (noteId !== "new") {
      updateNote();
    } else if (noteId === "new" && note != null) {
      createNote();
    }

    navigate("/");
  };

  return (
    <div className="container dark">
      <div className="app">
        <div className="note">
          <div className="note-header">
            <h3>
              <Link to="/">
                <ArrowLeft onClick={handleSubmit} />
              </Link>
            </h3>
            {noteId !== "new" ? (
              <button onClick={deleteNote}>Delete</button>
            ) : (
              <button onClick={handleSubmit}>Done</button>
            )}
          </div>

          <textarea
            onChange={(e) => {
              // console.log(e);
              setNote({ ...note, body: e.target.value });
            }}
            value={note?.body}
          ></textarea>
        </div>
      </div>
    </div>
  );
};

export default NotePage;
