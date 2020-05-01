import os
import shutil

os.unlink(r'temp\sample1.txt')
os.rmdir(r'temp') # deletes folder only if it is empty

shutil.rmtree(r'folder2')
