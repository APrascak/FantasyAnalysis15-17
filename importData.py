import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Read in spreadsheets
df = pd.read_excel('dlstats_2015_2017.xlsx', sheet_name='Sheet1')
rk = pd.read_excel('espn_rankings.xlsx', sheet_name="Sheet1")


# Read in player statistics
names 		= df['Name']		# Player stats
pos 		= df['Pos']
team 		= df['Team']
years		= df['Year']
numGames	= df['Games Plyd']
rush 		= df['Rush']		# Rushing stats
rushYD	= df['Rush Yards']
rushTD		= df['Rush TD']
target		= df['Target']		# Receiving Stats
catch		= df['Catch']
catchYD		= df['Catch yards']
catchTD		= df['Catch TD']
passAtt		= df['Pass']		# Passing stats
passComp	= df['Complete']
passYD		= df['Pass Yards']
passTD		= df['Pass TD']
passInt		= df['Int']			# Turnovers
fum			= df['Fum']



namesRk 	= rk['Name']
yearRk		= rk['Year']
rank 		= rk['Rank']

# Logs information for all RB with > 1000 rushing yards in a seasion
for i in range(names.size):
	if pos[i] == 'RB':
		if rushYards[i] >= 1000:

			# Print information for each running back with more than 1,000 yards
			print('Player: ' + names[i])
			print('Team: ' + team[i])
			print('Year: ' + str(years[i]))
			print('Rushing Attempts: ' + str(rush[i]))
			print('Rushing Yards: ' + str(rushYards[i]))
			print('Yards/Rush: ' + str((rushYards[i] / rush[i])))
			print('Yards/Game: ' + str(rushYards[i] / numGames[i]))
			print('---------------------------------')

# Prints information 2016 rankings
score = 0
for i in range(namesRk.size):
	score = 0
	for j in range(names.size):
		if (names[j] == namesRk[i] and years[j] == yearRk[i]):
			print('FOUND')
			score = 18
	print(str(yearRk[i]) + ' Rank #' + str(int(rank[i])) + ' ' + namesRk[i] + ' ' + str(score))

