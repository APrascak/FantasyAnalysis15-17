import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('dlstats_2015_2017.xlsx', sheet_name='Sheet1')

names 		= df['Name']
pos 		= df['Pos']
team 		= df['Team']
years		= df['Year']
numGames	= df['Games Plyd']
rush 		= df['Rush']
rushYards	= df['Rush Yards']

print(names[1271])
print(pos[1271])
print(team[1271])
print(years[1271])
print(numGames[1271])
print(names.size)

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