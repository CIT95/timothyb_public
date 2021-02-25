# List sorted in order of most wins to least wins
# this code used for reference: https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
def sortPlayers(players):
  return sorted(players, key = lambda x: x['wins'], reverse=True)

# Key added to DD, also checks whether given key already exists
def addPocket(player, pocket):
  if 'pocket' in player:
    player['pocket'] = player['pocket'] + ', ' + pocket
  else:
    player['pocket'] = pocket

# Iterating through DD using for loop
def printPlayer(player):
  for k, v in player.items():
    print(k + ': ' + str(v))

# Filters list of DD based on values
def sortWinners(players):
  winners = []
  for player in players:
    if player['wins'] > player['losses']:
      winners.append(player)
  return winners

# Iterate over list of dictionaries and outputs summary data
def printRecords(players):
  charList = []
  bestPlayer = ''
  mostWins = 0
  for player in players:
    if player['main'] not in charList:
      charList.append(player['main'])
    if 'pocket' in player:
      charList.append(player['pocket'])
    if player['wins'] > mostWins:
      mostWins = player['wins']
      bestPlayer = player['tag']
  print('The best player in the region is ' + bestPlayer + ', with their record high ' + str(mostWins) + ' wins.')
  print('The characters used in this region are:')
  for char in charList:
    print(char)

# Creation of dictionaries/list of dictionaries
playerOne = {'tag':'Peter the Great', 'wins': 3, 'losses': 0, 'main':'R.O.B.'}
playerTwo = {'tag':'Lloydqrow', 'wins': 1, 'losses': 2, 'main':'Richter'}
playerThree = {'tag':'Draxxus', 'wins': 2, 'losses': 1, 'main':'Byleth'}
playerFour = {'tag':'Butcho', 'wins': 0, 'losses': 3, 'main':'Inkling'}
playerList = [playerOne, playerTwo, playerThree, playerFour]

print(sortPlayers(playerList))
addPocket(playerTwo, 'Joker')
printPlayer(playerTwo)
print(sortWinners(playerList))
printRecords(playerList)