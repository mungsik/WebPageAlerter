import express from "express";
import connection from "../models/db.js";
// import * as noticesController from "../controller/notices.js";

const router = express.Router();

// router.get("/notices", noticesController.getNotices);
var result;
router.route("/notices").get(async (req, res, next) => {
  connection.connect();
  connection.query("select * from today_notice limit 10", (err, response) => {
    if (err) {
      console.log("error", err);
      return;
    }

    console.log("notices:", response);
    result = response;
    connection.end();
  });

  res.json(result);
});

export default router;
// module.exports = router;
