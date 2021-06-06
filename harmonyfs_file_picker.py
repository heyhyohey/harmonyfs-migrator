import os
import random
import psutil

# Find all files from the input path
def get_files(path):
    files = os.listdir(path)
    return files

# Check whether file is ussig
def check_in_use(path):
    origin_path = path
    for i in range(len(path)-1, -1, -1):
        if path[i] == '/':
            swap_file_name = "." + path[i+1:] + ".swp"
            path = path[:i]
            break

    swap_file_path = path + "/" + swap_file_name

    for proc in psutil.process_iter():
        if proc.open_files() == []:
            continue
        opened_file_path = proc.open_files()[0].path
        if opened_file_path == swap_file_path:
            return True
        elif opened_file_path == origin_path:
            return True

    return False


# Pick a random file in the list of files
def pick_random(files):
    it = psutil.process_iter()
    while True:
        picked_file = random.choice(files)
        if check_in_use(picked_file) == False:
            break
    return picked_file

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
    #print(pick_from_dir("/mnt/pmem/upper"))
    check_in_use("/mnt/pmem/upper/a.c")
