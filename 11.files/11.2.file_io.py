# create file sample.txt in write mode only
print('create file sample.txt in write mode only')
FileObj = open('sample.txt', 'w')
Data = """Helllo World
How are you?
I am fine"""
count = FileObj.write(Data)
print('Written', count, 'characters in to the file')
FileObj.close()
print('')

# open sample.txt in read only mode and read contents as a single string
print('open sample.txt in read only mode and read contents as a single string')
FileObj = open('sample.txt', 'r')
Data = FileObj.read()
FileObj.close()
print('Contents:', Data)
print('')

# open sample.txt in read only mode and read contents as a list
print('open sample.txt in read only mode and read contents as a list')
FileObj = open('sample.txt', 'r')
DataAsList = FileObj.readlines()
FileObj.close()
print('Data List:', DataAsList)
print('')

# Open sample.txt in append mode and add text
print('Open sample.txt in append mode and add text')
FileObj = open('sample.txt', 'a')
Data = 'Learning python is interesting\n'
count = FileObj.write(Data)
print('Written', count, 'characters in to the file')
FileObj.close()
print('')

