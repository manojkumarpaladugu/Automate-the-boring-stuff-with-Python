
# print local scope variable message
def printLocalVariable(name):
    message = 'Hello'
    print(message, name)

def printGlobalVariable(name):
    print(message, name)

def modifyGlobalVariable():
    global message
    message = 'Good Morning'

message = 'Hi'  # global variable
name = 'Manoj'

# print local variable message
print('')
print('print local variable message')
printLocalVariable(name)

# print global variable message
print('')
print('print global variable message')
printGlobalVariable(name)

# modify global variable message
print('')
print('modify global variable message')
modifyGlobalVariable()
print(message, name)
