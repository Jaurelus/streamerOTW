from league import league
from league import pastLeague
import pandas as pd
import numpy as np 

def getLeagueTeams():
    teams = []
    for team in (league.teams):
        teams.append({"id": team.team_id, "name":team.team_name, "abbrev": team.team_abbrev, "logo": team.logo_url,
                      "wins": team.wins, "losses": team.losses, "ties": team.ties, "standing":team.standing, "division": team.division_id})
        
            
        #i
    return sorted(teams, key=lambda t: t["standing"])

def getTeam(id):
    teamInfo = league.get_team_data(id)
    roster = []
    for player in teamInfo.roster:
        roster.append({"name": player.name, "injured": player.injuryStatus, "projected": player.projected_avg_points, "avg": player.avg_points, "id": player.playerId})
    filtered = [{"id": teamInfo.team_id, "name":teamInfo.team_name, "abbrev": teamInfo.team_abbrev, "logo": teamInfo.logo_url,
                      "wins": teamInfo.wins, "losses": teamInfo.losses, "ties": teamInfo.ties, "standing":teamInfo.standing, "division": teamInfo.division_id,
                      "PA":teamInfo.points_against, "PF": teamInfo.points_for, "roster":roster}]
    return filtered

def analyzePlayer(id):
    """
    This function scans players on other people's teams. It looks for players who avg less fpts than projected, players with insanely high TOs, players with 
    abornamlly low shooting splits %, players severly lacking in defensive stats that usually have, players playing less MPG than usual, and other context like 
    injury implications, or role changes, (extra to young players bc development)
    """
    
    #7 day analysis
    league.player_info(playerId=id)
    #pass data into llm to reason from the data
    
    #15 day analysis
    
    #30 day analysis
    return
 
#------Helper functions for analysis-----
def getBaseline(id: int):
    """
    In order to know if a player is playing well or not we need to have a baseline to compare to
    The "regular them" will use data from the past 2 szns 
    """
    
    #Get box scores from last szn
    league.year=2026
    player = league.player_info(playerId=id)
    sznStats1 = []
    for game in player.stats:
        if "total" in player.stats[game]:
            sznStats1.append(player.stats[game]["total"])
    #Get box scores from 2 szns ago
    player = pastLeague.player_info(playerId=id)
    sznStats2 = []
    for i,game in enumerate(player.stats):
        if "total" in player.stats[game]:
            if i<=len(player.stats)-3: #Removes summary data to only keep raw box score data
             sznStats2.append(player.stats[game]["total"])
            
    df = pd.DataFrame(sznStats1+sznStats2)
    
    df.to_excel("stats.xlsx", index=False)
    
    #Apply exponential weight to favor recent games
        #Half-life: 41 games (half szn)
    half= 41
    df["weight"]=0.5**(df.index-1/half) #1/2^(time elapsed/halflife)
    
        #Get player years pro if less than 6 development is highly more likely so weight should favor receny more

    #Get mean, std, median
    playerBaseline = {"name": player.name, "id": player.playerId, "pts": np.average(df["PTS"], weights=df["weight"  ]), 
                      "reb": np.average(df["REB"], weights=df["weight"  ]), "ast": np.average(df["AST"], weights=df["weight"  ]), 
                      "stl": np.average(df["STL"], weights=df["weight"  ]), "blk": np.average(df["BLK"], weights=df["weight"  ]), 
                      "fgm": np.average(df["FGM"], weights=df["weight"  ]), "fga": np.average(df["FGA"], weights=df["weight"  ]), 
                      "3pm": np.average(df["3PM"], weights=df["weight"  ]),"3pa": np.average(df["3PA"], weights=df["weight"  ]),
                      "ftm": np.average(df["FTM"], weights=df["weight"  ]), "fta": np.average(df["FTA"], weights=df["weight"  ]), 
                      "gs": np.average(df["GS"], weights=df["weight"  ]), "dd": np.average(df["DD"], weights=df["weight"  ]), 
                      "td": np.average(df["TD"], weights=df["weight"  ]), "mpts": np.median(df["PTS"], weights=df["weight"  ]),
                      "mast": np.median(df["PTS"], weights=df["weight"  ]), "mreb": np.median(df["PTS"], weights=df["weight"  ]),
                      "mfgm": np.median(df["FGM"], weights=df["weight"  ]), "mfga": np.median(df["FGA"], weights=df["weight"  ]), 
                        "m3pm": np.median(df["3PM"], weights=df["weight"  ]),"m3pa": np.median(df["3PA"], weights=df["weight"  ]),
                        "mftm": np.median(df["FTM"], weights=df["weight"  ]), "mfta": np.median(df["FTA"], weights=df["weight"  ]), 
                        "starter": np.median(df["GS"], weights=df["weight"  ]),}
    return playerBaseline

    getBaseline()