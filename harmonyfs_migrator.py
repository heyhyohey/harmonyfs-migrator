import subprocess
import harmonyfs_file_picker as picker
import os

def check_path(path):
    for i in range(len(path)-1, -1, -1):
        if path[i] == '/':
            path = path[:i]
            break

    if not os.path.exists(path):
        os.makedirs(path)

def migration_to_lower(upper_dir_path, lower_dir_path, merged_dir_path):
    picked_file = picker.pick_from_dir(upper_dir_path, "upper")

    if picked_file == None:
        #print("No files in the " + merged_dir_path)
        return

    from_path = merged_dir_path + picked_file.replace(upper_dir_path, "")
    to_path = lower_dir_path + picked_file.replace(upper_dir_path, "")
    
    check_path(to_path)

    subprocess.call(["mv", from_path, to_path])
    subprocess.call(["rm", "-rf", picked_file])
    subprocess.call(["ln", "-s", to_path, from_path])
    #print("Move " + from_path + " to " + to_path)

def migration_to_upper(upper_dir_path, lower_dir_path, merged_dir_path):
    picked_file = picker.pick_from_dir(lower_dir_path, "lower")

    if picked_file == None:
        #print("No files in the " + lower_dir_path)
        return

    to_path = merged_dir_path + picked_file.replace(lower_dir_path, "")
    upper_path = upper_dir_path + picked_file.replace(lower_dir_path, "")

    check_path(to_path)

    subprocess.call(["rm", "-rf", to_path])
    subprocess.call(["rm", "-rf", upper_path])
    subprocess.call(["mv", picked_file, to_path])
    #print("Move " + picked_file + " to " + to_path)


if __name__ == "__main__":
    migration_to_lower("/mnt/pmem/upper", "/mnt/lower", "/mnt/merged")
    #migration_to_upper("/mnt/pmem/upper", "/mnt/lower", "/mnt/merged")
    #check_path("/hello/my/name/is")
