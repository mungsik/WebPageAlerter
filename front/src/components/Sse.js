// import EventSource from "eventsource";
import { NativeEventSource, EventSourcePolyfill } from "event-source-polyfill";
import { useEffect, useState } from "react";
import { Typography, Box, Button } from "@mui/material";

const Sse = () => {
  // Server Sent Event 로 가져온 data를 화면에 보여주기 위한 state 변수
  const [sseCompany, setSseCompany] = useState("");
  const [sseReport, setSseReport] = useState("");
  const [sseUrl, setSseUrl] = useState("");

  const noticeBox = {
    backgroundColor: "#1e222d80",
    border: "none",
    borderRadius: "30px",
    height: "8rem",
    width: "15rem",
    // minWidth: "5rem",
    padding: "6px 16px 6px 12px",
    color: "white",
    mt: "3rem",
  };

  useEffect(() => {
    //? SSE Polyfill
    const EventSource = NativeEventSource || EventSourcePolyfill;

    //   const getNotices = async () => {
    //     const res = await Api.get("notices");
    //     console.log(res.data);
    //     console.log(res.data[5].company);
    //   };

    // useEffect(() => {
    //   getNotices();
    // }, []);
    //EventSource로 Server Sent Event를 호출하는 부분
    const eventSource = new EventSource("http://localhost:8080/notices");

    // EventSource 로 data 를 받아서 처리하는 event listener 설정
    eventSource.addEventListener("sseData", async function (event) {
      const data = JSON.parse(event.data);
      setSseCompany(data.company);
      setSseReport(data.report_head);
      setSseUrl(data.url);
    });

    // Server Sent Event 가 종료되는 경우 연결된 EventSource 를 close 하는 부분
    eventSource.addEventListener("close", () => eventSource.close());
    return () => eventSource.close();
  }, []);

  return (
    <Box sx={noticeBox}>
      <Typography
        sx={{
          transition: "all 1s ease-in-out 1s",
          pt: 0.5,
          fontWeight: "bold",
          fontSize: 20,
        }}
      >
        {sseCompany}
      </Typography>
      <Typography
        sx={{ transition: "all 1s ease-in-out 1s", mt: 1, color: "red" }}
      >
        {sseReport}
      </Typography>
      <Button
        sx={{ transition: "all 1s ease-in-out 1s", mt: 1 }}
        target="_blank"
        rel="noreferrer noopener"
        href={sseUrl}
        color="buttonColor"
        style={{ backgroundColor: "transparent" }}
      >
        원본 링크
      </Button>
    </Box>
  );
};

export default Sse;
