import shutil
import os

if not os.path.exists('folder1'):
    os.mkdir('folder1')

FileObj = open(r'folder1\sample1.txt', 'w')
FileObj.write('Hello World\n')
FileObj.close()

FileObj = open(r'folder1\sample2.txt', 'w')
FileObj.write('I am Manoj, Learning python is interesting')
FileObj.close()

if not os.path.exists('folder2'):
    os.mkdir('folder2')
    
shutil.copy(r'folder1\sample2.txt', r'folder2\sample2.txt')
shutil.copytree(r'folder1', r'folder2\folder1')

if not os.path.exists('temp'):
    os.mkdir('temp')
    
shutil.move(r'folder1\sample1.txt', r'temp\sample1.txt')
