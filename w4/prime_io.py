numStart = 0
numEnd = 0
while (numStart >= numEnd):
  try:
    print('Please input a number.')
    numStart = int(input())
    print('Please input a second number.')
    numEnd = int(input())
    if (numStart >= numEnd):
      print('Starting value is not smaller than ending value. Please input new values.')
    else:
      print('Values accepted. Prime numbers between values is:')
  except ValueError:
    print('Input is not a number! Please try again.')
for num in range(numStart, numEnd+1):
  # code to determine if number is prime found at https://www.javatpoint.com/python-check-prime-number
  if num > 1:
    for i in range(2,num):  
      if (num % i) == 0:
        break
    else:
      print(num)