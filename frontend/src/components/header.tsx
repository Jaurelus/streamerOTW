import { Link } from "react-router";
function Header() {
  return (
    <div className="w-full text-center">
      <h1 className="text-primary">Fantasy Basketball Wizard</h1>
      <div className="flex-row flex text-center w-full justify-between px-[35%]">
        <Link to="/freeagents">
          <p className="text-white">Free Agents</p>
        </Link>
        <Link to="/">
          <p className="text-white">Roster</p>
        </Link>
        <Link to="/league">
          <p className="text-white">League</p>
        </Link>
      </div>
    </div>
  );
}
export default Header;
