import ReactMarkdown from "react-markdown";

const Main = ({ activeNote, onUpdateNote }) => {

  
  const onEditField = (field, value) => {
    onUpdateNote({
      ...activeNote,
      [field]: value,
      lastModified: Date.now(),
    });
  };

  /* if (!activeNote) return <div className="no-active-note">No Active Note</div>; */
  if (!activeNote) return <></>;

  return (
    <div className="app-main">
      <div className="app-main-note-edit">
        <input
          type="text"
          id="title"
          placeholder="제목"
          value={activeNote.title}
          onChange={(e) => onEditField("title", e.target.value)}
          autoFocus
        />
        <textarea
        style={{height:"100px"}}
          id="body"
          placeholder="내용"
          value={activeNote.body}
          onChange={(e) => onEditField("body", e.target.value)}
        />
      </div>
{/*       <div className="app-main-note-preview">
        <h1 className="preview-title">{activeNote.title}</h1>
        <ReactMarkdown className="markdown-preview">
          {activeNote.body}
        </ReactMarkdown>
      </div> */}
    </div>
  );
};

export default Main;
