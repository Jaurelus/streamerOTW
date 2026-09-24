import react from "react";
import { Route, Routes } from "react-router";
import App from "../src/App";
import FA from "./fa";
import League from "./league";

const AppRoutes: React.FC = () => (
  <Routes>
    <Route path="/" element={<App />} />
    <Route path="/freeagents" element={<FA />} />
    <Route path="/league" element={<League />} />
  </Routes>
);

export default AppRoutes;
