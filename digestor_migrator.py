import subprocess
import digestor_file_picker as picker

def migration_to_lower():
    upper_dir_path = "/mnt/pmem/pmem/"
    lower_dir_path = "/mnt/ssd/"
    user_dir_path = "/mnt/overlay/"
    fname = picker.pick_from_dir(upper_dir_path)

    if fname == None:
        print("No files in the " + upper_dir_path)
        return

    original_path= user_dir_path + fname
    new_path = lower_dir_path + fname
    clear_path = upper_dir_path + fname
    cp_command = "cp " + original_path + " " + new_path
    print(cp_command)
    subprocess.check_call(["cp", original_path, new_path])
    rm_command = "rm " + original_path + " " + clear_path
    print(rm_command)
    subprocess.check_call(["rm", original_path, clear_path])
    print("migration to lower!!!")

def migration_to_upper():
    upper_dir_path = "/mnt/pmem/pmem/"
    lower_dir_path = "/mnt/ssd/"
    fname = picker.pick_from_dir(lower_dir_path)

    if fname == None:
        print("No files in the " + lower_dir_path)
        return

    original_path= lower_dir_path + fname
    new_path = upper_dir_path + fname
    command = "mv " + original_path + " " + new_path
    print(command)
    subprocess.check_call(["mv", original_path, new_path])
    print("migration to upper!!!")


if __name__ == "__main__":
    migration_to_upper()
    migration_to_lower()
