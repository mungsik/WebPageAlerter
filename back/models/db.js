import mysql from "mysql";
import dotenv from "dotenv";

//! config 안에 path 경로 설정해줘야 작동함.
dotenv.config({ path: "../.env" });

const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

export default connection;
