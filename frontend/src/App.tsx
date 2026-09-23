import { useState } from "react";
import { Card, CardHeader } from "./components/ui/card";
import { Link } from "react-router";
import Header from "./components/header";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="w-screen h-screen bg-darkbg">
      {/* Header div */}
      <Header />
      {/* Roster div */}
      <div className="flex justify-center">
        <Card className="bg-card w-[50%] py-5 text-white">
          <CardHeader className="flex flex-row justify-between">
            <p>Name</p>
            <p>NBA Team</p>
            <p>Avg PPG</p>
            <p>Avg RBG</p>
            <p>Avg APG</p>
            <p>Avg SPG</p>
            <p>Avg BPG</p>
            <p>Avg TOPG</p>
            <p>Avg MPG</p>
            <p>Avg FPts</p>
          </CardHeader>
        </Card>
      </div>
    </div>
  );
}

export default App;
