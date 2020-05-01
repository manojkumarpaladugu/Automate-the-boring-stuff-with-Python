name = 'Manoj'
place = 'Chennai'
time = 8
AM_PM = 'PM'

# string formatting style 1
message = 'Hello ' + name + ', you are invited to the party ' + str(time) + AM_PM + ' at ' + place
print(message)

# string formatting style 2
print('Hello %s, you are invited to the party %d %s at %s'%(name, time, AM_PM, place))

# string formatting style 3
print('Hello {0}, you are invited to the party {1} {2} at {3}'.format(name, time, AM_PM, place))
