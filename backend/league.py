from dotenv import load_dotenv
import os
from espn_api.basketball import League

#Unpack the information from the .env file and create an instance of the league
#This way we create the league once and work form that object
load_dotenv()
year = os.getenv("YEAR")
lid = os.getenv("LEAGUEID")
s2 = os.getenv("ESPNS2")
swid = os.getenv("SWID")

league = League(year=year, league_id=lid, espn_s2=s2, swid=swid)




