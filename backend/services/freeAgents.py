import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from league import league



from datetime import datetime




print("\n\n-------------New run!!----------------\n\n")



class freeAgents:
    def getAll():
        return league.free_agents()
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
            print(injuryDF)
            return injuryDF
                
            
            

            
        else:
            print(f"Error: {response.status_code}")


    def getInjuredFAReturn():
        fAtable = getFA()
        tb= getExpectedReturnDates()
        print(type(fAtable))
        print(fAtable.index)     
        print(tb.index)
        iFAIndex = []
        iFAData = []
        for name in tb.index:
            if name in  fAtable.index:
                print(name)
                iFAIndex.append(name)
                tbRD=tb.loc[name, "Return Date"]
                tbN=tb.loc[name, "Notes"]
                
                iFAData.append([tbRD, tbN]) 
        df = pd.DataFrame(iFAData, index=iFAIndex, columns=["Return Date", "Notes"])
        return df.to_dict(orient="index")
    t= getInjuredFAReturn()
    print(t)
    """
    if minutes!=None:
        if
    """
    def getPotentiallHealthyStreamers():
        today = datetime.now().date()

        injuryReturnTable = getExpectedReturnDates()
        injuredFA = getInjuredFAReturn()


        #Find this Sunday
        daysTillSunday = 6-today.weekday()
        thisSunday = datetime(today.year, today.month, today.day+daysTillSunday)
        #Take  the injuredFA table and if the return date is not by that Sunday remove
        injuredFA = pd.DataFrame(injuredFA)
        injuredFA=injuredFA.T
        #print(injuredFA)
        injuredFA["Return Date"]=pd.to_datetime(injuredFA["Return Date"], format='%b %d')
        injuredFA["Return Date"]=injuredFA["Return Date"].apply(lambda x:x.replace(year=2026))
        injuredFA = injuredFA[injuredFA["Return Date"]<=thisSunday]
        

        return injuredFA
        

    useDict=getPotentiallHealthyStreamers()
    print(useDict)

    def appendHealthyWPotential():
        x=0


    this = getFA(flag=1, reserveNames=useDict)
        
    #league.get_team_data()
    #league = League(id=1)

    #Gather all data needed

    #Filter only players who average 10+ fantasy ppg on the szn