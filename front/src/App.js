import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CssBaseline from "@mui/material/CssBaseline";
import Header from "./components/Header";
import Main from "./components/Main";
import RealTimeInfo from "./pages/RealTimeInfo";
import { createTheme, ThemeProvider } from "@mui/material";
import "./App.css";
import MetaTag from "./pages/MetaTag";

const theme = createTheme({
  typography: {
    fontFamily: "'Source Sans Pro', sans-serif",
  },
  palette: {
    buttonColor: {
      main: "#FFFFFF",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      {/* 디폴트 메타태그는 설정완료 */}
      {/* //TODO 페이지별 메타태그 구분해줄 것 */}
      <MetaTag
        title="DART Alerter"
        description="DART 홈페이지에 올라오는 실시간 공시 알리미"
        keywords="dart"
      />
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
