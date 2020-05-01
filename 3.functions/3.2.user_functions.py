# Prints greeting and returns None value 
def greeting(name):
    print('Good morning ' + name)

# returns the length of the string
def strlen(string):
    return len(string)


print('Enter your name: ', end = '')
name = input()

# print a greeting for the user
returnValue = greeting(name)
print('returnValue of greeting() is ', returnValue)

# print length of the string
print('')
print('print length of the string')
length = strlen(name)
print(name + ' has ' + str(length) + ' letters in his name')

# print() with newline
print('')
print('print() with newline')
print('Hello')
print('World')

# print() without new line
print('')
print('print() without newline')
print('Hello', end = ' ')
print('World', end = ' ')

# print() multiple arguements with seperator
print('')
print('print() multiple arguements with seperator as space')
print('America', 'Brazil', 'China')

print('')
print('print() multiple arguements with seperator as hyphen')
print('America', 'Brazil', 'China', sep='-')
