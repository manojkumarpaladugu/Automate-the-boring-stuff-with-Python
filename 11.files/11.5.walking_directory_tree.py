import os

for folderName, subFolderList, fileList in os.walk('C:\\'):
    print('Folder Name:', folderName)
    print('Sub folders in', folderName, 'are:', subFolderList)
    print('Files in', folderName, 'are:', fileList)
    print()
