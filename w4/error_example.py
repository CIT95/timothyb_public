# Example of NameError, which occurs when a local or global name is not found

def printGuy():
  try:
    print(guy)
  except NameError:
    print('There is no guy to print!')

print('Caling printGuy()...')
printGuy()