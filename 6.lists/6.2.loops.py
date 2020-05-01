# generate list using range function
print('generate list using range function')
mylist = list(range(0, 4))
print(mylist)
print('')

# for loop using list list generated from range()
print('for loop using list generated from range()')
for i in range(0, 4):
    print(i)
print('')

# for loop using list variable
print('for loop using list variable')
mylist = [1.1, 1.2, 1.3]
for i in mylist:
    print(i)
print('')

# for loop using list
print('for loop using list')
for i in ['Hello', 'Hi', 'Good Mornign']:
    print(i)
print('')

# indexing a list
print('indexing a list')
mylist = [ 'Manoj', 'Arya', 'Mani' ]
for i in range(len(mylist)):
    print('Index ' + str(i) + ' of mylist: ' + mylist[i])
print('')

# multiple assignment
print('multiple assignment')
animals = [ 'dog', 'cat', 'tiger' ]
animal1, animal2, animal3 = animals
print('animal1:', animal1)
print('animal2:', animal2)
print('animal3:', animal3)
print('')

# swap variables using multiple assignment
print('swap variables using multiple assignment')
a = 10
b = 20
print('before swap:', 'a:', a, 'b:', b)
a, b = b, a
print('after swap:', 'a:', a, 'b:', b)
print('')

# augmented assignment
print('augmented assignment')
temp = 10
temp = temp + 1
temp += 1
print('temp:', temp)
