//API Call to get free agents
async function getFreeAgents() {
  try {
    const response = await fetch("http://127.0.0.1:8000/streamers");
    const data = await response.json();
    console.log(data);
    document.getElementById("freeAgents").innerHTML = data;
  } catch (error) {
    console.log(error);
  }
}
