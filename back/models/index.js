import Sequelize from "sequelize";
import config from "../config/config.js";
import initModels from "./init-models.js";
import dotenv from "dotenv";

dotenv.config({ path: "../.env" });

const sequelize = new Sequelize(
  config.database,
  config.username,
  config.password,
  { host: config.host, dialect: "mysql" }
);

const db = initModels(sequelize);

export { db, sequelize };
