import re

# Match for Batman or Batwoman in the message
message = 'Adventure of Batman'
pattern = re.compile(r'Bat(man|woman)')
matchObject = pattern.search(message)
print(matchObject.group())

# Match for Batman or Batwoman in the message using ?
# ?: look for 0 or 1 occurance. It is like the group can appear as optional.
message = 'Adventure of Batman'
pattern = re.compile(r'Bat(wo)?man') # ? telling that 'wo' is optional, can appear 0 or 1 time
matchObject = pattern.search(message)
print(matchObject.group())

message = 'Adventure of Batwoman'
pattern = re.compile(r'Bat(wo)?man') # ? telling that 'wo' is optional, can appear 0 or 1 time
matchObject = pattern.search(message)
print(matchObject.group())

# will not match, because ? matches only if it appears 0 or 1 time
message = 'Adventure of Batwowowowoman'
pattern = re.compile(r'Bat(wo)?man') # ? telling that 'wo' is optional, can appear 0 or 1 time
matchObject = pattern.search(message)
print(matchObject)

# Match the phone number with or without area code.
message = 'I am Manoj Kumar, Please reach me at +91 9586743265 or 9438710992.'
pattern = re.compile('(\+\d\d\ )?\d\d\d\d\d\d\d\d\d\d')
matchObject = pattern.search(message)
print(matchObject.group())


#Match zero or more occurences with *.
message = 'Adventure of Batman'
pattern = re.compile(r'Bat(wo)*man') # * is telling that 'wo' can appear zero or more times
matchObject = pattern.search(message)
print(matchObject.group())

message = 'Adventure of Batwoman'
pattern = re.compile(r'Bat(wo)*man') # * is telling that 'wo' can appear zero or more times
matchObject = pattern.search(message)
print(matchObject.group())

message = 'Adventure of Batwowowoman'
pattern = re.compile(r'Bat(wo)*man') # * is telling that 'wo' can appear zero or more times
matchObject = pattern.search(message)
print(matchObject.group())

# Match one or more occurences with +
message = 'Adventure of Batwoman'
pattern = re.compile(r'Bat(wo)*man') # + is telling that 'wo' can appear one or more times
matchObject = pattern.search(message)
print(matchObject.group())

message = 'Adventure of Batwowowoman'
pattern = re.compile(r'Bat(wo)*man') # + is telling that 'wo' can appear one or more times
matchObject = pattern.search(message)
print(matchObject.group())

# Match a word for n number times
message = 'I sad HaHaHa'
pattern = re.compile(r'(Ha){3}')
matchObject = pattern.search(message)
print(matchObject.group())

# Match 3 phone numbers in a row
message = 'I am Manoj Kumar, Please reach me at 9586743265, 9438710992, 94448509876'
pattern = re.compile('(\d\d\d\d\d\d\d\d\d\d(, )?){3}')
matchObject = pattern.search(message)
print(matchObject.group())

# Match a word for minimum of x times and maximum of y times
message = 'I said HaHaHa'
pattern = re.compile(r'(Ha){3,5}') # match 'Ha' if it repeates for 3 or 5 times
matchObject = pattern.search(message)
print(matchObject.group())

# Match phone number
message = 'I am Manoj Kumar, Please reach me at +91 9586743265'
pattern = re.compile('(\+\d\d )?(\d){10}') # area code is optional and phone number is 10 digits
matchObject = pattern.search(message)
print(matchObject.group())

# Greedy Check
message = '1234567890'
pattern = re.compile(r'(\d){3,5}') # match digits with length of minimum 3 and maximum 5
matchObject = pattern.search(message)
# It return '12345'. Because python do greedy search. It matches for maximum possible length
print(matchObject.group())

# Non Greedy Check
message = '1234567890'
pattern = re.compile(r'(\d){3,5}?') # match digits with length of minimum 3 and maximum 5
                                    # ? says pyhton to match as non greedy. So it returns minimum of 3 characters matched '123'
matchObject = pattern.search(message)
# It return '12345'. Because python do greedy search. It matches for maximum possible length
print(matchObject.group())
