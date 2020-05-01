import re

# group the regular expression and then find country code
message = 'I am Manoj Kumar, You can contact me at +91 9591039137 or +91 9291039127'
pattern = re.compile('(\+\d\d) (\d\d\d\d\d\d\d\d\d\d)') # grouped expression
matchObject = pattern.search(message) # gives first occurence
countryCode = matchObject.group(1)
phoneNumber = matchObject.group(2)
print('Country Code:', countryCode, 'Phone Number:', phoneNumber)


# looping through all the matches
for match in re.finditer(pattern, message):
    print(match.group())


# using pipe character
message = 'Batmobile is lost'
# search for word starts with Bat and contains any of the words mobile,copter,bat
pattern = re.compile('Bat(man|mobile|copter|bat)')
matchObject = pattern.search(message)
print(matchObject)
