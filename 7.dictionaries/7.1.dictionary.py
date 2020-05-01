import pprint

# Dictionaries store data as key and value.
# Dictionaries are mutable
# Dictionaries don't have any order.

dict1 = { 'Name':'Manoj', 'Age':25, 'Hobby':'Riding' }
dict2 = { 'Hobbies':'Riding', 'Age':25, 'Name':'Manoj' }
dict3 = dict2 # as dictionaries are mutable, i.e Variables hold references to dictionary values, not the dictionary values it self
print('dict1:',dict1)
print('dict1:',dict2)
print('Comparing two unordered dictionaries')
# Dictionaries matches, even though two dictionaries are in different order, as they are having similar keys and values
if dict1 == dict2:
    print('dict1 and dict2 are same')
else:
    print('dict1 and dict2 are not same')
print('')


print('Check if a key exists in dictionary')
if 'Name' in dict1.keys():
    print('Key \'Name\' exists in dict1')
print('')

print('Check if a value exists in dictionary')
if 'Manoj' in dict1.values():
    print('Value \'Manoj\' exists in dict1')
print('')

print('Print all the keys exists in dict2')
print(list(dict2.keys()))
print('')

print('Print all the values exists in dict2')
print(list(dict2.values()))
print('')

print('Print all the items in the dict1')
print(list(dict1.items()))
print('')

print('Print all the keys exists in dict1 using for loop')
for key in dict1.keys():
    print(key)
print('')

print('Print all the values exists in dict1 using for loop')
for value in dict1.values():
    print(value)
print('')

print('Print all the keys and values of dict2 using for loop multiple assignment')
for key, value in dict1.items():
    print(key, value)
print('')

print('Print key value pair as tuple')
for _tuple in dict1.items():
    print(_tuple)
print('')

print('Get value of key using get() method')
print('Name:',dict1.get('Name', ''))

print('Get value of key using get() method')
print('Profession:',dict1.get('Profession', 'Unknown'))

print('Count occurence of each character in a string')
message = 'Sunrise at Nandhi hills is best during december'
count = {}
print('Message:',message)
for character in message:
    count.setdefault(character, 0) # can set a value if key doesn't exist
    count[character] = count[character] + 1
pprint.pprint(count)
print('')
    
