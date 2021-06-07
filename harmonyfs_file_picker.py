import os
import random
import psutil
import datetime

policy = "random"

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
    while True:
        picked_file = random.choice(files)
        if check_in_use(picked_file) == False:
            break
    return picked_file

# Pick the most recently used file
def pick_mru(files, path):
    while True:
        accessed_dates = os.popen("du --time=access -a " + path + "| awk '{ print $2 }'").read()
        accessed_dates = accessed_dates.split("\n")
        del accessed_dates[-1:-3:-1]

        accessed_time = os.popen("du --time=access -a " + path + "| awk '{ print $3 }'").read()
        accessed_time = accessed_time.split("\n")
        del accessed_time[-1:-3:-1]

        files = os.popen("du --time=access -a " + path + "| awk '{ print $4 }'").read()
        files = files.split("\n")
        del files[-1:-3:-1]

        files_accessed_time = {}
        for accessed_info in zip(files, accessed_dates, accessed_time):
            accessed_datetime = datetime.datetime.strptime(
                    accessed_info[1] + " " + accessed_info[2]
                    , "%Y-%m-%d %H:%M")
            files_accessed_time[accessed_info[0]] = accessed_datetime

        picked_file = max(files_accessed_time)

        if check_in_use(picked_file) == False:
            break
        else:
            del(files_accessed_time[picked_file])

        if files_accessed_time == {}:
            return None
            
    return picked_file

# Pick the least recently used file
def pick_lru(files, path):
    while True:
        accessed_dates = os.popen("du --time=access -a " + path + "| awk '{ print $2 }'").read()
        accessed_dates = accessed_dates.split("\n")
        del accessed_dates[-1:-3:-1]

        accessed_time = os.popen("du --time=access -a " + path + "| awk '{ print $3 }'").read()
        accessed_time = accessed_time.split("\n")
        del accessed_time[-1:-3:-1]

        files = os.popen("du --time=access -a " + path + "| awk '{ print $4 }'").read()
        files = files.split("\n")
        del files[-1:-3:-1]

        files_accessed_time = {}
        for accessed_info in zip(files, accessed_dates, accessed_time):
            accessed_datetime = datetime.datetime.strptime(
                    accessed_info[1] + " " + accessed_info[2]
                    , "%Y-%m-%d %H:%M")
            files_accessed_time[accessed_info[0]] = accessed_datetime

        picked_file = min(files_accessed_time)

        if check_in_use(picked_file) == False:
            break
        else:
            del(files_accessed_time[picked_file])

        if files_accessed_time == {}:
            return None
            
    return picked_file

# Pick a file in the list of files
def pick_from_dir(path, layer):
    global policy

    files = os.popen("du -a " + path + "| awk '{ print $2 }'").read()
    files = files.split("\n")
    files.remove(path)
    files.remove('')

    dirs = os.popen("du " + path + "| awk '{ print $2 }'").read()
    dirs = dirs.split("\n");
    dirs.remove(path)
    dirs.remove('')

    only_files = [ x for x in files if x not in dirs ]

    if only_files == []:
        return None
    else:
        if policy == "random":
            picked_file = pick_random(only_files)
        elif policy == "access":
            if layer == "upper":
                picked_file = pick_lru(only_files, path)
            elif layer == "lower":
                picked_file = pick_mru(only_files, path)

    return picked_file 

if __name__=="__main__":
    print(pick_from_dir("/mnt/pmem/upper"))
    #check_in_use("/mnt/pmem/upper/a.c")
