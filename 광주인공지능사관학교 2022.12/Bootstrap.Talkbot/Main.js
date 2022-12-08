import React from "react";
import { Toast, ToastContainer } from "react-bootstrap";
/* import a2 from "../../../img/greenee.png"; */
import a1 from "../../../img/a1.jpg";
import a2 from "../../../img/a2.jpg";
import a3 from "../../../img/a3.jpg";
import a4 from "../../../img/a4.jpg";
import a5 from "../../../img/a5.jpg";
import a6 from "../../../img/a6.jpg";
import a7 from "../../../img/a7.jpg"; 
let avatarArray = [a1,a2,a3,a4,a5,a6,a7]
let avatar = avatarArray[Math.floor(Math.random() * avatarArray.length)]

function Main(props) {
  return (
    <main className="main-container">
      <ToastContainer bsPrefix="toast-main-container">
        {props.message.map((item) =>
          item.from ? (
            /* bg:버블컬러 */
            <Toast bg="warning" className="my-message">
              <Toast.Body>{item.msg}</Toast.Body>
            </Toast>
          ) : (
            <Toast className="other-message">
              <Toast.Body>
                <img
                  src={avatar}
                  className={"a2"}
                  style={{ width: "2px", padding: "0px" }}
                />
                {item.msg}
              </Toast.Body>
            </Toast>
          )
        )}
      </ToastContainer>
    </main>
  );
}
export default Main;
