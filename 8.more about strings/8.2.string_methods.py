# strigs are immutable, so string methods do not modify its value, instead it returns new string

# convert string from upper case to lower case
print('convert string from upper case to lower case')
mystring = 'AWESOME'
modifiedstring = mystring.lower()
print(mystring, '->', modifiedstring)
print('')

# convert string from lower case to upper case
print('convert string from lower case to upper case')
mystring = 'wonderful'
modifiedstring = mystring.upper()
print(mystring, '->', modifiedstring)
print('')

# check if string is lowercase
print('check if string is lowercase')
mystring = 'manoj'
if mystring.islower():
    print(mystring ,'is lowercase')
print('')

# check if string is uppercase
print('check if string is uppercase')
mystring = 'MANOJ'
if mystring.isupper():
    print(mystring ,'is uppercase')
print('')

# check if string is titlecase
print('check if string is titlecase')
mystring = 'Manoj'
if mystring.istitle():
    print(mystring ,'is titlecase')
print('')

# check if string is decimal
print('check if string is decimal')
mystring = '1234'
if mystring.isdecimal():
    print(mystring ,'is decimal')
print('')

# check if string is alphanumeric
print('check if string is alphanumeric')
mystring = 'abcd1234'
if mystring.isalnum():
    print(mystring ,'is alphanumeric')
print('')

