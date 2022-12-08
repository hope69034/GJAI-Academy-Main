import React from "react";

import '../components/chatbot/talkbot/TalkChat.css';
import 'bootstrap/dist/css/bootstrap.min.css';

//import TalkChat from '../components/chatbot/talkbot/TalkChat'
import Header from '../components/chatbot/talkbot/Header';
import Main from '../components/chatbot/talkbot/Main';
import Footer from '../components/chatbot/talkbot/Footer';
import { useState } from 'react';

function ChatPage() {

  const [message, setMessage] = useState([{ msg: "안녕하세요. AI 비서 그리니입니다. '일상대화, '심리상담', '큐엔에이'를 하고 싶으시면 말씀만 하세요. 대화, 상담, qna라고 말씀하셔도 됩니다. 기본은 대화모드입니다.",  from: false }])

  const getMessage = (msg, from) => {
    setMessage((current) => [...current, ({ msg: msg, from: from })])
  }

  return (
    <>
      <Header />

      <Main message={message} />


      <Footer setMessage={getMessage} />




      

    </>
  );
};

export default ChatPage;
