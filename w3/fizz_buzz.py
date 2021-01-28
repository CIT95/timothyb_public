def fizz_buzz(num):
  output = ''
  if num % 3 == 0:
    output = output + 'Fizz'
  if num % 5 == 0:
    output = output + 'Buzz'
  if num % 3 != 0 and num % 5 != 0:
    return num
  else:
    return output

print('Fizz buzz! Please input a number.')
userInput = input()
print(fizz_buzz(int(userInput)))