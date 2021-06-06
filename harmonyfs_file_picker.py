import os
import random

# Find all files from the input path
def get_files(path):
    files = os.listdir(path)
    return files

# Pick a random file in the list of files
def pick_random(files):
    return random.choice(files)

# Pick a file in the list of files
def pick_from_dir(path):
    files = os.popen("du -a " + path + "| awk '{ print $2 }'").read()
    files = files.split("\n")
    files.remove(path)
    files.remove('')

    dirs = os.popen("du " + path + "| awk '{ print $2 }'").read()
    dirs = dirs.split("\n");
    dirs.remove(path)
    dirs.remove('')

    only_files = [ x for x in files if x not in dirs ]

    if files == []:
        return None
    else:
        file = pick_random(only_files)
        return file


if __name__=="__main__":
    print(pick_from_dir("/mnt/pmem/upper"))
