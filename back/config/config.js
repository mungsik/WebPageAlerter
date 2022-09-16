import dotenv from "dotenv";

dotenv.config({ path: "../.env" });

const config = {
  username: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  host: process.env.DB_HOST,
};

export default config;
