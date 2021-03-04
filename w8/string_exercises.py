# w3 #16: Python function to insert a string in the middle of a string.
# My initial function had some errors, but simplifying it based on the example
# made it work properly.
def insert_string_middle(main_string, insert_string):
    return main_string[:2] + insert_string + main_string[2:]


# w3 #17: Python function to get a string made of 4 copies of the last two
# characters in a specified string of at least 2 characters.
# I wondered if the * 4 would work, and it did! Pleasant surprise!
def insert_end(input):
    if len(input) > 2:
        return input
    else:
        return input[-2:] * 4


# w3 #18: Python function to return a string of the first three characters.
# If string is >3, return the original string.
# I was able to solve it with no issues!
def first_three(input):
    if len(input) < 3:
        return input
    else:
        return input[0:3]


# w3 #19: Python program to get the last part of a string before a specified
# character.
# I looked up a way to find a specific char in a string, and fittingly
# found the .find function.
test_string = 'This is a large test string with a random X in it to use!'
print(test_string[:test_string.find('X')])


# w3 #20: Python function that reverses a string if its length is a multiple
# of 4.
# I had to look back at old code and double check the % equation.
def reverse_four(input):
    if len(input) % 4 == 0:
        return input[::-1]
    else:
        return input


# Pynative #12: Find the last position of a substring "Emma" in a given string.
# I kinda stumbled into this answer...I was going to use find() like an above
# problem, and my IDE showed the rfind() method, which ended up being perfect.
str1 = '''Emma is a close friend of mine. I met her with another friend, Jim.
Jim and Emma knew each other from Emma's school.'''
emma_index = str1.rfind('Emma')
print('Last occurence of Emma starts at: ' + str(emma_index))

# Pynative #14: Remove empty strings from a list of strings
# A simple for loop gets the job done. I tried the filter method on the site
# afterwards, but None didn't work, and it required an iterator, which I
# haven't messed around with in Python. I didn't want to go too far ahead.
name_list = ['Greg', 'Fred', 'Ted', '', 'Bill', '', 'Steve']
print('Original list of string')
print(name_list)
for name in name_list:
    if name is '':
        name_list.remove(name)
print('After removing empty strings')
print(name_list)

# Pynative #15: Remove special symbols/punctuation from a given string.
# Initially I forget to re-assign the string. I need to remember strings are
# not lists or dictionaries, I'm not editing the reference!
str2 = '/*Denz is a #talented ^$swordsman)().'
for char in str2:
    if char.isalpha() is False and char is not ' ':
        str2 = str2.replace(char, '')
print(str2)

# Pynative #17: Find words with both alphabets and numbers.
# The is functions made this work pretty smooth. I figured if I looked for
# words that were alphanumeric, but NOT just alpha, it would return what
# I wanted, and I was correct.
str3 = 'This1 is a String5 with 7Numbers3 atta8ched to random w0rds'
str3_split = str3.split()
str3_alphanum_sorted = []
for word in str3_split:
    if word.isalnum() is True and word.isalpha() is False:
        str3_alphanum_sorted.append(word)
print(str3_alphanum_sorted)

# Pynative #18: Replace each punctuation with # in the following string.
# The same logic to find punctuation worked. However, the website used an
# import of the punctuation library from the string class itself! I plan
# to look further into this in my own time.
str4 = '/*Jon is @developer & musician!!'
for char in str4:
    if char.isalpha() is False and char is not ' ':
        str4 = str4.replace(char, '#')
print(str4)
