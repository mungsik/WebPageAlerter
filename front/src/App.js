import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CssBaseline from "@mui/material/CssBaseline";
import Header from "./components/Header";
import Main from "./components/Main";
import RealTimeInfo from "./pages/RealTimeInfo";
import { createTheme, ThemeProvider } from "@mui/material";
import "./App.css";

const theme = createTheme({
  typography: {
    fontFamily: "'Source Sans Pro', sans-serif",
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Header />
        {/* <Footer /> */}
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="real-time-info" element={<RealTimeInfo />} />
          <Route path="*" element={<Main />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
