import os
import shutil

os.chdir('FilesToSort')
print("Current directory is", os.getcwd())

names = []

for filename in os.listdir('.'):
    if not os.path.isdir(filename):
        extension_index = filename.find(".")
        extension = filename[extension_index:]
        if extension not in names:
            names.append(extension)

for extension in names:
    try:
        os.mkdir(extension)
    except:
        pass

for filename in os.listdir('.'):
    if not os.path.isdir(filename):
        extension_index = filename.find(".")
        extension = filename[extension_index:]
        shutil.move(filename, extension)
