import React, { Component } from "react";
import PropTypes from "prop-types";
import axios from "axios";
//import { useSelector } from "react-redux";
//import { useEffect, useState } from "react";

class ChatbotReview extends Component {
  constructor(props) {
    super(props);
    this.state = {
      wake: "",
      startwork: "",
      lunch: "",
      endwork: "",
      transport: "",
      job: "",
      hobby: "",
      music: "",
      food: "",
      drink: "",
    };
  }
  componentWillMount() {
    const { steps } = this.props;
    const {
      wake,
      startwork,
      lunch,
      endwork,
      transport,
      job,
      hobby,
      music,
      food,
      drink,
    } = steps;
    this.setState({
      wake,
      startwork,
      lunch,
      endwork,
      transport,
      job,
      hobby,
      music,
      food,
      drink,
    });
  }
  render() {
    let {
      wake,
      startwork,
      lunch,
      endwork,
      transport,
      job,
      hobby,
      music,
      food,
      drink,
    } = this.state;
    let data = {
      wake: wake.value,
      startwork: startwork.value,
      lunch: lunch.value,
      endwork: endwork.value,
      transport: transport.value,
      job: job.value,
      hobby: hobby.value,
      music: music.value,
      food: food.value,
      drink: drink.value,
    };

    /* 라우터에서 req.body.transport */
    axios
      .post("http://127.0.0.1:5000/chatbotUpdate", data)
      .then((res) => {
        console.log("라우터다녀옴");
        console.log("res: " + res);
      })
      .catch((res) => {
        console.log("error");
      });

    return (
      <form>
        <div style={{ width: "100%" }}>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            기상시간 :{" "}
          </qq>
          {wake.value}
          <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            출근시간 :{" "}
          </qq>
          {startwork.value}
          <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            점심시간 :{" "}
          </qq>
          {lunch.value}
          <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            퇴근시간 :{" "}
          </qq>
          {endwork.value}
          <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            교통수단 :{" "}
          </qq>
          {transport.value}
          <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            직업 :{" "}
          </qq>
          {job.value}
          <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            취미 :{" "}
          </qq>
          {hobby.value} <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            좋아하는 음악 :{" "}
          </qq>
          {music.value}
          <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            좋아하는 음식 :{" "}
          </qq>
          {food.value}
          <br></br>
          <qq style={{ fontSize: "15px", fontWeight: "bold", color: "white" }}>
            좋아하는 음료 :{" "}
          </qq>
          {drink.value}
          <br></br>
          <button
            type="submit"
            style={{
              border: "5px solid",
              borderRadius: "60px 60px 20px",
              borderColor: "#f39c12",
              color: "white",
              background: "#f39c12",
              marginTop: "8px",
            }}
          >
            {" "}
            응, 앞으로 잘 부탁해{" "}
          </button>
        </div>
      </form>
    );
  }
}
ChatbotReview.propTypes = {
  steps: PropTypes.object,
};
ChatbotReview.defaultProps = {
  steps: undefined,
};
export default ChatbotReview;
