from password_strength import PasswordStats

password = input('Please input a password to test: ')
print('Your password strength is: ' + str(PasswordStats(password).strength()))
print('Remember, a score above 0.66 is a strong password!')
