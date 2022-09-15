import sql from "./db.js";

const Notices = (notices) => {
  this.time = notices.time;
  this.company = notices.company;
  this.report_head = notices.report_head;
  this.date = notices.date;
  this.url = notices.url;
  this.getAll = (err, data) => {
    sql.query("SELECT * FROM DB.today_notice", (err, res) => {
      if (err) {
        console.log("error", err);
        return err, null;
        // return;
      }

      console.log("notices:", res);
      return null, res;
      // return;
    });
  };
};

// Notices.getAll = () => {
//   sql.query("SELECT * FROM DB.today_notice", (err, res) => {
//     if (err) {
//       console.log("error", err);
//       return err, null;
//     }

//     console.log("notices:", res);
//     return null, res;
//   });
// };

export default Notices;
