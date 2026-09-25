from league import league
print(league.teams)

def counter(search, obj):
    count=0 
    for item in obj:
        print(item.standing)
        if item["standing"] == search:
             count+=1
    #for item in obj:
     #   if item.standing==search:
      #      count+=1
    return count
def getLeagueTeams():
    teams = []
    for team in (league.teams):
        teams.append({"id": team.team_id, "name":team.team_name, "abbrev": team.team_abbrev, "logo": team.logo_url,
                      "wins": team.wins, "losses": team.losses, "ties": team.ties, "standing":team.standing, "division": team.division_id})
        
            
        #i
    return sorted(teams, key=lambda t: t["standing"])