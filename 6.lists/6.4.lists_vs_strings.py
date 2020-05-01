# many methods we do with strings can also be done with strings
# list is a collection of any type items
# string is a collection of characters
# list a mutable, means we can change its items.
# strings are immutable, means we canot change characters inside string

# mutable values like lists can be modified in place
# immutable values like strings can not be modified in place

import copy

print('Lists are mutable. i.e if we assign mylist1 to mylist2, python does not create a new copy, instead it gives reference')
print('if you modify mylist2, then mylist1 also gets modified, because both are pointing to same memory')
mylist1 = [1, 2, 3, 4, 5]
mylist2 = mylist1
mylist2[0] = 10
print(mylist1)
print(mylist2)
print('')

print('Strings are immutable. So assigning str1 to str2 create a new copy of string')
print('As strings are immutable, even though we modify str2, str1 remains same')
str1 = 'Hello Manoj'
str2 = str1
str2 = 'Hello Arya'
print(str1)
print(str2)
print('')

# modifying a immutable string
print('modifying a immutable string')
str3 = 'Hello Manoj Kumar'
print(str3)
str3 = str3[0:6] + 'Venky'
print(str3)
print('')

print('passing a list and modifying inside another function')
# passing list to function
def my_function(my_list):
    mylist.append('Hello')

mylist = [1, 2, 3, 4]
print(mylist)
my_function(mylist)
print(mylist)
print('')

print('Deep copy a list to another list, This does not effect changes in one list on the other')
mylist1 = [1, 2, 3, 4, 5]
mylist2 = copy.deepcopy(mylist1)
mylist2[0] = 'Good'
print(mylist1)
print(mylist2)
print('')

# line continution
print('Hey, ' + \
      'thats all for today')
print('')

#we can't modify a string, because string is immutable
print('Trying to modify a string')
str4 = 'Hello Manoj'
str4[0] = 'h'
print(str4)
print('')

