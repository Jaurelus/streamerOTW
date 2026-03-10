from espn_api.basketball import League
from fastapi import APIRouter
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests



from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()
apiKey = os.getenv("INJURYAPIKEY")
today = datetime.now().date()
""" 
load_dotenv()
year    = os.getenv("LEAGUE_YEAR")
leagueID = os.getenv("LEAGUE_ID")
espnS2= os.getenv("ESPNS2")
swid = os.getenv("SWID")
"""
router= APIRouter()


print(str(datetime.now().date()))

#delete below

url = "https://fantasy.espn.com/basketball/team?leagueId=283299059&teamId=1&seasonId=2026"
year = url[len(url)-4:len(url)]
leagueID = url[url.find("leagueId")+len("leagueId")+1:url.find("teamId")-1]
espnS2= "AEC3Qxs88ujQc3Wrv8WftMO2B8XHlwpsHfMfknHqAuTbEU8H0W3mWMzlJnSbQZVQeEdgIaYU3bcl76G05caWw3%2FkUS%2Fwgzb2A23rgyMlb0%2BOmbMB7zd%2FMVadr6ed%2F7ubAXnJ0U4la%2FnbQiQH5r0C8k2Op6D%2FVaFHXSmTamYNq6byQg27t6PTP7q9EB7Y9AmNAy6U1GEio4D3hiZmEY7W5P0KQl5Dx8%2BPgiDV7bsVpJVfAJidhZLZ1rI2EFhp9ixlXScABhKW2zvZQMtasUfRUD3jHixV00iznAh83Q6bs2saGw%3D%3D"
swid= "{00975141-F7A5-4D73-A7F3-0EC0BF42B603}"

#delete above

league = League(league_id=leagueID, year=int(year), espn_s2=espnS2, swid=swid)


def getFA(flag=0, reserveNames=None):
    """
    A function to get all free agents in the current league with restrictions based on health or minutes played
    """
    currFA= league.free_agents()
    freeAgentData = []
    tmpIndex=[]
    for player in currFA:
        if player.injured==True and flag==0:
            
            
            continue
        if flag==1:
            if player.name not in reserveNames.keys():
                continue
        playerPositions = []
        for slot in player.eligibleSlots:
            if "/" in slot:
                break
            playerPositions.append(slot)
            #print(player.stats["2026_total"]["avg"]["MPG"])                          
            #print(player.stats["2026_last_7"])              
        freeAgentData.append([player.playerId,playerPositions,player.posRank,player.acquisitionType,player.proTeam,player.position,player.injuryStatus,player.injured,player.stats,player.schedule,player.lineupSlot,player.total_points,player.avg_points,player.projected_avg_points,player.projected_total_points]) 
        tmpIndex.append(player.name)
    headers= "PlayerId,eligibleSlots,posRank,acquisitionType,proTeam,position,injuryStatus,injured,stats,schedule,lineupSlot,total_points,avg_points,projected_avg_points,projected_total_points"
    df=pd.DataFrame(freeAgentData, columns=headers.split(","), index=tmpIndex)


    return df

freeAgentTable =getFA()

def get7DAverages():
    x=0

def get15DAverages():
    x=0

def getExpectedReturnDates():
    x=0
    bs4espn= "https://www.espn.com/nba/injuries"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(bs4espn, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        names = (soup.select('[class="AnchorLink"]'))
        adjustedNames= []
        for name in names:
            s1= str(name)[:-4]
            index= s1.find(">")
            adjustedName =(s1[index+1:])
            adjustedNames.append(adjustedName)
        
        cards= soup.find_all(class_="col-desc Table__TD")
        dates = soup.find_all("td", class_="col-date Table__TD")

        data= []
        for index,card in enumerate(cards):
            strCard = (str(card)[31:-5])
            strDate = str(dates[index])[31:-5]
            data.append([strDate,strCard])
        
            
        injuryDF = pd.DataFrame(data,index=adjustedNames, columns=["Return Date", "Notes"])
        
        return injuryDF
            
        
        

        
    else:
        print(f"Error: {response.status_code}")


def getInjuredFAReturn(iRTable, fAtable):
    fAtable
    print(iRTable, type(iRTable))
    iRTable.columns
    iFAIndex = []
    iFAData = []
    for name in fAtable.columns:
        if name in iRTable.columns:
            iFAIndex.append(name)
            iFAData.append([iRTable[name]["Return Date"], iRTable[name]["Notes"]]) 
    df = pd.DataFrame(iFAData, index=iFAIndex, columns=["Return Date", "Notes"])
    return df.to_dict(orient="index")
tmptmp= getExpectedReturnDates
theFAs= getFA()
getInjuredFAReturn(iRTable=tmptmp, fAtable=theFAs)
"""
if minutes!=None:
    if
"""
@router.get("/")
def getPotentiallHealthyStreamers():
    injuryReturnTable = getExpectedReturnDates()
    injuredFA = getInjuredFAReturn(injuryReturnTable,freeAgentTable)


    #Find this Sunday
    daysTillSunday = 6-today.weekday()
    thisSunday = datetime(today.year, today.month, today.day+daysTillSunday)
    #Take  the injuredFA table and if the return date is not by that Sunday remove
    injuredFA = pd.DataFrame(injuredFA)
    injuredFA=injuredFA.T
    #print(injuredFA)
    injuredFA["Return Date"]=pd.to_datetime(injuredFA["Return Date"], format='%b %d')
    #injuredFA["Return Date"]=injuredFA["Return Date"].apply(lambda x:x.replace(year=2026))
    #injuredFA = injuredFA[injuredFA["Return Date"]<=thisSunday]
    theDict= injuredFA.to_dict(orient="index")
    print(injuredFA)

    return injuredFA
    

useDict=getPotentiallHealthyStreamers()
print(useDict)


this = getFA(flag=1, reserveNames=useDict)
    
#league.get_team_data()
#league = League(id=1)

#Gather all data needed

#Filter only players who average 10+ fantasy ppg on the szn