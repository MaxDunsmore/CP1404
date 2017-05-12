import os

print("Current directory is", os.getcwd())
os.chdir('Lyrics/Christmas')


os.chdir('..')
for dir_name, subdir_list, file_list in os.walk('.'):

    for filename in file_list:
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
        extension = new_name.find(".")

        if "_" in new_name:  # have no idea how to deal with names with no spaces. tried and failed.
            new_name = new_name[:extension].title() + new_name[extension:]

        os.rename(dir_name + os.sep + filename, dir_name + os.sep + new_name)  # no idea what os.sep is
