# list is a value which contains multiple values
# we can store same or different types of data in it
# a list can store another list inside it

# list with same type of data
sampleList = ['cat', 'bat', 'rat']
print('sampleList[0]:',sampleList[0])

# list wit different types of data
sampleList = ['apple', 'ball', 'cellphone', 1, 2, 3, 4.4, 5.5, 6.6]
print('sampleList[6]:',sampleList[6])

# slicing a list
# we can get multiple items from list using slice
slicedList = sampleList[1:3]
print('slicedList:', slicedList)

# slice from 3rd last to last
slicedList = sampleList[-3:]
print('slicedList:', slicedList)

# list within list
sampleList = [ [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ] ]
print('sampleList[1]:',sampleList[1])
print('sampleList[1][1]:',sampleList[1][1])

# modify existing item from list
sampleList[1] = 'Hello'
print('sampleList at index 1 is modified: ',sampleList)

# modify existing values with slicing
sampleList[1:3] = [ 1, 2, 3, 4, 5 ]
print('sampleList modified: ',sampleList)

# delete an item from the list
del sampleList[0]
print('sampleList after deletion index 0: ',sampleList)

# length of list
print('length of sampleList: ', len(sampleList))

# list replication
sampleList = sampleList * 2
print('list replication: ',sampleList)

# convert string to list
sampleList = list('Hello')
print('convert Hello to list: ',sampleList)

# convert list to string
string = ''.join(sampleList)
print('convert list to string:', string)

# list cancatenation
sampleList = sampleList + [1, 2, 3]
print('list cancatenation:', sampleList)

# in and not in operators
list1 = [ 'Arun', 'Sai', 'siva', 'Manoj' ]
print('Manoj' in list1)

print('Manoj' not in [ 'Arun', 'Sai', 'siva', 'Manoj' ])
