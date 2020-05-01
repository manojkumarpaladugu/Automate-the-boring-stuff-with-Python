#Methods in list
# methods are functions that are called on values

mylist = [ 'Hello', 'Hi', 'Hey' ]
print(mylist)
print('')

# Get the index of value in list
print('Get the index of string')
index = mylist.index('Hey')
print('Index of Hey is', index)
print('')

# append the string to list
print('Append the value to list')
mylist.append('Howdy')
print(mylist)
print('')

# insert the string at specified position to a list
print('Append the string at specified position')
mylist.insert(1, 'Namaste')
print(mylist)
print('')

# remove an item from the list by specifying value
print('remove an item from the list by specifying value')
mylist.remove('Hello')
print(mylist)
print('')

# delete an item from the list by specifying index
print('delete an item from the list by specifying index')
del mylist[0]
print(mylist)
print('')

# sort a list
print('sort a list')
mylist = [1, 8, 4, 6, 2, 5]
mylist.sort()
print(mylist)
print('')

# sort a list in reverse
print('sort a list in reverse')
mylist.sort(reverse=True)
print(mylist)
print('')

# by default, list is sorted as ASCII-betically.
# ascii values of 'A' is less than 'a'. So python will sort capital letters first and then small letters.
print('sort as per ASCII')
mylist = [ 'ccc', 'bbb', 'AAA', 'BBB', 'CCC', 'aaa' ]
mylist.sort();
print(mylist)
print('')

print('sort alphabetically')
mylist = [ 'AAA', 'aaa', 'BBB', 'bbb', 'CCC' ,'cccc' ]
mylist.sort(key=str.lower);
print(mylist)
print('')


