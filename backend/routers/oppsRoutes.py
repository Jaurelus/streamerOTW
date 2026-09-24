from fastapi import APIRouter
from services import opps

router = APIRouter()
@router.get("/getLeagueTeams")
def getLeagueTeams():
    return opps.getLeagueTeams()