import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CssBaseline from "@mui/material/CssBaseline";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Main from "./components/Main";
import RealTimeInfo from "./pages/RealTimeInfo";

function App() {
  return (
    <>
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
    </>
  );
}

export default App;
