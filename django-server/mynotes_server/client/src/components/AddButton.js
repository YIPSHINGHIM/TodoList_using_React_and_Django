import React from "react";
import { Link } from "react-router-dom";
import { ReactComponent as AddIcon } from "../assets/add.svg";

const AddButton = () => {
  return (
    // ? passing new as a id into the backend ny directing the user to /note/new url

    <Link to="/note/new" className="floating-button">
      <AddIcon />
    </Link>
  );
};

export default AddButton;
