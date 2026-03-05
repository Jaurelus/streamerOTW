from espn_api.basketball import League
url = "https://fantasy.espn.com/basketball/team?leagueId=283299059&teamId=1&seasonId=2026"
year = url[len(url)-4:len(url)]
leagueID = url[url.find("leagueId")+len("leagueId")+1:url.find("teamId")-1]
espnS2= "AEC3Qxs88ujQc3Wrv8WftMO2B8XHlwpsHfMfknHqAuTbEU8H0W3mWMzlJnSbQZVQeEdgIaYU3bcl76G05caWw3%2FkUS%2Fwgzb2A23rgyMlb0%2BOmbMB7zd%2FMVadr6ed%2F7ubAXnJ0U4la%2FnbQiQH5r0C8k2Op6D%2FVaFHXSmTamYNq6byQg27t6PTP7q9EB7Y9AmNAy6U1GEio4D3hiZmEY7W5P0KQl5Dx8%2BPgiDV7bsVpJVfAJidhZLZ1rI2EFhp9ixlXScABhKW2zvZQMtasUfRUD3jHixV00iznAh83Q6bs2saGw%3D%3D"
swid= "{00975141-F7A5-4D73-A7F3-0EC0BF42B603}"
league = League(league_id=leagueID, year=int(year), espn_s2=espnS2, swid=swid)
print(league.year)

print(league.free_agents(size=5))
print (2+3)
#league = League(id=1)

#Gather all data needed

#Filter only players who average 10+ fantasy ppg on the szn