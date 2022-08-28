import React from "react";
import { Link } from "react-router-dom";
// * we can now destructuring the props by using {}
// const hero = {
//     name: 'Batman',
//     realName: 'Bruce Wayne'
//   };

//   const { name, realName } = hero;
//   name;     // => 'Batman',
//   realName; // => 'Bruce Wayne'

const getTitle = (note) => {
  const title = note.body.split("\n")[0];

  if (title.length > 45) {
    return title.slice(0, 45) + " ...";
  }

  return title;
};

const getDate = (note) => {
  return new Date(note.updated).toLocaleDateString();
};

const getContent = (note) => {
  const title = getTitle(note);
  let content = note.body.replaceAll("\n", " ");
  content = content.replaceAll(title, " ");

  if (content.length > 40) {
    return " " + content.slice(0, 40) + " ...";
  } else {
    return content;
  }
};

const ListItem = ({ note }) => {
  return (
    <Link to={`/note/${note.id}`}>
      <div className="notes-list-item">
        <h3>{getTitle(note)}</h3>
        <p>
          <span>
            {getDate(note)}
            {getContent(note)}
          </span>
        </p>
      </div>
    </Link>
  );
};

export default ListItem;
