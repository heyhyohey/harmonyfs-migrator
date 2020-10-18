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
def pick_from_dir(root_path):
    files = get_files(root_path)

    if files == []:
        return None
    else:
        file = pick_random(files)
        return file


if __name__=="__main__":
    print(pick_from_dir("/mnt/pmem/pmem"))
    print(pick_from_dir("/mnt/ssd"))
