import react from "react";
import { Route, Routes } from "react-router";
import App from "../src/App";
import FA from "./fa";

const AppRoutes: React.FC = () => (
  <Routes>
    <Route path="/" element={<App />} />
    <Route path="/freeagents" element={<FA />} />
  </Routes>
);

export default AppRoutes;
