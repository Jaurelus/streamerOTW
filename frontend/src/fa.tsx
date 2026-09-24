import { useEffect, useState } from "react";
import Header from "./components/header";
import { Card, CardHeader } from "#components/ui/card";
import {
  Table,
  TableBody,
  TableHead,
  TableHeader,
  TableRow,
  TableCell,
} from "#components/ui/table";

function FA() {
  const [allFreeAgents, setAllFreeAgents] = useState([]);
  const getAllFA = async () => {
    const response = await fetch("http://127.0.0.1:8000/streamers/getAll", {
      headers: {},
      method: "GET",
    });
    const data = await response.json();
    if (response.ok) {
      setAllFreeAgents(data);
    } else {
    }
  };
  useEffect(() => {
    getAllFA();
  }, []);
  useEffect(() => {
    console.log(allFreeAgents);
  }, [allFreeAgents]);
  return (
    <div className="w-screen h-screen">
      <Header />
      <div className="flex flex-row justify-between px-10">
        <h1 className="">Free Agents</h1>
        <div className="flex items-end">
          <p>Filter Streamers</p>
        </div>
      </div>
      <div className="px-5">
        <Card className="text-white ">
          {allFreeAgents && (
            <Table className="text-center">
              <TableHeader className="">
                <TableRow className="">
                  <TableCell>Name</TableCell>
                  <TableCell>Pos</TableCell>
                  <TableCell>NBA Team</TableCell>
                  <TableHead>PPG</TableHead>
                  <TableHead>RPG</TableHead>
                  <TableHead>APG</TableHead>
                  <TableHead>SPG</TableHead>
                  <TableHead>BPG</TableHead>
                  <TableHead>TOPG</TableHead>
                  <TableHead>MPG</TableHead>
                  <TableHead>FPPG</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody className="">
                {allFreeAgents.map((fa) => (
                  <TableRow>
                    <TableCell>{fa.name}</TableCell>
                    <TableCell>{fa.eligibleSlots[1]}</TableCell>
                    <TableCell>{fa.proTeam}</TableCell>
                    <TableCell></TableCell>
                    <TableCell></TableCell>
                    <TableCell></TableCell>
                    <TableCell></TableCell>
                    <TableCell></TableCell>
                    <TableCell></TableCell>
                    <TableCell></TableCell> <TableCell></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          )}
        </Card>
      </div>
    </div>
  );
}
export default FA;
