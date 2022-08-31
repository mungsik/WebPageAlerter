import { Box } from "@mui/material";
import wallStreet from "./imgs/wallStreet.jpg";
import MainPage from "./../pages/MainPage";

const Main = () => {
  const mainStyle = {
    bgcolor: "skyblue",
    height: "100vh",
    backgroundImage: `url(${wallStreet})`,
    backgroundSize: "cover",
    backgroundRepeat: "no-repeat",
  };

  return (
    <Box sx={mainStyle}>
      <MainPage />
    </Box>
  );
};

export default Main;
