// import * as noticesRepository from "../models/notices.js";
import Notices from "../models/notices.js";
export async function getNotices(req, res) {
  Notices("kkhk").getAll((err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving customers.",
      });
    else res.send(data);
  });
}
