import express from "express";
import today_notice from "./../models/today_notice.js";
import SSEStream from "ssestream";

const router = express.Router();

router.get("/", async (req, res) => {
  const notices = await today_notice.findAll({
    order: [["id", "DESC"]],
    limit: 1,
  });

  const result = [];

  for (const notice of notices) {
    // if (notice.report_head.length >= 10) {
    //   return notice.report_head.substr(0, 10) + "...";
    // }
    result.push({
      id: notice.id,
      time: notice.time,
      date: notice.date,
      company: notice.company,
      url: notice.url,
      report_head: notice.report_head,
    });
  }
  console.log(result);

  const sseStream = new SSEStream(req);
  // stream pipe 설정
  sseStream.pipe(res);
  // 1초 간격으로 시간을 보내주는 setInterval 구성
  const pusher = setInterval(async () => {
    // 현재 시간, auth-user 정보를 client 로 보내주는 부분
    result.forEach((value) => {
      sseStream.write({
        event: "sseData",
        data: {
          id: value.id,
          time: value.time,
          date: value.date,
          company: value.company,
          url: value.url,
          report_head: value.report_head,
        },
      });
    });
  }, 5000);

  // close 시점에 setInterval 삭제, sseStream pipe 설정 해제
  res.on("close", () => {
    console.log("server send event connection closed!");
    clearInterval(pusher);
    sseStream.unpipe(res);
  });
});

export default router;
