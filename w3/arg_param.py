def numberDoubler(num):
  return (int(num)*2)

def numberPlusTwo(num, addNum='2'):
  return (num + int(addNum))

print('Input a number to be doubled.')
numInput = input()
numInputDoubled = numberDoubler(numInput)

print('The number doubled is ' + str(numInputDoubled))
print('This number will now be added to another number. Input a number to add, or input nothing for it to be added by two.')
powerInput  = input()
finalNum = 0
if powerInput != '':
  finalNum = numberPlusTwo(numInputDoubled, powerInput)
else:
  finalNum = numberPlusTwo(numInputDoubled)
print('The final number is ' + str(finalNum))