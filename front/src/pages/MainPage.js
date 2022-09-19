import { Grid, Box, Typography } from "@mui/material";
import Sse from "../components/Sse";

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

  const mainText = { color: "white", fontSize: "5em", fontFamily: "Jalnan" };

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
              The Time.
            </Typography>
          </Grid>
          <Grid item sm={6} xs={12}>
            <Sse />
          </Grid>
        </Grid>
      </Box>
    </>
  );
};

export default MainPage;
