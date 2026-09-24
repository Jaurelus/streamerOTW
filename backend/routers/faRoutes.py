from fastapi import APIRouter
from services import freeAgents

router = APIRouter()

@router.get("/getAll")
def getAllFA():
    return freeAgents.getAll()
@router.get("/getAvailable")
def getAvailableFA():
    return 