import EventSource from "eventsource";
import { useEffect, useState } from "react";
import { Typography } from "@mui/material";

//! eventSource polyfill 때문에
//! npm uninstall react-scripts 한 후
//! npm i react-scripts@4.0.3 이거 설치함
//! 혹시나 에러 생기면 다시 react-scripts 최신 버전으로 설치할 것

const Sse = () => {
  // Server Sent Event 로 가져온 data를 화면에 보여주기 위한 state 변수
  const [sseDate, setSseDate] = useState();
  const [sseHeader, setSseHeader] = useState();

  useEffect(() => {
    // Server Sent Event 요청시 header에 auth-user를 설정하는 부분
    const eventSourceInitDict = {
      headers: {
        "auth-user": "bearer 123123123",
      },
    };
    //EventSource로 Server Sent Event를 호출하는 부분
    const eventSource = new EventSource(
      "http://localhost:8080/time/sse",
      eventSourceInitDict
    );

    // EventSource 로 data 를 받아서 처리하는 event listener 설정
    eventSource.addEventListener("sseData", async function (event) {
      const data = JSON.parse(event.data);
      setSseHeader(data["auth-user"]);
      setSseDate(data["date"]);
    });

    // Server Sent Event 가 종료되는 경우 연결된 EventSource 를 close 하는 부분
    eventSource.addEventListener("close", () => eventSource.close());
    return () => eventSource.close();
  }, []);
  return (
    <>
      <center>
        <Typography variant="h5" color="white">
          header : {sseHeader}
        </Typography>
        <Typography variant="h5" color="white">
          date : {sseDate}
        </Typography>
      </center>
    </>
  );
};

export default Sse;
