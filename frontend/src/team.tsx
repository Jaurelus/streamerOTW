import { useParams } from "react-router";

function Team() {
  const { id } = useParams();
  const getTeam = async () => {};

  return (
    <div>
      <h1>Team</h1>
    </div>
  );
}
export default Team;
