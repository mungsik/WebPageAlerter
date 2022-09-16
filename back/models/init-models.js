import _sequelize from "sequelize";
const DataTypes = _sequelize.DataTypes;
import _today_notice from  "./today_notice.js";

export default function initModels(sequelize) {
  const today_notice = _today_notice.init(sequelize, DataTypes);


  return {
    today_notice,
  };
}
