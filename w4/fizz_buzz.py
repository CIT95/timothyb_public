def fizz_buzz(num):
  output = ''
  try:
    num = int(num)
    if num % 3 == 0:
      output = output + 'Fizz'
    if num % 5 == 0:
      output = output + 'Buzz'
    if num % 3 != 0 and num % 5 != 0:
      print(str(num))
  except ValueError:
    print('That is not a number!')
  else:
    print(output)
  finally:
    print('Fizz buzz complete!')

print('Fizz buzz! Please input a number.')
fizz_buzz(input())