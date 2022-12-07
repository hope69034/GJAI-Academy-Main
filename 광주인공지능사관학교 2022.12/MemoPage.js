import { useEffect, useState } from "react";
import uuid from "react-uuid";
import "../components/chatbot/MemoPageCompo/MemoPageCss.css";
import MemoPageCompo from "../components/chatbot/MemoPageCompo/MemoPageCompo";
import ClearIcon from '@mui/icons-material/Clear';
import AddIcon from '@mui/icons-material/Add';
function App() {
  const [notes, setNotes] = useState(
    localStorage.notes ? JSON.parse(localStorage.notes) : []
  );
  const [activeNote, setActiveNote] = useState(false);

  useEffect(() => {
    localStorage.setItem("notes", JSON.stringify(notes));
  }, [notes]);

  const onAddNote = () => {
    const newNote = {
      id: uuid(),
      title: "",
      body: "",
      lastModified: Date.now(),
    };

    setNotes([newNote, ...notes]);
    setActiveNote(newNote.id);
  };

  const onDeleteNote = (noteId) => {
    setNotes(notes.filter(({ id }) => id !== noteId));
  };

  const onUpdateNote = (updatedNote) => {
    const updatedNotesArr = notes.map((note) => {
      if (note.id === updatedNote.id) {
        return updatedNote;
      }

      return note;
    });

    setNotes(updatedNotesArr);
  };

  const getActiveNote = () => {
    return notes.find(({ id }) => id === activeNote);
  };

  /*  */
  const sortedNotes = notes.sort((a, b) => b.lastModified - a.lastModified);

  return (
    <div className="App">
      <div className="app-sidebar-header">
        {/* 헤더 */}
        <h1>메모</h1>
        <button className='addbt' onClick={onAddNote}>추가</button>
      </div>
      {/* 작성하는페이지 */}
      <MemoPageCompo activeNote={getActiveNote()} onUpdateNote={onUpdateNote} />
      {/*  목록 */}
      <div className="app-sidebar">
        <div className="app-sidebar-notes">
          {sortedNotes.map(({ id, title, body, lastModified }, i) => (
            <div
              className={`app-sidebar-note ${id === activeNote && "active"}`}
              onClick={() => setActiveNote(id)}
            >
              <div className="sidebar-note-title">
                <strong>{title}</strong>
                <button className='delbt' onClick={(e) => onDeleteNote(id)}>삭제</button>
              </div>
              <p>{body && body.substr(0, 100) + "..."}</p>
              <small className="note-meta">
                수정한 날짜{" "}
                {new Date(lastModified).toLocaleDateString("en-GB", {
                  hour: "2-digit",
                  minute: "2-digit",
                })}
              </small>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
export default App;
