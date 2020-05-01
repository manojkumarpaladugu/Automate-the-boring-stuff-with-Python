# with escaping characters
print('1. with Escaping characters')
mystring = 'That is Bob\'s vehicle'
print(mystring)
print('')

# without escaping characters
print('2. without Escaping characters')
mystring = "That is Bob\'s vehicle"
print(mystring)
print('')

# raw strings
print('3. raw strings')
mystring = r'That is Mr.Rao\'s house'
print(mystring)
print('')

# multiple line strings
print('4. multiple line strings')
mystring = """My name is Manoj Kumar,
I am a Software Artist,
from India."""
print(mystring)
print('')

# string slicing
print('string slicing')
mystring = "Manoj Kumar Paladugu"
firstname = mystring[:5]
print('First Name:', firstname)
middlename = mystring[6:11]
print('Middle Name:', middlename)
lastname = mystring[12:]
print('Last Name', lastname)
print('')

# check if part of substring is in a string
print('check if part of substring is in a string')
mystring = 'Hello, Learning python is really interesting'
substring = 'python'
status = substring in mystring
print(status)
print('')
