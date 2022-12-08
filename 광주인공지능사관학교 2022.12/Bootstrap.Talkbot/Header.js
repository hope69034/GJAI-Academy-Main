import { Navbar } from "react-bootstrap";
/* 뒤로가기 */
import { useNavigate } from "react-router-dom";
import React from "react";
 
/* import HistorySample from '../../../HistorySample'; */

function Header() {
  //뒤로가기 구현
  const navigate = useNavigate();
  // 인덱스로 처리, 두번 뒤로 가고싶으면 -2
  const handleGoBack = () => {
    navigate(-1);
  };
  // 홈으로 가기
  //const handleGoHome = () => {navigate('/');}

  return (
    <>
      <Navbar variant="dark" className="header-container">
        <Navbar.Brand className="header-title-container">
            {/* 뒤로가기 버튼 */}
            <button className="hisSampleButton" name="back" onClick={handleGoBack}>
            <a class="sc-eDWCr gvCYGp rsc-header-close-button"><svg height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path><path d="M0 0h24v24H0z" fill="none"></path></svg></a>
            </button>
            {/* <button name="go" onClick={handleGoHome}>홈으로</button> */}
          <h3> Greenee</h3>
        </Navbar.Brand>
      </Navbar>
    </>
  );
}

export default Header;
