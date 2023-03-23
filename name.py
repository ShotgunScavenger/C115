import os

source = "C:/Users/pangp/Downloads/main.txt"
dest = "C:/Users/pangp/Downloads/newfile.txt"
os.rename(source, dest)
print('File has been renamed')