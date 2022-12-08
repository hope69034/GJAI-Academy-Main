/* import */
import React, { Component } from "react";
import ChatBot from "react-simple-chatbot";
import ChatbotReview from "./ChatbotReview";
import { ThemeProvider } from "styled-components";
/* 랜덤 아바타 펑션용 임포트 */
import a1 from "../../../img/a1.jpg";
import a2 from "../../../img/a2.jpg";
import a3 from "../../../img/a3.jpg";
import a4 from "../../../img/a4.jpg";
import a5 from "../../../img/a5.jpg";
import a6 from "../../../img/a6.jpg";
import a7 from "../../../img/a7.jpg";
/* export */
class ChatbotSteps extends Component {
  render(props) {
    const config = {
      steps: steps, //인풋아웃풋대본
      headerTitle: "Greenee", //채팅창 타이틀
      className: "greeniChatbot", //클래스네임(CSS를위한)(채팅창외부)
      hideUserAvatar: "true",
      placeholder: "  자신의 정보를 입력해 주세요.",
      botDelay:  0,
      footerStyle: { background: "#efefef" },
      bubbleOptionStyle: { background: "#f39c12" },
      botAvatar: avatarArray[Math.floor(Math.random() * avatarArray.length)],
      floating: "true", /* 채팅창 버튼으로 자동 플로팅 */
      floatingStyle: floatingStyle,
      //floatingIcon={greenihead},
      //submitButtonStyle:{},
      //inputStyle:{},
      //width: {},
      //height: {},
    };
    return (
      <>
        <ThemeProvider theme={lightTheme}>
          <div
            style={{
              marginRight: "-1px",
              marginTop: "-7.73px",
              borderColor: "#fff",
            }}
          >
            <ChatBot {...config} />
          </div>
        </ThemeProvider>
      </>
    );
  }
}
export default ChatbotSteps;
/* 봇아바타랜덤돌리기 */
/* Math.random() 함수는 0 ~ 1 사이의 숫자를 반환합니다. 그리고 0과 배열의 마지막
인덱스 사이의 값을 구하기 위해서는 Math.random() 함수와 배열의 length를 곱합니다.
마지막으로 Math.random() 함수의 반환 값 * 배열의 length는 정수 또는 실수이므로 
Math.floor() 함수를 호출하여 정수로 반올림합니다. */
let avatarArray = [a1,a2,a3,a4,a5,a6,a7]
let firstArray = [
  "AI비서 그리니입니다. 회원님의 정보가 필요합니다.",
  "만나서 반갑습니다. 그리니입니다.",
  "Load Complete, AI Secretary 'Greenee'",
  "회원님의 정보를 받겠습니다.",
];
let secondArray = ["", "", "", "", "네. 그럼, ", "음, ", "그럼, ", "네. "];
let transportArray = [
  "교통수단은 무엇인가요? ",
  "교통수단을 여쭤봐도 되겠습니까? ",
  "교통수단을 알려주시면 정말 감사하겠습니다. ",
  "교통수단 정보가 필요합니다. ",
];
let jobArray = [
  "직업은 무엇인가요? ",
  "직업을 여쭤봐도 되겠습니까? ",
  "직업을 알려주시면 정말 감사하겠습니다. ",
  "직업 정보가 필요합니다. ",
];
let hobbyArray = [
  "취미는 무엇인가요? ",
  "취미를 여쭤봐도 되겠습니까? ",
  "취미를 알려주시면 정말 감사하겠습니다. ",
  "취미 정보가 필요합니다. ",
];
let musicArray = [
  "좋아하는 음악은 무엇인가요? ",
  "좋아하는 음악을 여쭤봐도 되겠습니까? ",
  "좋아하는 음악을 알려주시면 정말 감사하겠습니다. ",
  "좋아하는 음악 정보가 필요합니다. ",
];
let foodArray = [
  "좋아하는 음식은 무엇인가요? ",
  "좋아하는 음식을 여쭤봐도 되겠습니까? ",
  "좋아하는 음식을 알려주시면 정말 감사하겠습니다. ",
  "좋아하는 음식 정보가 필요합니다. ",
];
let drinkArray = [
  "좋아하는 음료는 무엇인가요? ",
  "좋아하는 음료를 여쭤봐도 되겠습니까? ",
  "좋아하는 음료를 알려주시면 정말 감사하겠습니다. ",
  "좋아하는 음료 정보가 필요합니다. ",
];
let thirdArray = [
  "",
  "",
  "",
  "",
  "잘 읽고 답변해 주시길 바랍니다.",
  "서비스에 필요한 정보입니다.",
  "궁금해요.",
  "언제든 수정이 가능합니다.",
  "답변에 따라 좋은 정보를 추천해드립니다.",
];
/* 첫인사 */
function randomF() {
  return firstArray[Math.floor(Math.random() * firstArray.length)];
}
/* 앞문장 */
function randomS() {
  return secondArray[Math.floor(Math.random() * secondArray.length)];
}
/* 중간문장 성향묻기 */
function randomTransport() {
  return transportArray[Math.floor(Math.random() * transportArray.length)];
}
function randomJob() {
  return jobArray[Math.floor(Math.random() * jobArray.length)];
}
function randomHobby() {
  return hobbyArray[Math.floor(Math.random() * hobbyArray.length)];
}
function randomMusic() {
  return musicArray[Math.floor(Math.random() * musicArray.length)];
}
function randomFood() {
  return foodArray[Math.floor(Math.random() * foodArray.length)];
}
function randomDrink() {
  return drinkArray[Math.floor(Math.random() * drinkArray.length)];
}
/* 뒷문장 */
function randomT() {
  return thirdArray[Math.floor(Math.random() * thirdArray.length)];
}
const steps = [
  {
    id: "0",
    message:  randomF(),
    trigger: "1",
  },
  {
    id: "1",
    message: "기상시간을 숫자 4개로 적어주세요. 0000 ~ 2459",
    trigger: "wake",
  },
  {
    id: "wake",
    user: true,
    trigger: "2",
    validator: (value) => {
      if (/^([0-1]?[0-9]|2[0-4])([0-5][0-9])(:[0-5][0-9])?$/.test(value)) {
        return true;
      } else {
        return "ex) 오후1시30분 > 1340";
      }
    },
  },
  {
    id: "2",
    message: "출근시간을 숫자 4개로 적어주세요. 0000 ~ 2459",
    trigger: "startwork",
  },
  {
    id: "startwork",
    user: true,
    trigger: "3",
    validator: (value) => {
      if (/^([0-1]?[0-9]|2[0-4])([0-5][0-9])(:[0-5][0-9])?$/.test(value)) {
        return true;
      } else {
        return "ex) 오후1시30분 > 1340";
      }
    },
  },

  {
    id: "3",
    message: "점심시간을 숫자 4개로 적어주세요. 0000 ~ 2459",
    trigger: "lunch",
  },
  {
    id: "lunch",
    user: true,
    trigger: "4",
    validator: (value) => {
      if (/^([0-1]?[0-9]|2[0-4])([0-5][0-9])(:[0-5][0-9])?$/.test(value)) {
        return true;
      } else {
        return "ex) 오후1시30분 > 1340";
      }
    },
  },
  {
    id: "4",
    message: "퇴근시간을 숫자 4개로 적어주세요. 0000 ~ 2459",
    trigger: "endwork",
  },
  {
    id: "endwork",
    user: true,
    trigger: "5",
    validator: (value) => {
      if (/^([0-1]?[0-9]|2[0-4])([0-5][0-9])(:[0-5][0-9])?$/.test(value)) {
        return true;
      } else {
        return "ex) 오후1시30분 > 1340";
      }
    },
  },
  {
    id: "5",
    message: randomS() + randomTransport() + randomT(),
    trigger: "transport",
  },
  {
    id: "transport",
    options: [
      { value: "자가용", label: "자가용", trigger: "6" },
      { value: "버스", label: "버스", trigger: "6" },
      { value: "택시", label: "택시", trigger: "6" },
      { value: "지하철", label: "지하철", trigger: "6" },
    ],
  },
  {
    id: "6",
    message: randomS() + randomJob() + randomT(),
    trigger: "job",
  },
  {
    id: "job",
    user: true,
    trigger: "7",
  },
  {
    id: "7",
    message: randomS() + randomHobby() + randomT(),
    trigger: "hobby",
  },
  {
    id: "hobby",
    user: true,
    trigger: "8",
  },
  {
    id: "8",
    message: randomS() + randomMusic() + randomT(),
    trigger: "music",
  },
  {
    id: "music",
    options: [
      { value: "클래식", label: "클래식", trigger: "9" },
      { value: "발라드", label: "발라드", trigger: "9" },
      { value: "힙합", label: "힙합", trigger: "9" },
      { value: "락", label: "락", trigger: "9" },
      { value: "트로트", label: "트로트", trigger: "9" },
      { value: "댄스", label: "댄스", trigger: "9" },
      { value: "인디", label: "인디", trigger: "9" },
    ],
  },
  {
    id: "9",
    message: randomS() + randomFood() + randomT(),
    trigger: "food",
  },
  {
    id: "food",
    options: [
      { value: "한식", label: "한식", trigger: "10" },
      { value: "중식", label: "중식", trigger: "10" },
      { value: "일식", label: "일식", trigger: "10" },
      { value: "양식", label: "양식", trigger: "10" },
      { value: "패스트푸드", label: "패스트푸드", trigger: "10" },
    ],
  },
  {
    id: "10",
    message: randomS() + randomDrink() + randomT(),
    trigger: "drink",
  },
  {
    id: "drink",
    options: [
      { value: "커피", label: "커피", trigger: "11" },
      { value: "차", label: "차", trigger: "11" },
      { value: "탄산음료", label: "탄산음료", trigger: "11" },
      { value: "프라페", label: "프라페", trigger: "11" },
    ],
  },
  {
    id: "11",
    message: "정확히 입력하셨나요?",
    trigger: "review",
  },
  {
    id: "review",
    component: <ChatbotReview />,
    asMessage: true,
    trigger: "update",
  },
  {
    id: "update",
    options: [
      { value: "no", label: "아니, 잘못 입력했어", trigger: "update-yes" },
      /* { value: 'yes', label: '네', trigger: 'end-message' }, */
    ],
  },
  {
    id: "update-yes",
    message: "수정할 정보를 선택하고 입력해주세요.",
    trigger: "update-fields",
  },
  {
    id: "update-fields",
    options: [
      { value: "기상시간", label: "기상시간", trigger: "update-wake" },
      { value: "출근시간", label: "출근시간", trigger: "update-startwork" },
      { value: "점심시간", label: "점심시간", trigger: "update-lunch" },
      { value: "퇴근시간", label: "퇴근시간", trigger: "update-endwork" },
      { value: "교통수단", label: "교통수단", trigger: "update-transport" },
      { value: "직업", label: "직업", trigger: "update-job" },
      { value: "취미", label: "취미", trigger: "update-hobby" },
      { value: "좋아하는음악", label: "좋아하는음악", trigger: "update-music" },
      { value: "좋아하는음식", label: "좋아하는음식", trigger: "update-food" },
      { value: "좋아하는음료", label: "좋아하는음료", trigger: "update-drink" },
    ],
  },
  {
    id: "update-wake",
    update: "wake",
    trigger: "11",
  },
  {
    id: "update-startwork",
    update: "startwork",
    trigger: "11",
  },
  {
    id: "update-lunch",
    update: "lunch",
    trigger: "11",
  },
  {
    id: "update-endwork",
    update: "endwork",
    trigger: "11",
  },
  {
    id: "update-transport",
    update: "transport",
    trigger: "11",
  },
  {
    id: "update-job",
    update: "job",
    trigger: "11",
  },
  {
    id: "update-hobby",
    update: "hobby",
    trigger: "11",
  },
  {
    id: "update-music",
    update: "music",
    trigger: "11",
  },
  {
    id: "update-food",
    update: "food",
    trigger: "11",
  },
  {
    id: "update-drink",
    update: "drink",
    trigger: "11",
  },
  /*   {
    id: "end-message",
    message: "정보를 수정했습니다.",
    end: true,
  },  
  {
        id: 'age',
        user: true,
        trigger: '7',
        validator: (value) => {
            if (isNaN(value)) {
                return 'value must be a number';
            } else if (value < 0) {
                return 'value must be positive';
            } else if (value > 120) {
                return `${value}? Come on!`;
            }
            return true;
        },
    }, 
      {
    id: 'startwork',
    user: true,
    trigger: '3',
    validator: (value) => {
        if (/^([0-1]?[0-9]|2[0-4])([0-5][0-9])(:[0-5][0-9])?$/.test(value)) {
          return true;
        }
        else {
          return 'ex) 오후1시30분 > 1340';
        }
    },
  },*/
];
const lightTheme = {
  background: "#f0fddd",
  fontFamily: "Helvetica Neue",
  headerBgColor: "#2ecc71",
  headerFontColor: "#fff",
  headerFontSize: "20px",
  botBubbleColor: "#2ecc71",
  botFontColor: "#fff",
  userBubbleColor: "#f39c12",
  userFontColor: "#fff",
};
/* 플로팅(채팅창 아이콘) 스타일 */
const floatingStyle = {
  background: "#2ecc71",
  marginRight: "300px",
  padding: "0px",
  bottom: "110px",
  /* border: "5px solid", */
  /* borderColor:'#7e7e7e', */
  /* Top: '100px', */
};
