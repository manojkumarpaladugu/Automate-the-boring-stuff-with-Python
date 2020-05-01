import re

# search word starts with 'hello'
# Caret ^ symbol tells the python to match for the word in the very beginning
message = 'Hello there, I am using Whatsapp'
pattern = re.compile(r'^Hello')
matchObject = pattern.search(message)
print(matchObject.group())

# search word ends with 'world!'
# dollar $ symbol tells the python to match for the word in the end
message = 'Hello world!'
pattern = re.compile(r'world!$')
matchObject = pattern.search(message)
print(matchObject.group())

# match all the digits starts and ends
message = '123534004933'
# ^ match should start in the very beginning of the string
# + match one or more digits
# $ match should end
pattern = re.compile(r'^\d+$')
matchObject = pattern.search(message)
print(matchObject.group())

# match all the characters before word 'at'
message = 'The cat in the hat sat on the flat mat'
# . says python to match any character before word 'at'
pattern = re.compile(r'.at')
matchList = pattern.findall(message)
print(matchList)


# match first name and last name
message = 'First Name: Manoj Kumar, Last Name: Paladugu'
pattern = re.compile(r'First Name: (.*), Last Name: (.*)')
matchList = pattern.findall(message)
print(matchList)
