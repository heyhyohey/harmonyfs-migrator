import os
import sys
import time
import harmonyfs_migrator as migrator
import harmonyfs_file_picker as picker

# Global variables
if len(sys.argv) != 5:
    print("Usage: python3 digestor_main.py [upper_layer_path] [lower_layer_path] [merged_layer_path] [policy]")
    sys.exit(1)

UPPER_HOME = sys.argv[1]
LOWER_HOME = sys.argv[2]
MERGED_HOME = sys.argv[3]
picker.policy = sys.argv[4]

# Remove the last '/'
if UPPER_HOME[-1] == "/":
    UPPER_HOME = UPPER_HOME[:-1]
if LOWER_HOME[-1] == "/":
    LOWER_HOME = LOWER_HOME[:-1]
if MERGED_HOME[-1] == "/":
    MERGED_HOME = MERGED_HOME[:-1]

print("HarmoyFS Migrator")
print("Upper layer: " + UPPER_HOME)
print("Lower layer: " + LOWER_HOME)
print("Merged layer: " + MERGED_HOME)
print("Policy: " + picker.policy)

# Check remaining space periodically
while True:
    pmem_stat = os.popen("df | grep pmem0").read()
    pmem_stat = str(pmem_stat)

    if pmem_stat == "":
        print("Warnning: No mounted pmem device")
        sys.exit(1)

    pmem_stat = ' '.join(pmem_stat.split())
    pmem_stat = int(list(pmem_stat.split())[4][:-1])
    print("Used space of the upper layer: " + str(pmem_stat) + "%")
    
    # If remaining space is above the pm threshold
    if pmem_stat <= 50:
        migrator.migration_to_upper(UPPER_HOME, LOWER_HOME, MERGED_HOME)
    # If remaining space is the threshold
    elif pmem_stat >= 80:
        migrator.migration_to_lower(UPPER_HOME, LOWER_HOME, MERGED_HOME)

    time.sleep(1)

