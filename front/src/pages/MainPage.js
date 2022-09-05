import { Grid, Box, Container } from "@mui/material";

const MainPage = () => {
  const mainBox = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  };

  return (
    <Container sx={mainBox}>
      <Grid container spacing={1}>
        <Grid item xs={12}>
          <Box sx={{ color: "white" }}>지금이니!</Box>
        </Grid>
        <Grid item xs={12}>
          <Box sx={{ color: "white" }}>여기서 마켓서치</Box>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Box sx={{ color: "white" }}>비트코인 올라가자</Box>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Box sx={{ color: "black" }}>나스닥도 올라가자</Box>
        </Grid>
      </Grid>
    </Container>
  );
};

export default MainPage;
