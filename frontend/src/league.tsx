import Header from "#components/header";
import { Card, CardContent, CardHeader, CardTitle } from "#components/ui/card";
import { useEffect, useState } from "react";
import { Link } from "react-router";

function League() {
  const [teams, setTeams] = useState([]);
  const getAllTeams = async () => {
    const response = await fetch(
      "http://127.0.0.1:8000/league/getLeagueTeams",
      {
        headers: {},
        method: "GET",
      },
    );
    const data = await response.json();
    if (response.ok) {
      setTeams(data);
    } else {
      console.log(response);
    }
  };
  useEffect(() => {
    getAllTeams();
  }, []);
  useEffect(() => {
    console.log(teams);
  }, [teams]);
  return (
    <div className="w-screen h-screen ">
      <Header />
      <div className="flex items-center flex-col">
        <h1>League</h1>
        <div className="w-full justify-center flex">
          {teams && (
            <Card className="w-[50%] text-white text-center">
              <CardHeader>
                <CardTitle>Rosters</CardTitle>
              </CardHeader>
              {teams && (
                <CardContent className="grid grid-cols-2 gap-3">
                  {teams.map((team) => (
                    <div key={team.id} className="flex-row">
                      <div className="flex flex-col">
                        <img src={team.logo} className="max-w-16"></img>
                        <p className="text-left px-8">{team.standing}</p>
                      </div>
                      <div className="flex flex-col">
                        <p>{team.standing}</p>
                        <Link to={`/team/${team.id}`}>
                          <p className="text-white">{team.name}</p>
                        </Link>

                        <p>
                          {team.wins}-{team.losses}-{team.ties}
                        </p>
                      </div>
                    </div>
                  ))}
                </CardContent>
              )}
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}
export default League;
