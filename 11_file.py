import os

print(os.sep)
print(os.getcwd())
# os.chdir('C:\\')
print()

# . this directory
# .. parent directory

print(os.path.abspath('cool bird.jpg'))
print(os.path.relpath('cool bird.jpg', 'C:\\Users\\shubh\\Desktop\\Code'))
print()

print(os.path.dirname(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\cool bird.jpg'))
print(os.path.basename(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\cool bird.jpg'))
print()

print(os.path.exists(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\cool bird.jpg'))
print(os.path.isfile(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\cool bird.jpg'))
print(os.path.isdir (r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\cool bird.jpg'))
print(os.path.getsize(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\cool bird.jpg'))
print(os.listdir(r'C:\Users\shubh\Desktop\Code\Courses'))
print()

totalSize=0
for filename in os.listdir(r'C:\Users\shubh\Desktop\Code\Courses'):
    if not os.path.isfile(os.path.join(r'C:\Users\shubh\Desktop\Code\Courses', filename)):
        continue
    totalSize+= os.path.getsize(os.path.join(r'C:\Users\shubh\Desktop\Code\Courses', filename))
print(totalSize)
print()

######################################################################################################

file= open(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\batman.txt')
print(file.read())
file.close()

# file= open(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\batman.txt','a')
# file.write('\n-Harvey Dent')
# file.close()
print()


import shelve
shelfFile= shelve.open('info')
shelfFile['Footballers'] = ['Messi', 'Ronaldo', 'Zlatan', 'De Bruyne']

print(shelfFile['Footballers'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
print()

######################################################################################################

import shutil

# copy file
print(shutil.copy(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\cool bird.jpg', r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample\bird.jpg'))

# copy folder
print(shutil.copytree(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample', r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample_backup'))

# move file
print(shutil.move(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample_backup\cool bird.jpg', r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample'))

# no rename function, move it to same folder and change name

######################################################################################################

# These will permanently delete, not move to recycle bin
# delete file
os.unlink(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample\bird.jpg')

# delete folder (has to be empty)
os.rmdir(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample_backup')

# delete folder with content
shutil.rmtree(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample_backup')

import send2trash
send2trash.send2trash(r'C:\Users\shubh\Desktop\Code\Courses\Udemy Automate the Boring Stuff\sample\cool bird.jpg')

######################################################################################################

for folderName, subFolders, fileNames in os.walk(r'C:\Users\shubh\Desktop\Code\Courses'):
    print('The folder is: ' + folderName)
    print('The subfolder in ' + folderName + ' are: ' + str(subFolders))
    print('The files in ' + folderName + ' are: ' + str(fileNames))
    print()
