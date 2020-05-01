import os

PathString = 'C:\\Users\\mpalad1x\\Desktop\\spam.jpg'
print('Path string:', PathString)
print('')

RawPathString = r'C:\Users\mpalad1x\Desktop\spam.jpg'
print('Raw path string:', RawPathString)
print('')

RelativePath = os.path.join('folder1', 'folder2', 'folder3', 'spam.jpg')
print('Join path:', RelativePath)
print('')

CwdString = os.getcwd()
print('Current Working Directory:', CwdString)
print('')

AbsolutePath = os.path.abspath('spam.jpg')
print('Absolute Path:', AbsolutePath)
print('')

AbsolutePath = os.path.abspath(r'..\..\spam.jpg')
print('Absolute Path:', AbsolutePath)
print('')

DirPath = 'C:\\'
os.chdir(DirPath)
print('Changed directory to:', os.getcwd())
print('')

path = r'..\..\spam.jpg'
print('is', path, 'abosule path?', os.path.isabs(path))
print('')

Path = r'C:\Users\mpalad1x\Desktop\spam.jpg'
print('Path:', Path)
print('Dir Name:', os.path.dirname(Path))
print('Base Name:', os.path.basename(Path))
print('')

Path = r'C:\Users\mpalad1x\Desktop\spam.jpg'
print('is', Path, 'exists?', os.path.exists(Path))
print('')

Path = r'C:\Users\mpalad1x\Desktop\spam.jpg'
print('is', Path, 'file?', os.path.isfile(Path))
print('')

Path = r'C:\Users\mpalad1x\Desktop'
print('is', Path, 'dir?', os.path.isdir(Path))
print('')

Path = r'C:\Windows\System32\calc.exe'
print('size of', Path, 'is', os.path.getsize(Path))
print('')

print('list of directories in C:\\:', os.listdir('C:\\'))
print('')
