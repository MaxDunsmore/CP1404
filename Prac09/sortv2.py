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

for i in names:
    abc = input("what would you like to sort {:5} files into?".format(i))
    try:
        os.mkdir(abc)
    except:
        pass
    for filename in os.listdir('.'):
        if filename.endswith(i):
            shutil.move(filename, abc)



