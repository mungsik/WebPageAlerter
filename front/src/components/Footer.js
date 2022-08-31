import { Box } from "@mui/material";

const Footer = () => {
  const footerStyle = {
    position: "fixed",
    bottom: 0,
    bgcolor: "gray",
    width: "100%",
    py: 1,
    zIndex: 1,
    borderTop: "2px solid #f1f3f5",
  };

  return <Box sx={footerStyle}>footer</Box>;
};

export default Footer;
