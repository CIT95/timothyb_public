numStart = 0
numEnd = 0
while (numStart >= numEnd):
  print('Please input a number.')
  numStart = int(input())
  print('Please input a second number.')
  numEnd = int(input())
  if (numStart >= numEnd):
    print('Starting value is not smaller than ending value. Please input new values.')
  else:
    print('Values accepted. Range between values is:')
for num in range(numStart, numEnd+1):
  print(num)