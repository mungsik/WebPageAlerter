import { Grid, Box, Typography } from "@mui/material";

const MainPage = () => {
  const mainBox = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    width: "100vw",
    /*
    0px to 599px : "32px 20px"
    600px to 1199px : "64px 40px"
    1200 px and up : "115px 100px"
    */
    padding: { xs: "32px 20px", sm: "64px 40px", lg: "115px 100px" },
  };

  const mainText = { color: "white", fontSize: "2em", fontFamily: "Jalnan" };

  const noticeBox = {
    backgroundColor: "#1e222d80",
    border: "none",
    borderRadius: "56px",
    cursor: "pointer",
    height: "48px",
    minWidth: "164px",
    padding: "6px 16px 6px 12px",
    color: "white",
  };

  return (
    //TODO : lazy loding 적용하기
    <>
      <Box sx={mainBox}>
        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Typography component="h1" sx={mainText}>
              Now Is
            </Typography>
            <Typography component="h1" sx={mainText}>
              The Time
            </Typography>
          </Grid>
          <Grid item sm={6} xs={12}>
            <Box sx={noticeBox}>비트코인 올라가자</Box>
            <Box sx={noticeBox}>나스닥도 올라가자</Box>
          </Grid>
        </Grid>
      </Box>
    </>
  );
};

export default MainPage;
