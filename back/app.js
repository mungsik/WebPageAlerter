import express from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
import morgan from "morgan";
import helmet from "helmet";
import "express-async-errors";
import SSEStream from "ssestream";
import noticesRouter from "./routes/notices.js";
import { sequelize } from "./models/index.js";

const PORT = 8080;

const app = express();

const corsOption = {
  origin: ["http://localhost:3000"],
  optionsSuccessStatus: 200,
};

sequelize
  .sync({ force: false }) // true면 서버 실행마다 테이블 재설정
  .then(() => {
    console.log("데이터베이스 연결 성공");
  })
  .catch((err) => {
    console.log(err);
  });

//? 사용중인 미들웨어들

app.use(cors(corsOption));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cookieParser());
app.use(morgan("tiny"));
app.use(helmet());

// app.get("/notices", noticesRouter);

app.get("/time/sse", (req, res) => {
  const headers = req.headers;
  // sseStream 생성
  const sseStream = new SSEStream(req);
  // stream pipe 설정
  sseStream.pipe(res);
  // 1초 간격으로 시간을 보내주는 setInterval 구성
  const pusher = setInterval(async () => {
    // header에 세팅된 auth-user 정보 가져오기
    const authUser = headers["auth-user"];
    // 현재 시간, auth-user 정보를 client 로 보내주는 부분
    sseStream.write({
      event: "sseData",
      data: { "auth-user": authUser, date: new Date() },
    });
  }, 1000);

  // close 시점에 setInterval 삭제, sseStream pipe 설정 해제
  res.on("close", () => {
    console.log("server send event connection closed!");
    clearInterval(pusher);
    sseStream.unpipe(res);
  });
});

app.listen(PORT, () => {
  console.log(`Success! Your application is running on the port ${PORT}`);
});
