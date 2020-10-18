import os
import digestor_file_picker as picker

def migration_to_lower():
    upper_dir_path = "/mnt/pmem/pmem/"
    lower_dir_path = "/mnt/ssd/"
    fname = picker.pick_from_dir(upper_dir_path)

    if fname == None:
        print("No files in the " + upper_dir_path)
        return

    original_path= upper_dir_path + fname
    new_path = lower_dir_path + fname
    command = "mv " + original_path + " " + new_path
    print(command)
    os.system(command)
    print("migration to lower!!!")

def migration_to_upper():
    upper_dir_path = "/mnt/pmem/pmem/"
    lower_dir_path = "/mnt/ssd"
    fname = picker.pick_from_dir("/mnt/ssd/")

    if fname == None:
        print("No files in the " + lower_dir_path)
        return

    original_path= lower_dir_path + fname
    new_path = upper_dir_path + fname
    command = "mv " + original_path + " " + new_path
    print(command)
    os.system(command)
    print("migration to upper!!!")


if __name__ == "__main__":
    migration_to_upper()
    migration_to_lower()
