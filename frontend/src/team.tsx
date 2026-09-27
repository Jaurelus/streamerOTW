import Header from "#components/header";
import { Card, CardContent, CardHeader, CardTitle } from "#components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "#components/ui/table";
import { useEffect, useState } from "react";
import { useParams } from "react-router";

function Team() {
  const { id } = useParams();
  const [team, setTeam] = useState();

  const getTeam = async () => {
    const response = await fetch(`http://127.0.0.1:8000/league/getTeam/${id}`, {
      headers: {},
      method: "GET",
    });
    const data = await response.json();
    if (response.ok) {
      console.log(data[0]);
      setTeam(data[0]);
    } else {
      console.log("Error getting team info");
    }
  };
  useEffect(() => {
    getTeam();
  }, []);
  return (
    <div className="w-screen h-screen">
      <Header />
      <div className="flex flex-col items-center pt-4">
        {team && (
          <div className="flex flex-col items-center">
            <h1>{team.name}</h1>
            <img src={team.logo} className="max-w-16" />
            <div>
              <div className="rounded-full border-2 min-w-8 min-h-8 flex items-center justify-center">
                <h2>{team.standing}</h2>
              </div>
              <p>
                {team.wins}-{team.losses}-{team.ties}
              </p>
            </div>
          </div>
        )}

        <Card className="text-white w-3/4">
          <CardHeader>
            <CardTitle>{}</CardTitle>
          </CardHeader>
          {team && (
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableCell>Name</TableCell>
                    <TableCell>Proj. FP</TableCell>
                    <TableCell>Avg FP</TableCell>
                    <TableCell></TableCell>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {team.roster.map((player) => (
                    <TableRow>
                      <TableCell>{player.name}</TableCell>
                      <TableCell>{player.projected}</TableCell>
                      <TableCell>{player.avg}</TableCell>
                      <TableCell>
                        <button className="">+</button>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </CardContent>
          )}
        </Card>
      </div>
    </div>
  );
}
export default Team;
