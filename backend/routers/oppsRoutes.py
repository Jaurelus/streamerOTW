from fastapi import APIRouter
from services import opps

router = APIRouter()
@router.get("/getLeagueTeams")
def getLeagueTeams():
    return opps.getLeagueTeams()

@router.get("/getTeam/{ownerId}")
def getTeam(ownerId: int):
    return opps.getTeam(id=ownerId)