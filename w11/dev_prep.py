import re
import os

playerRegex = re.compile(r'''
(PlayerName:)(\w+)
-
(Wins:)(\d+)
-
(Losses:)(\d+)
''', re.VERBOSE)

currentPlayer = ['', 0, 0]


def saveData(name, wins, losses):
    saveFile = open('.\\data\\' + name + '.txt', 'w')
    saveFile.write('PlayerName:%s-Wins:%s-Losses:%s'
                   % (name, str(wins), str(losses)))
    saveFile.close()


def loadData(name):
    fileExists = False
    for file in os.listdir('.\\data'):
        if file == name + '.txt':
            fileExists = True

    if fileExists:
        saveFile = open('.\\data\\' + file)
        playerData = saveFile.read()
        processedData = playerRegex.search(playerData)
        saveFile.close()
        return [processedData.group(2),
                processedData.group(4),
                processedData.group(6)]
    else:
        return ['', 0, 0]


print(currentPlayer)
saveData('Tim', 5, 0)
currentPlayer = loadData('Tim')
print(currentPlayer)
