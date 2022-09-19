import express from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
import morgan from "morgan";
import helmet from "helmet";
import "express-async-errors";
import SSEStream from "ssestream";
import { sequelize } from "./models/index.js";
import noticesRoutes from "./routes/today_notice.js";

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

app.use("/notices", noticesRoutes);

app.listen(PORT, () => {
  console.log(`Success! Your application is running on the port ${PORT}`);
});
