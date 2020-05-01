# example 1
print('example 1')
message = 'Hello, I am new to python'
count = 0
while count < 5:
    print(message)
    count += 1

# example 2
print('example 2')
name = ''
while name != 'Manoj':
    print('Enter your name correctly')
    name = input()


# infinite loop
print('example 3')
while True:
    print('Enter your name: ')
    name = input()
    if name == 'Manoj':
        break;

print('example 4')
while True:
    print('When india got independence?')
    year = input()
    if int(year) == 1947:
        break
    else:
        print('incorrect')
        continue
print('END of the program')
    
