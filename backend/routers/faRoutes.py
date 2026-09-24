from fastapi import APIRouter
from services import freeAgents

router = APIRouter()
service = freeAgents.freeAgents()

@router.get("/getAll")
def getAllFA():
    return service.getAll()
@router.get("/getAvailable")
def getAvailableFA():
    return 